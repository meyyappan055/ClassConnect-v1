import os
import requests
from dotenv import load_dotenv
from utils.scheduler import schedule_day_order_classes

load_dotenv()

USERNAME = os.getenv("COLLEGE_USERNAME")
PASSWORD = os.getenv("COLLEGE_PASSWORD")

LOGIN_URL = "https://academia-s-3.azurewebsites.net//login"
DATA_URL = "https://academia-s-2.azurewebsites.net//course-user"
DO_URL = "https://academia-s-3.azurewebsites.net/do"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://a.srmcheck.me',
    'Referer': 'https://a.srmcheck.me/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Gpc': '1'
}
session = requests.Session()

def authenticate():
    login_data = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, json=login_data, headers=HEADERS)
    response.raise_for_status()
    token = response.json().get('token')
    if token:
        HEADERS['X-Access-Token'] = token
        print("Authentication successful")
        return True
    print("Authentication failed")
    return False
    
    
def fetch_day_order():
    response = session.post(DO_URL, headers=HEADERS)
    response.raise_for_status()
    day_order = response.json().get('day_order')
    if day_order:
        day_order = ''.join(filter(str.isdigit, day_order))
        if day_order:
            day_order = int(day_order)
        else:
            day_order = None
    print(f"Fetched day order: {day_order}")
    return day_order


def fetch_timetable():
    response = session.post(DATA_URL, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    timetable = data.get("time-table", []) 
    print(f"Fetched timetable: {timetable}")
    return timetable


def fetch_and_schedule_classes():
    try:
        print("Starting fetch and schedule process")
        if authenticate():
            print("Authentication successful")
            day_order = fetch_day_order()
            if day_order:
                timetable_data = fetch_timetable()
                schedule_day_order_classes(day_order, timetable_data)
            else:
                print("No Day Order available")
        else:
            print("Authentication failed")
    except Exception as e:
        print(f"Error in fetch_and_schedule_classes: {e}")
