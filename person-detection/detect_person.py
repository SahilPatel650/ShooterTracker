from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model(source="people.jpeg", show=False, conf=0.4, save=True)[0].boxes
bboxes = []
for i in range(len(results.cls)):
    if results.cls[i] != 0:
        continue
    bboxes.append(results.data[i].cpu().tolist())

print(bboxes)
