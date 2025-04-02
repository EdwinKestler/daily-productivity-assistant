# daily_productivity_assistant/report.py

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

DATA_DIR = "storage"
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")
PROJECTS = ["Flatbox", "Robocrops", "Ereditas", "Coding"]


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as f:
        return json.load(f)


def generate_weekly_report():
    print("\n===== Weekly Performance Report =====")
    data = load_tasks()
    today = datetime.today()
    start_week = today - timedelta(days=today.weekday())  # Monday

    summary = defaultdict(lambda: {"total": 0, "completed": 0, "objectives": []})

    for i in range(7):
        date = (start_week + timedelta(days=i)).strftime('%Y-%m-%d')
        if date in data:
            for project, details in data[date].items():
                summary[project]["total"] += 1
                if details.get("completed"):
                    summary[project]["completed"] += 1
                summary[project]["objectives"].append(details.get("objective", ""))

    for project in PROJECTS:
        print(f"\nProject: {project}")
        print(f"  → Tasks Completed: {summary[project]['completed']} / {summary[project]['total']}")
        if summary[project]['objectives']:
            print("  → Objectives Reviewed:")
            for obj in summary[project]['objectives']:
                print(f"     - {obj}")

    print("\n[✓] Weekly report generated.")
