# Enhanced Pomodoro with Task Awareness from storage/tasks.json

import os
import sys
import json
from datetime import datetime
from plyer import notification
import tkinter as tk

# Define the time-based schedule mapping
SCHEDULE_BLOCKS = [
    ("Flatbox", "14:20", "17:00"),
    ("Robocrops", "17:00", "18:30"),
    ("Ereditas", "18:30", "21:30"),
    ("Coding", "21:30", "23:00")
]

TASKS_JSON_PATH = os.path.join(os.path.dirname(__file__), "storage", "tasks.json")

def notify(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
    except Exception as e:
        print(f"Notification error: {e}")

def get_current_block():
    now = datetime.now().time()
    for project, start_str, end_str in SCHEDULE_BLOCKS:
        start = datetime.strptime(start_str, "%H:%M").time()
        end = datetime.strptime(end_str, "%H:%M").time()
        if start <= now <= end:
            return project
    return None

def get_task_for_project(project_name):
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(TASKS_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        project_tasks = data[today][project_name]["tasks"]
        status = data[today][project_name]["task_status"]

        for task in project_tasks:
            if not status.get(task, False):
                return task  # Return first incomplete task

        # All tasks done? Return first one as cycle
        return project_tasks[0] if project_tasks else "Break"

    except Exception as e:
        print(f"[!] Error reading tasks: {e}")
        return "Break"

def run_countdown_timer(minutes, title):
    window = tk.Tk()
    window.title("Pomodoro Timer")
    window.geometry("280x130")
    window.attributes("-topmost", True)

    title_label = tk.Label(window, text=title, font=("Helvetica", 12, "bold"))
    title_label.pack(pady=5)

    timer_label = tk.Label(window, text="", font=("Helvetica", 28))
    timer_label.pack(pady=10)

    def update_timer(count):
        mins = count // 60
        secs = count % 60
        timer_label.config(text=f"{mins:02}:{secs:02}")
        if count > 0:
            window.after(1000, update_timer, count - 1)
        else:
            window.destroy()

    update_timer(minutes * 60)
    window.mainloop()

def run_pomodoro_block():
    project = get_current_block()
    if project is None:
        notify("No Active Block", "This time is not part of any defined work block.")
        return

    task = get_task_for_project(project)
    notify(f"{project} - Pomodoro Started", f"Task: {task}")
    run_countdown_timer(25, f"{project}: {task}")
    notify(f"{project} - Pomodoro Complete", f"Finished: {task}")

if __name__ == "__main__":
    run_pomodoro_block()
