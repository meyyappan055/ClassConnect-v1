# Class Connect

**Class Connect** is designed to simplify scheduling by automating the process of adding classes to your Google Calendar using FastAPI, Google Calendar API, and Streamlit for an intuitive backend and user interface, ensuring a seamless scheduling experience.

## Features
- Automates Google Calendar event creation for class schedules.
- Secure authentication using Google OAuth 2.0.
- Background scheduling with FastAPI and Python's `schedule` library.
- Simple and interactive UI built with Streamlit.

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/class-connect.git
   cd app
   
2. **Install Dependencies**  
   Install the required Python libraries:  
   ```bash
   pip install -r requirements.txt

3. **Set Up Google API Credentials**  
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the **Google Calendar API** for your project.
   - Create OAuth 2.0 credentials and download the `credentials.json` file.
   - Rename the file to `content.json` and place it in the root folder of the project.

4. **Run the Backend Server**  
   Start the FastAPI backend server:  
   ```bash
   cd backend
   uvicorn main:app --reload
   
5. **Run the Streamlit Frontend**  
   Launch the Streamlit app:  
   ```bash
   cd frontend
   streamlit run streamlit.py

6. **Start the Scheduler**  
   - Open the Streamlit app in your browser (`http://localhost:8501`).
   - Click on the **"Start Scheduler"** button to begin scheduling your classes automatically.

## Usage

1. **Authentication**  
   Upon running the backend for the first time, you'll be prompted to authenticate using your Google account. This will grant the application permission to add events to your Google Calendar.

2. **Schedule Classes**  
   - The backend will fetch class data and automatically create events in your Google Calendar based on the predefined schedule.
   - You can initiate the scheduling process by clicking the **"Start Scheduler"** button on the Streamlit frontend.

3. **Error Handling**  
   - In case of any issues during event creation, an error message will be displayed in the console and a response will be returned to the frontend.
  
     
## Technologies Used

- **FastAPI**: For building the backend API to handle event creation and scheduling.
- **Google Calendar API**: For interacting with Google Calendar and creating events.
- **Streamlit**: For building the simple frontend.
- **OAuth 2.0**: For secure authentication with Google services.
- **Schedule**: For scheduling the task of fetching and adding classes to the calendar.
- **Uvicorn**: ASGI server to run the FastAPI app.

