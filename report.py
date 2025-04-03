# daily_productivity_assistant/report.py

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage")
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

    summary = defaultdict(lambda: {
        "total_tasks": 0,
        "completed_tasks": 0,
        "objectives": set(),
        "completed_blocks": 0,
        "total_blocks": 0
    })

    for i in range(7):
        date = (start_week + timedelta(days=i)).strftime('%Y-%m-%d')
        if date in data:
            for project, details in data[date].items():
                summary[project]["total_blocks"] += 1
                if details.get("completed"):
                    summary[project]["completed_blocks"] += 1

                for task in details.get("tasks", []):
                    summary[project]["total_tasks"] += 1
                    if details.get("task_status", {}).get(task):
                        summary[project]["completed_tasks"] += 1

                obj = details.get("objective")
                if obj:
                    summary[project]["objectives"].add(obj)

    for project in PROJECTS:
        print(f"\nProject: {project}")
        print(f"  → Tasks Completed: {summary[project]['completed_tasks']} / {summary[project]['total_tasks']}")
        print(f"  → Blocks Completed: {summary[project]['completed_blocks']} / {summary[project]['total_blocks']}")
        if summary[project]['objectives']:
            print("  → Objectives Reviewed:")
            for obj in summary[project]['objectives']:
                print(f"     - {obj}")

    print("\n[✓] Weekly report generated.")


if __name__ == "__main__":
    generate_weekly_report()
