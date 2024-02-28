import shareRealTime
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import time

shareRealTime.executeShare()


# def job():
#     shareRealTime.executeShare()

# schedule.every().hour.do(job)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     time.sleep(1)
