# 📐 Architecture Overview

## 🧠 Daily Productivity Assistant - High-Level Design

```text
                         ┌────────────────────────┐
                         │   Daily Planning (08:20)│
                         └────────────┬───────────┘
                                      │
      ┌───────────────────────────────┼────────────────────────────────┐
      ▼                               ▼                                ▼
┌──────────────┐              ┌──────────────┐                ┌──────────────┐
│  Flatbox     │              │  Robocrops   │                │  Ereditas    │
└─────┬────────┘              └─────┬────────┘                └─────┬────────┘
      │                             │                                 │
      ▼                             ▼                                 ▼
┌────────────┐             ┌────────────┐                   ┌────────────┐
│ Pomodoro   │             │ Pomodoro   │                   │ Pomodoro   │
│ (25 + 5)   │             │ (25 + 5)   │                   │ (25 + 5)   │
└─────┬──────┘             └─────┬──────┘                   └─────┬──────┘
      │ Completion Check         │ Completion Check               │ Completion Check
      ▼                          ▼                                ▼
┌────────────┐           ┌────────────┐                   ┌────────────┐
│ Task Log   │◄──────────┼────────────┼───────────────────┼────────────┘
└────┬───────┘                                           
     ▼
┌────────────┐
│ Weekly     │
│ Report     │
│ (Sunday)   │
└────┬───────┘
     ▼
┌────────────┐
│ Charts.py  │⟶ [matplotlib]
└────────────┘
```

---

## 📦 Core Components

| Module            | Description                                 |
|------------------|---------------------------------------------|
| `main.py`         | Scheduler for daily and weekly routines     |
| `planner.py`      | Input prompts for task/goals/objectives     |
| `pomodoro.py`     | Work timer with review window + notifications|
| `review.py`       | End-of-block verification prompts           |
| `report.py`       | Aggregates weekly performance               |
| `charts.py`       | Visualizes progress with matplotlib         |
| `notifications.py`| Cross-platform desktop alerts               |
| `time_utils.py`   | Time parsing, validation, window tracking   |

---

## 🔁 Daily Flow
1. 08:20 – You input plans for the day per project
2. Timers begin at predefined work blocks
3. Notifications signal when to start/stop
4. Completion prompts log what was done
5. Weekly review shows stats and visuals

---

## 🧰 Tech Stack
- Python 3.8+
- `schedule` for timing
- `plyer` for toast notifications
- `matplotlib` for charts
- Standard JSON for persistent logs

---

For extended documentation, custom configs, and templates, create additional docs:
```
docs/
├── architecture_diagram.md
├── faq.md
├── customization_guide.md
└── usage_scenarios.md
