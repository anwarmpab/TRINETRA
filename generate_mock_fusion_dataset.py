import csv
import random
from datetime import datetime, timedelta

# Define possible gestures and brain states
gestures = ["Open Palm", "Fist", "Thumbs Up", "Victory"]
brain_states = ["active", "neutral", "drowsy"]

# Generate mock data
rows = []
current_time = datetime.now()

for _ in range(100):  # 100 mock entries
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    gesture = random.choice(gestures)
    brain_state = random.choice(brain_states)

    # Simple logic to decide action_triggered
    action_triggered = 1 if (gesture == "Thumbs Up" and brain_state == "active") else 0

    rows.append([timestamp, gesture, brain_state, action_triggered])
    current_time += timedelta(seconds=1)

# Write to CSV
with open("fusion_dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("✅ Mock fusion dataset generated with 100 rows.")
