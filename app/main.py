import os
from utils.fetch_data import fetch_and_schedule_classes
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_and_schedule_classes, 'cron', hour=0, minute=0 ) 
    try:
        print("Starting scheduler")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped")
        