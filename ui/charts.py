# daily_productivity_assistant/ui/charts.py

import os
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "storage")
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")
PROJECTS = ["Flatbox", "Robocrops", "Ereditas", "Coding"]


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as f:
        return json.load(f)


def show_weekly_chart():
    data = load_tasks()
    today = datetime.today()
    start_week = today - timedelta(days=today.weekday())  # Monday

    summary = defaultdict(lambda: {"total_tasks": 0, "completed_tasks": 0, "total_blocks": 0, "completed_blocks": 0})

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

    projects = PROJECTS
    completed_tasks = [summary[p]["completed_tasks"] for p in projects]
    total_tasks = [summary[p]["total_tasks"] for p in projects]
    completed_blocks = [summary[p]["completed_blocks"] for p in projects]
    total_blocks = [summary[p]["total_blocks"] for p in projects]

    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axs[0].bar(projects, total_tasks, label='Total Tasks', alpha=0.4)
    axs[0].bar(projects, completed_tasks, label='Completed Tasks', alpha=0.9)
    axs[0].set_ylabel('Tasks')
    axs[0].set_title('Task Completion')
    axs[0].legend()
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)

    axs[1].bar(projects, total_blocks, label='Total Blocks', alpha=0.4)
    axs[1].bar(projects, completed_blocks, label='Completed Blocks', alpha=0.9)
    axs[1].set_ylabel('Blocks')
    axs[1].set_title('Block Completion')
    axs[1].legend()
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)

    plt.suptitle('Weekly Completion Summary by Project')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    show_weekly_chart()
