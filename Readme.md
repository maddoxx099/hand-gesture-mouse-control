# Hand Gesture Mouse Control

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-blue.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.7-orange.svg)](https://mediapipe.dev/)

This project enables you to control your computer's mouse using hand gestures detected via a webcam. The program uses OpenCV for video capture and MediaPipe for hand detection, allowing you to perform various mouse actions like left-click, double-click, and right-click using specific gestures.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Hand Gestures](#hand-gestures)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Single Left Click:** Touch between thumb and ring finger.
- **Double Left Click:** Touch between thumb and index finger.
- **Right Click:** Touch between thumb and middle finger.
- **Smooth Mouse Movement:** Hand position is mapped to screen coordinates with smoothing for accurate control.
- **Real-Time Detection:** Real-time hand gesture detection and action mapping.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Webcam (built-in or external)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/hand-gesture-mouse-control.git
   cd hand-gesture-mouse-control

2. **Create and Activate a Virtual Environment**

    ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

### Usage

1. **Run the Program**
 
   ```bash
   python gesture_control.py

2. **Using Hand Gestures**

   - Position your hand in front of the webcam.
   - Use the specified hand gestures to control the mouse.

## Hand Gestures

- Single Left Click: Touch between thumb and ring finger.
- Double Left Click: Touch between thumb and index finger.
- Right Click: Touch between thumb and middle finger.

## Customization

- Adjusting Sensitivity: You can modify the distance threshold in the detect_gesture function to adjust gesture sensitivity.
- Adding New Gestures: To add new gestures, define new conditions in the detect_gesture function and map them to actions in the control_mouse function.

## Troubleshooting

- No Camera Detected: Ensure your webcam is properly connected and recognized by your system.
- Inaccurate Detection: Try adjusting the lighting and background. The program works best in a well-lit environment.