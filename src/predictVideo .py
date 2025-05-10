"""Predict crosshair alignment using a trained model on new gameplay video."""
import cv2
import pickle
import os
import numpy as np

VIDEO_PATH = '../data/video/valorant.mp4'
MODEL_PATH = '../models/aim_model.pkl'

with open(MODEL_PATH, 'rb') as f:
    clf = pickle.load(f)

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Erro ao abrir vídeo")
    exit()

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
crosshair_y = height // 2

frame_index = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1600, 900))
    height = frame.shape[0]
    crosshair_y = height // 2

    roi = frame[crosshair_y - 10:crosshair_y + 10, width // 2 - 10:width // 2 + 10]

    # Simulação: usuário anota a cabeça em algumas frames manualmente neste modo
    # Ou sistema detecta (futuro). Aqui vamos apenas testar com Y estático para demonstração

    diff = 0  # Simulação de diferença com a mira
    prediction = clf.predict([[diff]])[0]

    color = (0, 255, 0) if prediction == "aligned" else (0, 0, 255)
    cv2.putText(frame, f"Prediction: {prediction}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Prediction", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
