import schedule     #Module to schedule time
from plyer import notification      #Notification module
import time     #Time module to keep a track of minutes for notification
from datetime import datetime   #Module to record the current time

# Input for the task reminder
title = input("Enter the title for the notification: ").strip()

#Handling empty input
if not title:
    title = "Reminder"

def send_reminder():
    current_time = datetime.now().strftime("%I:%M %p")
    notification.notify(
        title=title,
        message=f"It's {current_time}. Your task was: '{title}'",
        timeout=5
    )

#Interval based on user's choice
interval = int(input("Enter reminder interval in minutes: "))

# Schedule the reminder every 30 minutes
schedule.every(interval).minutes.do(send_reminder)

print(f"🔔 Reminder for '{title}' is running every 30 minutes. Press Ctrl+C to stop.")

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)
