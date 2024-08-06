import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
from collections import deque

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

# OpenCV: Capture video from the webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Gesture variables
gesture_history = deque(maxlen=5)  # For smoothing gestures
position_history = deque(maxlen=5)  # To store recent positions for smoothing

# Touch state variables
is_touching = False


def distance(point1, point2):
    return np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def detect_gesture(hand_landmarks):
    # Extract coordinates for specific landmarks
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]

    # Define distance threshold for fingers to be considered touching
    threshold = 0.05

    # Detect gestures based on distances
    if distance(thumb_tip, ring_tip) < threshold:
        return "single_click"
    elif distance(thumb_tip, index_tip) < threshold:
        return "double_click"
    elif distance(thumb_tip, middle_tip) < threshold:
        return "right_click"
    else:
        return "unknown"


def smooth_coordinates(new_x, new_y, position_history):
    # Add the new position to the history
    position_history.append((new_x, new_y))
    # Calculate the average of the stored positions
    avg_x = np.mean([pos[0] for pos in position_history])
    avg_y = np.mean([pos[1] for pos in position_history])
    return avg_x, avg_y


def control_mouse(gesture, x, y):
    global is_touching

    # Smooth the gesture by taking the most common in recent history
    gesture_history.append(gesture)
    smoothed_gesture = max(set(gesture_history), key=gesture_history.count)

    # Map hand position to screen coordinates with smoothing
    screen_x, screen_y = smooth_coordinates(
        np.interp(x, [0, 640], [0, screen_width]),
        np.interp(y, [0, 480], [0, screen_height]),
        position_history
    )

    pyautogui.moveTo(screen_x, screen_y)

    # Click actions
    if smoothed_gesture == "single_click":
        if not is_touching:
            pyautogui.click()
            is_touching = True
    elif smoothed_gesture == "double_click":
        if not is_touching:
            pyautogui.doubleClick()
            is_touching = True
    elif smoothed_gesture == "right_click":
        if not is_touching:
            pyautogui.rightClick()
            is_touching = True
    else:
        is_touching = False


# Main loop for gesture detection and mouse control
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks)
            x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]
            y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0]
            control_mouse(gesture, x, y)

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
