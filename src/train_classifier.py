"""Train a classifier to predict whether crosshair is aligned with the enemy's head."""
import cv2
import pickle
import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

with open('../data/head_labels.pkl', 'rb') as f:
    data = pickle.load(f)

X = []
y = []
for item in data:
    diff = item['head_center_y'] - item['crosshair_y']
    X.append([diff])
    y.append(item['label'])

X = np.array(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

os.makedirs('../models', exist_ok=True)  # ← cria a pasta se necessário


with open('../models/aim_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("✅ Model saved to ../models/aim_model.pkl")