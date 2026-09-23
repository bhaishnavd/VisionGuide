import cv2

from detector import ObjectDetector
from direction import get_direction
from speech import speak


detector = ObjectDetector()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]

    detections = detector.detect(frame)

    for detection in detections:

        name = detection["name"]
        confidence = detection["confidence"]
        box = detection["box"]

        if confidence < 0.5:
            continue

        direction = get_direction(
            box,
            frame_width
        )

        message = f"{name} {direction}"

        print(message)

        # speak(message)

        x1, y1, x2, y2 = map(int, box)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{name} {confidence:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    cv2.imshow("Vision Assistant", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()