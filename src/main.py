import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USER_NAME")
PASSWD = os.getenv("PASSWORD")


LOGIN_URL = "https://academia-s-3.azurewebsites.net//login"
DATA_URL = "https://a.srmcheck.me/timetable"

headers = {
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

login_data = {
    "username" : USERNAME,
    "password" : PASSWD
}

response = session.post(LOGIN_URL,json=login_data,headers=headers)
print(f"Login response status: {response.status_code}")
print(f"Login response text: {response.text}") #will get token 

if response.status_code == 200:
    response_json = response.json() #response json is the response text which gives token -> {'token':'tokenvalue'}
    token = response_json.get('token')
    if token: #check token is extracted
        headers['X-Access-Token'] = token #this will add token with key as X-Access-Token in header which can be used for further requests
        print("token added to header")        
        
        #authentication done!
        
        # content = session.get(DATA_URL,headers=headers)
        # print(f"Data retrieval response status: {content.status_code}")
        # print(f"Data retrieval response URL: {content.url}")
        # print(f"Data retrieval response headers: {content.headers}")
        # print(f"Data retrieval response text: {content.text}")

        # if content.status_code == 200:
        #     print("content: ",content.json())
        # else:
        #     print(f" failed to retrieve content. status code : {content.status_code}")
         
