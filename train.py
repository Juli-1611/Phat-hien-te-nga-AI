from ultralytics import YOLO

# model = YOLO("yolov8s.pt")  # hoặc yolov8n.pt nếu bạn muốn nhẹ hơn

# model.train(
#     data="C:/Hanh_dong_te_nga/data.yaml",  # Đường dẫn đến file yaml
#     epochs=5,
#     imgsz=640,
#     batch=16,
#     name="yolov8_te_nga",
#     workers=4,
    
# )
model = YOLO("runs/detect/yolov8_te_nga4/weights/best.pt")
results = model.predict("test.jpg", save=True)
