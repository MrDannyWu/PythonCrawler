# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           scheduler.py
   Description:
   Author:        
   Create Date:    2021/02/01
-------------------------------------------------
   Modify:
                   2021/02/01:
-------------------------------------------------
"""
import apscheduler

from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick)
    scheduler.add_job(tick)

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


# from apscheduler.schedulers.background import BackgroundScheduler
# import time
#
# def process_to_execute():
#     # time.sleep(0.5)
#     print(1)
#
# scheduler = BlockingScheduler()
# scheduler.add_job(process_to_execute)
# scheduler.add_job(process_to_execute)
# scheduler.add_job(process_to_execute)
# scheduler.start()
