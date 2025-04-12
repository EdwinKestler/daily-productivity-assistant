# daily_productivity_assistant/planner.py

import json
import os
from datetime import datetime

DATA_DIR = "storage"
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")

PROJECTS = ["Flatbox", "Robocrops", "Ereditas", "Coding"]


def ensure_storage():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            json.dump({}, f)


def load_tasks():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)


def save_tasks(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)


def daily_planner_prompt():
    ensure_storage()
    data = load_tasks()
    today = datetime.today().strftime('%Y-%m-%d')

    if today not in data:
        data[today] = {}

    print("\n--- Daily Planning Session ---")
    for project in PROJECTS:
        print(f"\nProject: {project}")
        task = input(f"  → Task for {project}: ")
        goal = input(f"  → Goal for {project}: ")
        objective = input(f"  → Measurable Objective for {project}: ")

        data[today][project] = {
            "task": task,
            "goal": goal,
            "objective": objective,
            "completed": False
        }

    save_tasks(data)
    print("\n[✓] Daily tasks saved.")
