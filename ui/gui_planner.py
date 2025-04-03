# daily_productivity_assistant/ui/gui_planner.py

import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

# File path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "storage")
FILE_PATH = os.path.join(DATA_DIR, "tasks.json")

# Constants
PROJECTS = {
    "Flatbox": 6,
    "Robocrops": 3,
    "Ereditas": 6,
    "Coding": 3
}

# Ensure storage exists
def ensure_storage():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            json.dump({}, f)

# Save task data
def save_tasks(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)

# GUI planner logic
def launch_planner_gui():
    ensure_storage()
    today = datetime.today().strftime('%Y-%m-%d')

    with open(FILE_PATH, 'r') as f:
        data = json.load(f)

    if today not in data:
        data[today] = {}

    root = tk.Tk()
    root.title("Daily Task Planner")
    root.geometry("800x1000")
    entries = {}

    def submit():
        for project, widgets in entries.items():
            task_entries = widgets['tasks']
            tasks = [t.get().strip() for t in task_entries if t.get().strip()]

            if len(tasks) > PROJECTS[project]:
                messagebox.showerror("Task Limit Exceeded", f"{project} allows max {PROJECTS[project]} tasks.")
                return

            goal = widgets['goal'].get().strip()
            objective = widgets['objective'].get().strip()

            data[today][project] = {
                "goal": goal,
                "objective": objective,
                "tasks": tasks,
                "completed": False
            }

        save_tasks(data)
        messagebox.showinfo("Success", "Tasks saved successfully!")
        root.destroy()

    for project, max_tasks in PROJECTS.items():
        frame = tk.LabelFrame(root, text=f"{project} (max {max_tasks} tasks)", padx=10, pady=10)
        frame.pack(padx=10, pady=10, fill="x")

        tk.Label(frame, text="Goal:").pack(anchor='w')
        goal_var = tk.StringVar()
        tk.Entry(frame, textvariable=goal_var, width=100).pack(pady=2)

        tk.Label(frame, text="Objective:").pack(anchor='w')
        objective_var = tk.StringVar()
        tk.Entry(frame, textvariable=objective_var, width=100).pack(pady=2)

        task_frame = tk.Frame(frame)
        task_frame.pack(fill="x")

        task_vars = []

        def make_task_adder(task_list, container, project_key):
            def add():
                if len(task_list) >= PROJECTS[project_key]:
                    messagebox.showwarning("Limit Reached", f"You can only add up to {PROJECTS[project_key]} tasks for {project_key}.")
                    return
                var = tk.StringVar()
                entry = tk.Entry(container, textvariable=var, width=100)
                entry.pack(pady=2)
                task_list.append(var)
            return add

        entries[project] = {
            'goal': goal_var,
            'objective': objective_var,
            'tasks': task_vars
        }

        add_task_fn = make_task_adder(task_vars, task_frame, project)
        tk.Button(frame, text="+ Task", command=add_task_fn).pack(pady=5)

        # Start with one task input
        add_task_fn()

    tk.Button(root, text="Submit Tasks", command=submit, bg="green", fg="white").pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    launch_planner_gui()
