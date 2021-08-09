import schedule
import time
import os

# scheduler job
def backup():
    os.system('python3 backup.py')

# schedule every 03:00 AM
schedule.every().day.at("03:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)