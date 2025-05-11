import cv2
import os
import random

# === Configuration ===
VIDEO_PATH = "../data/video/valorant.mp4"
OUTPUT_DIR = "../data/frames"
NUM_FRAMES = 10  # Number of random frames to extract

# Open video file
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"Error: Cannot open video file at {VIDEO_PATH}")

# Get total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

if NUM_FRAMES > total_frames:
    print(f"Error: Video only has {total_frames} frames, cannot extract {NUM_FRAMES}.")

# Choose random frame indices
selected_indices = sorted(random.sample(range(total_frames), NUM_FRAMES))

# Read and save frames
saved_count = 0
for frame_index in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break
    if frame_index == selected_indices[saved_count]:
        filename = os.path.join(OUTPUT_DIR, f"frame_{frame_index:05d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        saved_count += 1
        if saved_count >= NUM_FRAMES:
            break

cap.release()
print("Done.")
