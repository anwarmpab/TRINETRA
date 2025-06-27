# gesture_module/gesture_classifier.py

class GestureClassifier:
    def classify(self, landmarks):
        if not landmarks:
            return "No Hand"

        lm = landmarks[0]  # First detected hand
        fingers = []

        # Thumb (assume right hand for now)
        if lm[4][0] > lm[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 fingers: index to pinky
        for tip in [8, 12, 16, 20]:
            if lm[tip][1] < lm[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Gesture patterns
        if fingers == [0, 1, 1, 0, 0]:
            return "Victory"
        elif fingers == [1, 1, 1, 1, 1]:
            return "Open Palm"
        elif fingers == [0, 0, 0, 0, 0]:
            return "Fist"
        elif fingers == [1, 0, 0, 0, 0]:
            return "Thumbs Up"
        elif fingers == [0, 1, 0, 0, 1]:
            return "Peace"
        elif fingers == [1, 1, 0, 0, 1]:
            return "Okay"
        else:
            return "Unknown"

    def get_code(self, gesture_name):
        gesture_map = {
            "Fist": 0,
            "Thumbs Up": 1,
            "Victory": 2,
            "Open Palm": 3,
            "Peace": 4,
            "Okay": 5,
            "Unknown": 6
        }
        return gesture_map.get(gesture_name, 6)
# Example expected gestures
recognized_gestures = ["Fist", "Thumbs Up", "Peace", "Open Palm"]
