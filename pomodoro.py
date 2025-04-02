# daily_productivity_assistant/pomodoro.py

import time
from plyer import notification


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # seconds
    )


def run_pomodoro_block(project_name):
    print(f"\n[Pomodoro] Starting 25-minute session for {project_name}...")
    notify(f"{project_name} Work Block", "Start your 25-minute focus session!")
    time.sleep(25 * 60)  # 25 minutes

    print(f"\n[Pomodoro] 25-minute session complete for {project_name}.")
    notify(f"{project_name} Review Block", "Time for 5-minute review or research.")
    time.sleep(5 * 60)  # 5 minutes

    print(f"[Pomodoro] Break complete. Ready for next block or task.")
    notify("Pomodoro Complete", f"{project_name} block finished. Ready for next?")
