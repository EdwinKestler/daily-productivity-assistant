# daily_productivity_assistant/utils/time_utils.py

from datetime import datetime, timedelta

def str_to_time(time_str):
    """Convert 'HH:MM' string to datetime.time object."""
    return datetime.strptime(time_str, '%H:%M').time()

def str_to_datetime_today(time_str):
    """Return a datetime object for today's date with provided 'HH:MM' time."""
    today = datetime.today()
    parsed_time = str_to_time(time_str)
    return datetime.combine(today.date(), parsed_time)

def time_block_duration(start_str, end_str):
    """Return timedelta between two 'HH:MM' formatted strings."""
    start_dt = str_to_datetime_today(start_str)
    end_dt = str_to_datetime_today(end_str)
    return end_dt - start_dt

def is_now_within_range(start_str, end_str):
    """Check if the current time is within a given time range today."""
    now = datetime.now()
    return str_to_datetime_today(start_str) <= now <= str_to_datetime_today(end_str)
