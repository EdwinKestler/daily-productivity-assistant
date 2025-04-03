# 🔧 Customization Guide for Daily Productivity Assistant

This guide explains how to configure:
- 📅 Project schedules (Pomodoro work blocks)
- 📋 Tracked projects
- ⏲️ Work/Break durations
- 📁 Storage format

---

## 🕒 1. Customize Scheduled Work Blocks

Edit the `main.py` file to change start times:
```python
schedule.every().day.at("14:20").do(lambda: run_pomodoro_block("Flatbox"))
schedule.every().day.at("17:00").do(lambda: run_pomodoro_block("Robocrops"))
schedule.every().day.at("18:30").do(lambda: run_pomodoro_block("Ereditas"))
schedule.every().day.at("21:30").do(lambda: run_pomodoro_block("Coding"))
```
✅ **Tip:** Use 24-hour `HH:MM` format and check with `time_utils.py` helpers.


---

## 📂 2. Add or Remove Projects

In `planner.py`, modify the list of tracked projects:
```python
PROJECTS = ["Flatbox", "Robocrops", "Ereditas", "Coding"]
```
You must also:
- Add Pomodoro scheduling blocks in `main.py`
- Add reporting hooks in `report.py`

✅ **Tip:** Keep project names consistent across files.

---

## ⏱️ 3. Change Pomodoro Durations

Modify `pomodoro.py`:
```python
# Original
time.sleep(25 * 60)  # Work time
...
time.sleep(5 * 60)   # Review/Break
```
Replace `25` or `5` with any custom minute value.

✅ **Example:** For 50/10 sessions:
```python
time.sleep(50 * 60)  # Deep work
...
time.sleep(10 * 60)  # Extended reflection
```

---

## 🧠 4. Extend Planner Prompts

You can prompt for:
- Priority (Low/Medium/High)
- Estimated effort (in Pomodoros)

Edit `planner.py`:
```python
priority = input("  → Priority (L/M/H): ")
data[today][project] = {
    "task": task,
    "goal": goal,
    "objective": objective,
    "priority": priority,
    "completed": False
}
```
✅ **Optional:** Use enums or validation logic in `utils/`.

---

## 📁 5. Customize Storage

Default format is JSON at:
```
storage/tasks.json
```
You can:
- Use SQLite with `sqlite3` for structured querying
- Export weekly logs to CSV/Markdown
- Backup to cloud drive

✅ Tip: Use `report.py` as base to write custom export scripts.

---

## 💬 Need More?
- Trigger from mobile? → Add a Telegram Bot
- View data visually? → Integrate with Notion/Google Sheets
- GUI? → Use PyQt or Tkinter in future versions

Let us know what you'd like to see!
