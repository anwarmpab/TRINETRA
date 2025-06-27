import cv2
import joblib
import pandas as pd

from gesture_module.gesture_detector import HandGestureRecognizer
from gesture_module.gesture_classifier import GestureClassifier
from gesture_module.jarvis_react import trigger_action
from gesture_module.logger import log_gesture
from eeg_simulation.eeg_reader import get_brain_state
from ai_models.fusion_logger import log_fusion
from gesture_module.gesture_visualizer import draw_status

# Load trained fusion model
fusion_model = joblib.load("ai_models/fusion_model.joblib")

# Initialize components
classifier = GestureClassifier()
detector = HandGestureRecognizer()
cap = cv2.VideoCapture(0)

# Setup display window
cv2.namedWindow("TRINETRA Vision Feed", cv2.WINDOW_NORMAL)
cv2.moveWindow("TRINETRA Vision Feed", 100, 100)

# Default values to avoid NameError
gesture_text = ""
gesture = ""
brain_state = ""
should_act = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame, landmarks = detector.detect_hands(frame)

    if landmarks:
        gesture = classifier.classify(landmarks)
        brain_state = get_brain_state()

        # Convert to numeric codes
        gesture_code = classifier.get_code(gesture)
        brain_code = {"active": 0, "neutral": 1, "drowsy": 2}.get(brain_state, 1)

        # Safe prediction using DataFrame with proper column names
        try:
            input_df = pd.DataFrame([[gesture_code, brain_code]], columns=["gesture_code", "brain_code"])
            should_act = fusion_model.predict(input_df)[0]
        except Exception as e:
            print(f"⚠️ Prediction error: {e}")
            should_act = False

        # Logging & reaction
        log_fusion(gesture, brain_state, should_act)
        import csv
        from datetime import datetime

        # Save to CSV log
        with open("interaction_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().isoformat(),
                gesture,
                brain_state,
                "Yes" if should_act else "No"
            ])

        if should_act:
            log_gesture(f"{gesture} [BRAIN: {brain_state}]")
            trigger_action(gesture)
            gesture_text = f"{gesture} (Brain: {brain_state}) ✅"
        else:
            gesture_text = f"{gesture} (Brain: {brain_state}) ❌"

    # Overlay gesture, brain state, and decision on frame
    frame = draw_status(frame, gesture, brain_state, should_act)
    cv2.imshow("TRINETRA Vision Feed", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print(f"Detected: {gesture}, should_act: {should_act}")
import time

last_gesture = None
last_trigger_time = time.time()
COOLDOWN_SECONDS = 3

# Inside your while loop after detecting gesture
if gesture != last_gesture or time.time() - last_trigger_time > COOLDOWN_SECONDS:
    trigger_action(gesture)
    last_gesture = gesture
    last_trigger_time = time.time()
else:
    print(f"⏳ Cooldown active for: {gesture}")
import requests
import datetime

def send_to_dashboard(gesture, action_status):
    payload = {
        "gesture": gesture,
        "timestamp": datetime.datetime.now().isoformat(),
        "action": action_status
    }
    try:
        requests.post("http://localhost:8000/log", json=payload)  # Replace with your deployed API URL
    except Exception as e:
        print(f"⚠️ Dashboard log failed: {e}")
