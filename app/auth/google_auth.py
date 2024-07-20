import os
import json
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(CURRENT_DIR, 'token.json')
CONTENT_JSON_PATH = os.path.join(CURRENT_DIR, 'content.json')

creds = None  # Variable for storing OAuth2 credentials

def auth_token_handling():
    global creds
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CONTENT_JSON_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(TOKEN_PATH, 'w') as token_file:
                token_file.write(creds.to_json())
    
    return creds

creds = auth_token_handling()
print("Saving new credentials to token.json...")

with open(TOKEN_PATH, 'w') as token_file:
    token_file.write(creds.to_json())
    
print("Authentication completed successfully.")
print("Building Google Calendar service...")

service = build('calendar', 'v3', credentials=creds)

print("Google Calendar service built successfully.")
