import datetime
from pytz import timezone, utc
from calendar_service.event_service import create_event
from models.event_schema import Event
from auth.google_auth import service

def schedule_day_order_classes(day_order, timetable_data):
    print(f"Scheduling classes for day order: {day_order}")
    try:
        for entry in timetable_data:
            if entry['day_order'] == day_order:
                print(f"Matched day order: {day_order} in entry: {entry}")
                for time_slot, class_info in entry.items():
                    if time_slot == "day_order":
                        continue
                    print(f"Processing time slot: {time_slot} with class info: {class_info}")
                    try:
                        start_time, end_time = time_slot.split(" - ")

                        # Use UTC timezone
                        start_datetime = utc.localize(datetime.datetime.combine(
                            datetime.date.today(),
                            datetime.datetime.strptime(start_time, "%H:%M").time()
                        ))
                        end_datetime = utc.localize(datetime.datetime.combine(
                            datetime.date.today(),
                            datetime.datetime.strptime(end_time, "%H:%M").time()
                        ))

                        print(f"Start datetime (UTC): {start_datetime}")
                        print(f"End datetime (UTC): {end_datetime}")

                        event = Event(
                            summary=class_info[0],
                            location="",  # Add location if available
                            description="",  # Add description if available
                            start=start_datetime,
                            end=end_datetime
                        )
                        
                        created_event = create_event(service, event)
                        print(f"Created event: {created_event.get('id')}")
                    except Exception as e:
                        print(f"Error processing time slot {time_slot}: {e}")
    except Exception as e:
        print(f"Error in schedule_day_order_classes: {e}")
