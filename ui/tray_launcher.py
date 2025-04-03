# daily_productivity_assistant/ui/tray_launcher.py

import os
import sys
import subprocess
from pystray import Icon, MenuItem as Item, Menu
from PIL import Image, ImageDraw
from threading import Thread

# Base path resolution for subprocess context
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLANNER_PATH = os.path.join(BASE_DIR, "gui_planner.py")
REVIEW_PATH = os.path.join(BASE_DIR, "gui_review.py")
CHART_PATH = os.path.join(BASE_DIR, "charts.py")
REPORT_PATH = os.path.join(BASE_DIR, "..", "report.py")
POMODORO_PATH = os.path.join(BASE_DIR, "..", "pomodoro.py")

# Subprocess-safe launches

def run_planner():
    subprocess.run([sys.executable, PLANNER_PATH])

def run_review():
    subprocess.run([sys.executable, REVIEW_PATH])

def show_chart():
    subprocess.run([sys.executable, CHART_PATH])

def show_report():
    subprocess.run([sys.executable, REPORT_PATH])

def start_pomodoro():
    subprocess.run([sys.executable, POMODORO_PATH, "Flatbox"])

# Icon generator

def create_icon_image():
    image = Image.new('RGB', (64, 64), color=(30, 144, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill="white")
    draw.text((24, 22), "✓", fill="blue")
    return image

# Tray logic

def run_tray():
    icon = Icon("ProductivityAssistant")
    icon.icon = create_icon_image()
    icon.title = "Productivity Assistant"
    icon.menu = Menu(
        Item("📝 Planner", lambda: Thread(target=run_planner).start()),
        Item("✅ Review", lambda: Thread(target=run_review).start()),
        Item("⏱️ Pomodoro", lambda: Thread(target=start_pomodoro).start()),
        Item("📊 Weekly Chart", lambda: Thread(target=show_chart).start()),
        Item("📋 Weekly Report", lambda: Thread(target=show_report).start()),
        Item("❌ Exit", lambda icon, item: icon.stop())
    )
    icon.run()

if __name__ == "__main__":
    run_tray()
