from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolo11n.pt")

    def detect(self, frame):
        results = self.model(frame)

        detections = []

        for result in results:
            for box in result.boxes:

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                confidence = float(box.conf[0])
                class_id = int(box.cls[0])

                class_name = self.model.names[class_id]

                detections.append({
                    "name": class_name,
                    "confidence": confidence,
                    "box": (x1, y1, x2, y2)
                })

        return detections