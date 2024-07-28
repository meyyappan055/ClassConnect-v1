import schedule
import time
from utils.fetch_data import fetch_and_schedule_classes

if __name__ == "__main__":
    def job():
        print("Starting fetch and schedule process")
        fetch_and_schedule_classes()

    # Schedule the job every day at midnight
    schedule.every().day.at("00:00").do(job)

    print("Starting scheduler")
    while True:
        schedule.run_pending()
        time.sleep(1)