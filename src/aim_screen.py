import cv2
import numpy as np
import mss
from ultralytics import YOLO

MODEL_PATH = '../runs/detect/train4/weights/best.pt'
TOLERANCE = 15
WINDOW_NAME = 'Aim Analyzer'


def main():
    model = YOLO(MODEL_PATH)
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

        while True:
            screenshot = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

            height, width = frame.shape[:2]
            crosshair_y = height // 2

            results = model(frame)[0]
            head_center_y = None

            for box in results.boxes:
                if int(box.cls[0]) == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    head_center_y = (y1 + y2) // 2
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
                    break

            if head_center_y is not None:
                diff = head_center_y - crosshair_y
                if abs(diff) <= TOLERANCE:
                    label = 'aligned'
                    color = (0, 255, 0)
                elif diff < 0:
                    label = 'below'
                    color = (0, 255, 255)
                else:
                    label = 'above'
                    color = (0, 0, 255)

                cv2.line(frame, (0, crosshair_y), (width, crosshair_y), (200, 200, 200), 1)
                cv2.putText(frame, f'Aim: {label}', (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            else:
                cv2.putText(frame, 'No head detected', (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)

            cv2.imshow(WINDOW_NAME, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
