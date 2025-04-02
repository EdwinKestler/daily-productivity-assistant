# daily_productivity_assistant/ui/notifications.py

from plyer import notification

def show_notification(title: str, message: str, duration: int = 10):
    """Cross-platform desktop notification using plyer."""
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=duration  # duration in seconds
        )
        print(f"[🔔 Notification] {title}: {message}")
    except Exception as e:
        print(f"[!] Notification Error: {e}")
