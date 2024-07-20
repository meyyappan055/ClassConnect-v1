from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    summary: str
    location: str
    description: str
    start: datetime
    end: datetime
