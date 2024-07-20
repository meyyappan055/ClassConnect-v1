from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from fastapi.exceptions import HTTPException

def create_event(service, event):
    try:
        event_body = {
            'summary': event.summary,
            'location': event.location,
            'description': event.description,
            'start': {
                "dateTime": event.start.isoformat(),
                "timeZone": 'UTC'
            },
            'end': {
                "dateTime": event.end.isoformat(),
                "timeZone": 'UTC'
            }
        }
        print(f"Event body being sent to Google Calendar: {event_body}")
        created_event = service.events().insert(calendarId="primary", body=event_body).execute()
        print(f"Event created successfully: {created_event}")
        return created_event
    except Exception as e:
        print(f"Error creating event: {e}")
        raise HTTPException(status_code=500, detail="Failed to create event")
