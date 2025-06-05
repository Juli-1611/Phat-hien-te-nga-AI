import cv2
import time
import requests
from ultralytics import YOLO

BOT_TOKEN = '7679592044:AAFSPK4LZjQZtDdgw7K8vFpCeYUZZGfrMQ8'  
CHAT_ID = '5903178168' 


model = YOLO("runs/detect/yolov8_te_nga4/weights/best.pt") 


def send_telegram_alert(frame):
    timestamp = int(time.time())
    filename = f"fall_{timestamp}.jpg"
    cv2.imwrite(filename, frame)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {'photo': open(filename, 'rb')}
    data = {'chat_id': CHAT_ID, 'caption': '🚨 Phát hiện người té ngã!'}
    try:
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("📨 Đã gửi ảnh cảnh báo Telegram.")
        else:
            print("❌ Lỗi gửi Telegram:", response.text)
    except Exception as e:
        print("❌ Exception gửi Telegram:", e)


cap = cv2.VideoCapture(0)  


last_alert_time = 0
alert_cooldown = 10  # giây

print("🟢 Hệ thống nhận diện té ngã đang chạy... Nhấn 'q' để thoát.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Không lấy được khung hình từ camera.")
        break

    results = model(frame, verbose=False)

    fall_detected = False
    detected_count = 0  

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]  

            if name == 'Fall-Detected' and conf > 0.5:
                fall_detected = True
                detected_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                text = f"{name} {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.putText(frame, f"Detections: {detected_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if fall_detected and time.time() - last_alert_time > alert_cooldown:
        send_telegram_alert(frame)
        last_alert_time = time.time()

    cv2.imshow("Fall Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Thoát chương trình.")
        break

cap.release()
cv2.destroyAllWindows()
