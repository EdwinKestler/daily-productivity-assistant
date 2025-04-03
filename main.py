# daily_productivity_assistant/main.py

import time
from ui.gui_planner import launch_planner_gui
from ui.gui_review import launch_review_gui
from pomodoro import run_pomodoro_block
from report import generate_weekly_report
import schedule
import datetime

# Daily startup routine at 08:20
def start_daily_routine():
    print("[+] Launching GUI Planner for Daily Planning (08:20–08:30)")
    launch_planner_gui()

# Scheduled checks for each major work block (manually aligned for now)
def setup_schedule():
    schedule.every().day.at("08:20").do(start_daily_routine)

    schedule.every().day.at("14:20").do(lambda: run_pomodoro_block("Flatbox"))
    schedule.every().day.at("17:00").do(lambda: run_pomodoro_block("Robocrops"))
    schedule.every().day.at("18:30").do(lambda: run_pomodoro_block("Ereditas"))
    schedule.every().day.at("21:30").do(lambda: run_pomodoro_block("Coding"))

    # End of each block -> check task completion via GUI
    schedule.every().day.at("17:00").do(lambda: launch_review_gui())
    schedule.every().day.at("18:30").do(lambda: launch_review_gui())
    schedule.every().day.at("21:30").do(lambda: launch_review_gui())
    schedule.every().day.at("23:00").do(lambda: launch_review_gui())

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
