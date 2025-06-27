import csv
from collections import Counter
import matplotlib.pyplot as plt

def read_gesture_log(filepath="gesture_log.csv"):
    gestures = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    _, gesture = row
                    gestures.append(gesture)
    except FileNotFoundError:
        print("Log file not found.")
    return gestures

def plot_gesture_stats():
    gestures = read_gesture_log()
    if not gestures:
        print("No gestures to plot.")
        return

    counts = Counter(gestures)
    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='skyblue')
    plt.title("TRINETRA Gesture Frequency")
    plt.xlabel("Gesture")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_gesture_stats()
def draw_status(frame, gesture, brain_state, should_act):
    import cv2
    status_text = f"Gesture: {gesture} | Brain: {brain_state} | Action: {'✔️' if should_act else '❌'}"
    color = (0, 255, 0) if should_act else (150, 150, 150)
    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return frame
