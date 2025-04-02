# daily_productivity_assistant/ui/charts.py

import os
import json
import matplotlib.pyplot as plt
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


def show_weekly_chart():
    data = load_tasks()
    today = datetime.today()
    start_week = today - timedelta(days=today.weekday())  # Monday

    summary = defaultdict(lambda: {"total": 0, "completed": 0})

    for i in range(7):
        date = (start_week + timedelta(days=i)).strftime('%Y-%m-%d')
        if date in data:
            for project, details in data[date].items():
                summary[project]["total"] += 1
                if details.get("completed"):
                    summary[project]["completed"] += 1

    projects = PROJECTS
    completed = [summary[p]["completed"] for p in projects]
    total = [summary[p]["total"] for p in projects]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(projects, total, label='Total Tasks', alpha=0.5)
    ax.bar(projects, completed, label='Completed Tasks', alpha=0.8)

    ax.set_ylabel('Task Count')
    ax.set_title('Weekly Task Completion by Project')
    ax.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
