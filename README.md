🤖 HỆ ThỐng Nhận Diện Té Ngã Thông Minh sử dụng YOLOv8

Một hệ thống AI sử dụng mô hình YOLOv8 để nhận diện té ngã của con người trong thời gian thực. Dự án hướng tớ\u1i mục tiêu hỗ trợ giám sát người cao tuổi, người bệnh hoặc các tình huống khẩn cấp trong môi trường chăm sóc sức khỏe và an ninh.

🚀 Tính Năng Chính

🔍 Nhận diện té ngã chính xác trong video hoặc luồng camera thời gian thực.

🧠 Huấn luyện với tập dữ liệu bao gồm hành vi té ngã và các hoạt động bình thường.

📆 Sử dụng mô hình YOLOv8 tối ưu, dễ triển khai trên cả máy tính và thiết bị nhúng.

⚠️ Có thể tích hợp gửi cảnh báo qua email, Telegram, hoặc hệ thống IoT.

🎥 Hỗ trợ phân tích video offline và online (live webcam).

🛠️ Công Nghệ Sử Dụng

Ultralytics YOLOv8

Python 3.8+

OpenCV

NumPy

PyTorch

(Tuỳ chọn) Flask hoặc FastAPI cho giao diện web/API

📁 Cấu Trúc Thư Mục

fall-detection-yolov8/
├— datasets/              # Dữ liệu huấn luyện và kiểm thử
├— runs/                  # Kết quả huấn luyện từ YOLOv8
├— models/                # Các file mô hình đã huấn luyện (.pt)
├— detect.py              # Script phát hiện té ngã từ video
├— train.py               # Script huấn luyện mô hình
└— requirements.txt       # Thư viện cần thiết

📦 Cài Đặt

git clone https://github.com/ten-cua-ban/fall-detection-yolov8.git
cd fall-detection-yolov8
pip install -r requirements.txt

🧪 Huấn Luyện Mô Hình

Chuẩn bị dữ liệu theo định dạng YOLO (ảnh + file .txt gắn nhãn).

Cấu hình file data.yaml:

train: datasets/train/images
val: datasets/val/images
nc: 2
names: ['normal', 'fall']

Chạy huấn luyện:

yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640

📹 Phát Hiện Té Ngã

Từ video hoặc webcam:

yolo detect predict model=models/best.pt source=0  # Webcam
yolo detect predict model=models/best.pt source='video.mp4'

📊 Kết Quả

Mô hình

mAP@0.5

FPS (Webcam)

Size

YOLOv8n

87.2%

30 FPS

~6MB

YOLOv8s

91.5%

25 FPS

~22MB

📌 Ghi Chú

Hệ thống chỉ nhận diện té ngã nằm xuống, không phân loại các tư thế khác.

Nên sử dụng camera từ góc rộng, toàn thân để có hiệu quả tốt hơn.
