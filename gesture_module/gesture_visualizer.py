import cv2
import numpy as np

def draw_status(frame, gesture, brain_state, action_triggered):
    h, w, _ = frame.shape

    # Display gesture
    cv2.putText(frame, f"Gesture: {gesture}", (10, h - 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Display brain state
    cv2.putText(frame, f"Brain State: {brain_state}", (10, h - 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 100, 100), 2)

    # Display action status
    status = "Action Triggered!" if action_triggered else "Idle"
    color = (0, 255, 0) if action_triggered else (0, 0, 255)
    cv2.putText(frame, f"System: {status}", (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    return frame
