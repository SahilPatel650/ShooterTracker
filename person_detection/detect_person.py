from ultralytics import YOLO

def init_model():
    return YOLO('yolov8n.pt')

def inference(model, img):
    results = model(source=img, show=False, conf=0.4, save=False)[0].boxes
    bboxes = []
    for i in range(len(results.cls)):
        if results.cls[i] != 0:
            continue
        bboxes.append(results.data[i].cpu().tolist())
    return bboxes

