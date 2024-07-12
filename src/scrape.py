from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import pickle
import os
import json

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None  # Variable for storing OAuth2 credentials


def auth_token_handling():
    global creds
    if os.path.exists('token.json'):
        with open('token.json', 'r') as token:
            creds_data = json.load(token)
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('content.json', SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

auth_token_handling()

service = build('calendar', 'v3', credentials=creds)


class Event(BaseModel):
    summary: str
    location: str = None
    description: str = None
    start: datetime.datetime
    end: datetime.datetime


app = FastAPI()


@app.post("/events/")
async def create_event(event: Event):
    try:
        event_body = {
            'summary': event.summary,
            'location': event.location,
            'description': event.description,
            'start': {
                "dateTime": event.start.isoformat(),
                "timeZone": 'Asia/Kolkata'  # IST setting
            },
            'end': {
                "dateTime": event.end.isoformat(),
                "timeZone": 'Asia/Kolkata'  # IST setting
            }
        }

        created_event = service.events().insert(calendarId="primary", body=event_body).execute()
        return created_event
    except Exception as e:
        print(f"Error creating event: {e}")
        raise HTTPException(status_code=500, detail="Failed to create event")

