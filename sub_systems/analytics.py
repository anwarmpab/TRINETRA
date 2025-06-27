# sub_systems/analytics.py

import csv
from datetime import datetime
import os

LOG_FILE = "logs/event_log.csv"

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


def log_event(event_type, description):
    """
    Logs an event with timestamp, event type, and a description.

    Args:
        event_type (str): Category of the event (e.g., 'gesture', 'eeg', 'system').
        description (str): What happened (e.g., 'Fist gesture triggered motor on').
    """
    timestamp = datetime.now().isoformat()

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, event_type, description])

    print(f"[LOG] {timestamp} | {event_type.upper()}: {description}")
