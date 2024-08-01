import schedule
import time
from backend.utils.fetch_data import fetch_and_schedule_classes
from backend.auth.google_auth import initialize_google_service


def start_scheduler():
    service = initialize_google_service()
    # def job():
    print("Starting fetch and schedule process")
    fetch_and_schedule_classes()

    # # Schedule the job every day at midnight
    # schedule.every().day.at("00:00").do(job)

    # print("Starting scheduler")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
        
