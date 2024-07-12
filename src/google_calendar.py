import os
import requests
import datetime
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None #var for storing Oauth2 credentials


def auth_token_handling():
    global creds
    if os.path.exists('token.pickle'): 
        with open('token.pickle','rb') as token: #read binary to read , gives error if file is not there
            creds = Credentials.from_authorized_user_info(pickle.load(token),SCOPES)

    if not creds or not creds.valid: #creds missing (or) not valid
        if creds and creds.expired and creds.refresh_token: # if creds are there but expired , refresh trying
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('content.json',SCOPES)
            creds = flow.run_local_server(port=0) #running local server to recieve the auth code
            with open('token.pickle','wb') as token:
                pickle.dump(creds,token)

auth_token_handling()

service = build('calendar','v3',credentials=creds)


class Event(BaseModel):
    summary : str
    location : str = None
    description : str = None
    start : datetime.datetime
    end : datetime.datetime


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
        return {"error": str(e)}
    
    
# @app.put("/events/{event_id}")
# async def update_event(event_id : str , event : Event):
#     try:
#         event_body = {
#             'summary' : event.summary,
#             'location' : event.location,
#             'description' : event.description,
#             'start' : {
#                 "dateTime" : event.start.isoformat(),
#                 "timeZone" : 'Asia/Kolkata' #IST setting
#             },
#             'end' : {
#                 "dateTime" : event.end.isoformat(),
#                 "timeZone" : 'Asia/Kolkata' #IST setting
#             }
#         }
        
#         updated_event = service.events().update(CalendarId="primary",eventId = event_id,body=event_body).execute()
#         return updated_event
#     except:
#         print("couldn't update events")
