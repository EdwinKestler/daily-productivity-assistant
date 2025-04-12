# ui/notifications.py — With sound and 30s duration using winsound

from plyer import notification
import platform

def play_sound():
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 500)  # Frequency 1000Hz, Duration 500ms
        except Exception as e:
            print(f"[!] Sound Error: {e}")

def show_notification(title: str, message: str, duration: int = 30):
    """Cross-platform desktop notification with sound"""
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=duration  # seconds
        )
        play_sound()
        print(f"[🔔 Notification] {title}: {message}")
    except Exception as e:
        print(f"[!] Notification Error: {e}")
