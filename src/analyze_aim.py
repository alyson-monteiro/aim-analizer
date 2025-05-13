from ultralytics import YOLO
import cv2

VIDEO_PATH = '../data/video/valorant.mp4'
MODEL_PATH = '../runs/detect/train4/weights/best.pt'
TOLERANCE = 15  # margem de erro em pixels

model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("❌ Erro ao abrir o vídeo.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1600, 900))
    height, width = frame.shape[:2]
    crosshair_y = height // 2

    results = model(frame)[0]
    head_center_y = None

    # Detectar primeira cabeça
    for box in results.boxes:
        if int(box.cls[0]) == 0:  # classe "head"
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            head_center_y = (y1 + y2) // 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            break

    # Comparar com mira
    if head_center_y is not None:
        diff = head_center_y - crosshair_y
        if abs(diff) <= TOLERANCE:
            label = "aligned"
            color = (0, 255, 0)
        elif diff < 0:
            label = "below"
            color = (0, 255, 255)
        else:
            label = "above"
            color = (0, 0, 255)

        # Mostrar linha da mira e resultado
        cv2.line(frame, (0, crosshair_y), (width, crosshair_y), (200, 200, 200), 1)
        #cv2.circle(frame, (width // 2, head_center_y), 5, color, -1)
        cv2.putText(frame, f"Aim: {label}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    else:
        cv2.putText(frame, "No head detected", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)

    cv2.imshow("Aim Analyzer", frame)
    if cv2.waitKey(8) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
