import requests
from datetime import datetime, timedelta, timezone  
from task06 import next_days_events

def attendance_report(token: str, n: int) -> dict:
    events = next_days_events(token, n)
    report = {}
    for event in events:
        attendees = event.get('attendees', [])
        for attendee in attendees:
            email = attendee['emailAddress']['address']
            if email not in report:
                report[email] = 0
            report[email] += 1
    return report