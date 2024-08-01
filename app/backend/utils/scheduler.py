import datetime
from pytz import timezone
from backend.calendar_service.event_service import create_event
from backend.models.event_schema import Event
from backend.auth.google_auth import initialize_google_service

local_tz = timezone('Asia/Kolkata')

def schedule_day_order_classes(day_order, timetable_data):
    print(f"Scheduling classes for day order: {day_order}")
    try:
        service = initialize_google_service()  # Initialize service here

        for entry in timetable_data:
            if entry['day_order'] == day_order:
                print(f"Matched day order: {day_order} in entry: {entry}")
                for time_slot, class_info in entry.items():
                    if time_slot == "day_order":
                        continue
                    print(f"Processing time slot: {time_slot} with class info: {class_info}")
                    try:
                        start_time, end_time = time_slot.split(" - ")

                        # Combine date and time and localize to local timezone
                        start_datetime = local_tz.localize(datetime.datetime.combine(
                            datetime.date.today(),
                            datetime.datetime.strptime(start_time, "%H:%M").time()
                        ))
                        end_datetime = local_tz.localize(datetime.datetime.combine(
                            datetime.date.today(),
                            datetime.datetime.strptime(end_time, "%H:%M").time()
                        ))

                        print(f"Start datetime (Local): {start_datetime}")
                        print(f"End datetime (Local): {end_datetime}")

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
