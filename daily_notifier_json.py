# daily_notifier.py — Sends start/end notifications based on schedule_data.json

import time
import json
import os
from datetime import datetime
from ui.notifications import show_notification

# Path to schedule data JSON
SCHEDULE_JSON_PATH = os.path.join(os.path.dirname(__file__), "storage", "schedule_data.json")

# Load schedule from JSON
def load_schedule():
    try:
        with open(SCHEDULE_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Failed to load schedule data: {e}")
        return []

notified_start = set()
notified_end = set()

def check_schedule(schedule_data):
    now = datetime.now().strftime("%H:%M")
    for activity, start, end, priority, note in schedule_data:
        if now == start and activity not in notified_start:
            show_notification(f"🟢 Start: {activity}", f"{priority} — {note}")
            notified_start.add(activity)
        elif now == end and activity not in notified_end:
            show_notification(f"🔴 End: {activity}", f"{priority} — {note}")
            notified_end.add(activity)

if __name__ == "__main__":
    schedule_data = load_schedule()
    while True:
        check_schedule(schedule_data)
        time.sleep(60)  # Check every minute
