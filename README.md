# 🎯 Aim Analyzer – Valorant Crosshair Feedback with YOLOv8

> 📄 This README is also available in Portuguese:  
> 🇧🇷 [Leia em Português](README.pt.md)

This project is a real-time **aim alignment analyzer** for the FPS game **Valorant**. It uses a custom-trained [YOLOv8](https://github.com/ultralytics/ultralytics) object detection model to detect **enemy heads** in gameplay footage and evaluates whether your **crosshair is aligned**, **above**, or **below** the target's head.

🤖 Object Detection with YOLOv8
YOLO (You Only Look Once) is a real-time object detection architecture.
It predicts bounding boxes and class probabilities directly from images in one forward pass, making it extremely fast and suitable for gaming-related tasks.
The model was trained on custom-labeled Valorant gameplay frames using Roboflow, where the enemy head hitbox was annotated.

🧠 Inference Pipeline
Each frame of the video is passed to the YOLOv8 model.
The model returns the coordinates of detected enemy heads.
We extract the vertical center of the detected head and compare it to the crosshair position, which is assumed to be at the vertical midpoint of the screen.
Based on this comparison, the frame is classified as:
"aligned" if the crosshair is close enough (within a set pixel tolerance)
"above" if the crosshair is lower than the head
"below" if the crosshair is higher than the head

⚙️ Tools and Libraries
Ultralytics: For training and using YOLOv8 models.
OpenCV: For video processing and real-time frame analysis.
PyAutoGUI and keyboard: For mouse control and key detection.
Python: Core language powering all processing, integration, and logic.

````

## 🚀 Usage

1. **Install dependencies** (in a virtual environment):

```bash
pip install ultralytics opencv-python pyautogui keyboard
````

2. **Download or record** your Valorant gameplay as `valorant.mp4`

3. **Run the script**:

```bash
python src/analyze_aim.py
````

4. **Real-time screen analysis** (optional):

```bash
python src/aim_screen.py
````

While this script is running you can hold the **`X`** key to move the mouse cursor to the center of the detected head.

## 🎥 Some images of the training
![val_batch0_pred](https://github.com/user-attachments/assets/69ecf833-8e88-4447-9a85-b09c5d53f172)

## 🎥 Example Video Output

https://github.com/user-attachments/assets/56acffe3-87e1-4389-a1e7-df7a0293aeb3

## 📄 License

This project is licensed under **MIT**.
