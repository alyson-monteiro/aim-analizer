# aim-analyzer/src/heads.py
import cv2
import os
import pickle
import random

VIDEO_PATH = '../data/video/valorant.mp4'
OUTPUT_FILE = '../data/head_labels.pkl'
NUM_FRAMES = 20

annotations = []

# Abrir vídeo
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("❌ Erro ao abrir o vídeo.")
    exit(1)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_indices = sorted(random.sample(range(total_frames), NUM_FRAMES))

print(f"Selecionando {NUM_FRAMES} frames aleatórios de {total_frames} disponíveis.")

for idx in frame_indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ret, frame = cap.read()
    if not ret:
        print(f"⚠️ Erro ao ler o frame {idx}")
        continue

    frame = cv2.resize(frame, (1600, 900))
    height = frame.shape[0]
    crosshair_y = height // 2


    print(f"Selecione a cabeça do inimigo no frame {idx}")
    roi = cv2.selectROI("Annotate Head", frame, False)
    cv2.destroyWindow("Annotate Head")

    x, y, w, h = roi
    head_center_y = y + h // 2

    diff = head_center_y - crosshair_y

    if diff < -5:
        label = "above"
    elif diff > 5:
        label = "bellow"
    else:
        label = "aligned"

    annotations.append({
        'frame_index': idx,
        'head_x': x,
        'head_y': y,
        'head_w': w,
        'head_h': h,
        'head_center_y': head_center_y,
        'crosshair_y': crosshair_y,
        'label': label
    })

cap.release()

# Criar diretório se necessário
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Salvar anotações
with open(OUTPUT_FILE, 'wb') as f:
    pickle.dump(annotations, f)

print(f"\n✅ {len(annotations)} anotações salvas em {OUTPUT_FILE}")
