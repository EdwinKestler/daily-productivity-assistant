# daily_productivity_assistant/ui/gui_launcher.py

import tkinter as tk
import subprocess
import sys
import os
from report import generate_weekly_report
from ui.charts import show_weekly_chart
from pomodoro import run_pomodoro_block

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define proper subprocess calls to ensure tasks.json updates
PLANNER_PATH = os.path.join(BASE_DIR, "gui_planner.py")
REVIEW_PATH = os.path.join(BASE_DIR, "gui_review.py")


def run_planner():
    subprocess.run([sys.executable, PLANNER_PATH])


def run_review():
    subprocess.run([sys.executable, REVIEW_PATH])


def launch_gui_launcher():
    root = tk.Tk()
    root.title("🧠 Productivity Assistant Launcher")
    root.geometry("320x350")

    tk.Label(root, text="Welcome! Choose an action:", font=("Helvetica", 12, "bold")).pack(pady=10)

    tk.Button(root, text="📝 Daily Planner", command=run_planner, width=30).pack(pady=5)
    tk.Button(root, text="✅ Task Review", command=run_review, width=30).pack(pady=5)
    tk.Button(root, text="⏱️ Start Pomodoro (Flatbox)", command=lambda: run_pomodoro_block("Flatbox"), width=30).pack(pady=5)
    tk.Button(root, text="📊 Show Weekly Chart", command=show_weekly_chart, width=30).pack(pady=5)
    tk.Button(root, text="📋 Weekly Report", command=generate_weekly_report, width=30).pack(pady=5)
    tk.Button(root, text="❌ Exit", command=root.destroy, bg="red", fg="white", width=30).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    launch_gui_launcher()
