# daily_productivity_assistant/main.py

import time
from planner import daily_planner_prompt
from pomodoro import run_pomodoro_block
from review import check_task_completion
from report import generate_weekly_report
import schedule
import datetime

# Daily startup routine at 08:20
def start_daily_routine():
    print("[+] Starting Daily Planning Prompt (08:20–08:30)")
    daily_planner_prompt()

# Scheduled checks for each major work block (manually aligned for now)
def setup_schedule():
    schedule.every().day.at("08:20").do(start_daily_routine)

    schedule.every().day.at("14:20").do(lambda: run_pomodoro_block("Flatbox"))
    schedule.every().day.at("17:00").do(lambda: run_pomodoro_block("Robocrops"))
    schedule.every().day.at("18:30").do(lambda: run_pomodoro_block("Ereditas"))
    schedule.every().day.at("21:30").do(lambda: run_pomodoro_block("Coding"))

    # End of each block -> check task completion
    schedule.every().day.at("17:00").do(lambda: check_task_completion("Flatbox"))
    schedule.every().day.at("18:30").do(lambda: check_task_completion("Robocrops"))
    schedule.every().day.at("21:30").do(lambda: check_task_completion("Ereditas"))
    schedule.every().day.at("23:00").do(lambda: check_task_completion("Coding"))

    # Weekly Review on Sunday 18:00
    schedule.every().sunday.at("18:00").do(generate_weekly_report)

# Main event loop
def run():
    print("[+] Productivity Assistant Started...")
    setup_schedule()
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    run()
