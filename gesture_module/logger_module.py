import csv
from datetime import datetime

LOG_FILE = "gesture_log.csv"

def log_gesture(gesture_label):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), gesture_label])
