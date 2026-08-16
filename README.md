# Face Emotion Recognition using CNN Algorithm

A Windows desktop app, built as a thesis/capstone project, that acts as a "teacher
companion for online learning." It watches a selected browser window (Google Meet, Zoom in
a browser tab, etc.) during a class, detects student faces, and classifies their emotional
state in real time using a Convolutional Neural Network.

## How it works

1. `main.py` opens a Tkinter GUI where the teacher picks which open browser window to
   monitor (filtered to Chrome/Edge/Opera/Firefox/Brave windows with a video-call tab).
2. `windowcapture.py` grabs live screenshots of that window using the Win32 API.
3. Each frame is converted to grayscale and passed through OpenCV's Haar Cascade
   classifier (`haarcascade_frontalface_default.xml`) to detect faces.
4. Each detected face is cropped, resized to 48x48, and fed into a CNN trained to classify
   seven emotions: Angry, Disgusted, Fearful, Happy, Neutral, Sad, Surprised. The trained
   model architecture and weights ship with the repo as `emotion_model(75).json` and
   `emotion_model(75).h5`.
5. Bounding boxes and emotion labels are drawn directly on the captured frame so the
   teacher can see, at a glance, how the class is reacting.
6. If negative emotions (e.g. Fearful, Sad) cross a configurable threshold, the app can
   pop up a short vocabulary mini-game (word scramble with dictionary lookups via
   `PyDictionary`) as a re-engagement break for students.

## Stack

- **Python**, **Tkinter** for the desktop UI
- **OpenCV** for face detection and frame drawing
- **Keras/TensorFlow** for the CNN emotion classifier
- **pywin32** (`win32gui`, `win32ui`) for capturing another window's contents on Windows
- **PyAutoGUI** to enumerate open windows

## Running it

This project targets Windows (it depends on `pywin32` for window capture) with a Python
3.7-era environment (see the bundled `.pyc` for that interpreter version). Install the
dependencies (`opencv-python`, `keras`/`tensorflow`, `pywin32`, `pyautogui`, `PyDictionary`,
`numpy`), then run:

```bash
python main.py
```
