import streamlit as st
import requests

def start_scheduler():
    response = requests.post("http://localhost:8000/api/schedule_classes")
    if response.status_code == 200:
        st.success("Scheduler started successfully!")
    else:
        st.error("Failed to start scheduler.")

st.title("Class connect")
st.text("by Meyyappan :)")
if st.button("Start Scheduler"):
    start_scheduler()
