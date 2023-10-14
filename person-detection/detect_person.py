from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model(source="/Users/ashwathkarunakaram/Documents/ShooterTracker/fire-and-gun-detection/screenshots/person1.jpg", show=True, conf=0.4, save=True)
