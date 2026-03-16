import requests
from datetime import datetime, timedelta, timezone

def next_days_events(token: str, n: int) -> list:
   
    start_time = datetime.now(timezone.utc).isoformat()
    end_time = (datetime.now(timezone.utc) + timedelta(days=n)).isoformat()
    
    url = f"https://graph.microsoft.com/v1.0/me/calendarView?startDateTime={start_time}&endDateTime={end_time}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        events = []
        
        for event in data.get("value", []):
            events.append({
                "start": event["start"]["dateTime"],
                "subject": event["subject"],
                "organizer": event["organizer"]["emailAddress"]["name"]
            })
        
        return events
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []
