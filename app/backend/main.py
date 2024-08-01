from fastapi import FastAPI
from threading import Thread
from backend.cron_scheduler import start_scheduler

app = FastAPI()

@app.post("/api/schedule_classes")
async def start_scheduler_endpoint():
    Thread(target=start_scheduler,daemon=True).start()
    return{"status":"scheduler started"}
