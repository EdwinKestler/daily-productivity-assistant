# daily_productivity_assistant/ui/gui_review.py

import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "storage")
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")

PROJECTS = ["Flatbox", "Robocrops", "Ereditas", "Coding"]

# Load existing task data
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as f:
        return json.load(f)

# Save task data
def save_tasks(data):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)

# GUI for completion review
def launch_review_gui():
    today = datetime.today().strftime('%Y-%m-%d')
    data = load_tasks()

    if today not in data:
        messagebox.showerror("No Data", "No tasks found for today.")
        return

    root = tk.Tk()
    root.title("Completion Review")
    root.geometry("700x900")

    entries = {}

    def submit():
        for project, widgets in entries.items():
            completed_tasks = []
            for i, var in enumerate(widgets['task_vars']):
                if var.get():
                    completed_tasks.append(i)

            if project in data[today]:
                task_list = data[today][project].get("tasks", [])
                all_completed = True

                for i, task in enumerate(task_list):
                    status = (i in completed_tasks)
                    data[today][project].setdefault("task_status", {})[task] = status
                    if not status:
                        all_completed = False

                data[today][project]["completed"] = all_completed
                data[today][project]["note"] = widgets['note'].get()

        save_tasks(data)
        messagebox.showinfo("Success", "Task completion status updated.")
        root.destroy()

    for project in PROJECTS:
        if project not in data[today]:
            continue

        frame = tk.LabelFrame(root, text=project, padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill="both")

        tk.Label(frame, text=f"Goal: {data[today][project].get('goal', '')}", wraplength=600, anchor='w', justify='left').pack(anchor='w')
        tk.Label(frame, text=f"Objective: {data[today][project].get('objective', '')}", wraplength=600, anchor='w', justify='left').pack(anchor='w')

        task_vars = []
        for task in data[today][project].get("tasks", []):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(frame, text=task, variable=var, wraplength=600, anchor='w', justify='left')
            cb.pack(anchor='w')
            task_vars.append(var)

        tk.Label(frame, text="Notes / Blockers:").pack(anchor='w')
        note_var = tk.StringVar()
        tk.Entry(frame, textvariable=note_var, width=80).pack(pady=2)

        entries[project] = {
            'task_vars': task_vars,
            'note': note_var
        }

    tk.Button(root, text="Submit Review", command=submit, bg="blue", fg="white").pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    launch_review_gui()
