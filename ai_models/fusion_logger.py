import csv
from datetime import datetime

LOG_FILE = "fusion_dataset.csv"

def log_fusion(gesture, brain_state, is_action_triggered):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            gesture,
            brain_state,
            int(is_action_triggered)
        ])
