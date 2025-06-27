import cv2
import mediapipe as mp

class HandGestureRecognizer:
    def __init__(self, mode=False, max_hands=2):
        self.mode = mode
        self.max_hands = max_hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, max_hands)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                lm_list = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                landmarks.append(lm_list)

        return frame, landmarks
