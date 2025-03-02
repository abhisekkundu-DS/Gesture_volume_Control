# Hand Gesture Voice Control Project

This project allows users to control a computer or application via hand gestures, integrated with voice control, using Python. The system utilizes computer vision techniques to recognize hand gestures and voice commands to control various actions on your device. It uses OpenCV for hand gesture detection and a speech recognition library for voice commands.

## Features
- **Hand Gesture Recognition**: The program uses a webcam to capture hand gestures and recognize specific gestures for controlling actions.
- **Voice Control Integration**: You can give voice commands to control functions, such as playing media, opening apps, and controlling volume.
- **Real-Time Processing**: Hand gesture and voice command processing happens in real-time for smooth interaction.

## Requirements

Before running this project, you'll need to install the following Python libraries:

- `opencv-python`: For real-time computer vision to detect and process hand gestures.
- `mediapipe`: For hand gesture recognition and tracking.
- `SpeechRecognition`: To process voice commands.
- `pyttsx3`: To convert text to speech for providing feedback.
- `pyaudio`: Required for capturing audio from the microphone for voice recognition.

Install the required libraries with:

```bash
pip install opencv-python mediapipe SpeechRecognition pyttsx3 pyaudio
