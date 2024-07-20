import os
from utils.fetch_data import fetch_and_schedule_classes

if __name__ == "__main__":
    try:
        fetch_and_schedule_classes()
    except Exception as e:
        print(f"Error during fetch and schedule process: {e}")
