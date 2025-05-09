import cv2
import os
import pickle

IMG_FOLDER = '../data/labeled_frames'
OUTPUT_FILE = '../data/head_labels.pkl'
TOLERANCE = 10  # margem de erro em pixels

annotations = []

# Percorre todas as imagens
images = [img for img in os.listdir(IMG_FOLDER) if img.endswith(('.png', '.jpg'))]
images.sort()

for img_name in images:
    path = os.path.join(IMG_FOLDER, img_name)
    img = cv2.imread(path)
    if img is None:
        print(f"Erro ao carregar {img_name}")
        continue

    img = cv2.resize(img, (1600, 900))
    height = img.shape[0]
    crosshair_y = height // 2

    print(f"Selecione a cabeça do inimigo em {img_name}")
    roi = cv2.selectROI("Annotate Head", img, False)
    cv2.destroyWindow("Annotate Head")

    x, y, w, h = roi
    head_center_y = y + h // 2

    # Define a classe com base na posição relativa
    diff = head_center_y - crosshair_y
    if abs(diff) <= TOLERANCE:
        label = "aligned"
    elif diff < 0:
        label = "above"
    else:
        label = "below"

    annotations.append({
        'filename': img_name,
        'head_x': x,
        'head_y': y,
        'head_w': w,
        'head_h': h,
        'head_center_y': head_center_y,
        'crosshair_y': crosshair_y,
        'label': label
    })

# Salva no arquivo .pkl
with open(OUTPUT_FILE, 'wb') as f:
    pickle.dump(annotations, f)

print(f"\n✅ Anotações salvas em {OUTPUT_FILE}")
