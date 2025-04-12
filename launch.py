# launch.py — Starts tray icon and background notifier with logging

import subprocess
import os
import sys
import logging
from datetime import datetime

# Setup logging
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "launch.log")
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.info("=== Launch sequence started ===")

try:
    # Start daily_notifier.pyw as a background process
    notifier_path = os.path.join(BASE_DIR, "daily_notifier.pyw")
    subprocess.Popen(["pythonw", notifier_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info(f"Started daily_notifier.pyw from: {notifier_path}")
except Exception as e:
    logging.error(f"Failed to launch daily_notifier.pyw: {e}")

try:
    # Launch tray icon (blocking process)
    sys.path.insert(0, BASE_DIR)
    from ui import tray_launcher
    logging.info("Starting tray_launcher.run_tray()")
    tray_launcher.run_tray()
except Exception as e:
    logging.error(f"Error in tray_launcher: {e}")
