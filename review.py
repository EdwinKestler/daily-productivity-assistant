# daily_productivity_assistant/review.py

import json
import os
from datetime import datetime

DATA_DIR = "storage"
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as f:
        return json.load(f)


def save_tasks(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)


def check_task_completion(project_name):
    today = datetime.today().strftime('%Y-%m-%d')
    data = load_tasks()

    if today not in data or project_name not in data[today]:
        print(f"[!] No task found for {project_name} today.")
        return

    print(f"\n--- Completion Check for {project_name} ---")
    completed = input("  → Was the task completed? (y/n): ").strip().lower() == 'y'
    note = input("  → Any notes or blockers?: ").strip()

    data[today][project_name]["completed"] = completed
    data[today][project_name]["note"] = note

    save_tasks(data)
    print(f"[✓] Task status for {project_name} updated.")
