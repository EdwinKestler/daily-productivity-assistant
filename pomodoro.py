# daily_productivity_assistant/pomodoro.py

import time
import threading
from plyer import notification
import tkinter as tk


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # seconds
    )


def run_countdown_timer(minutes, title):
    window = tk.Tk()
    window.title("Pomodoro Timer")
    window.geometry("200x120")
    window.attributes("-topmost", True)

    title_label = tk.Label(window, text=title, font=("Helvetica", 12, "bold"))
    title_label.pack(pady=5)

    timer_label = tk.Label(window, text="", font=("Helvetica", 24))
    timer_label.pack(pady=5)

    def update_timer(count):
        minutes = count // 60
        seconds = count % 60
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        if count > 0:
            window.after(1000, update_timer, count - 1)
        else:
            window.destroy()

    update_timer(minutes * 60)
    window.mainloop()


def run_pomodoro_block(project_name):
    print(f"\n[Pomodoro] Starting 25-minute session for {project_name}...")
    notify(f"{project_name} Work Block", "Start your 25-minute focus session!")

    # Start timer GUI in a thread
    threading.Thread(target=run_countdown_timer, args=(25, f"Work: {project_name}"), daemon=True).start()
    time.sleep(25 * 60)  # 25 minutes work session

    print(f"\n[Pomodoro] 25-minute session complete for {project_name}.")
    notify(f"{project_name} Review Block", "Time for 5-minute review or research.")

    threading.Thread(target=run_countdown_timer, args=(5, "Break"), daemon=True).start()
    time.sleep(5 * 60)  # 5 minutes break

    print(f"[Pomodoro] Break complete. Ready for next block or task.")
    notify("Pomodoro Complete", f"{project_name} block finished. Ready for next?")
