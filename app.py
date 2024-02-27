import shareRealTime
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    shareRealTime()

schedule.every().minute.do(job)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
