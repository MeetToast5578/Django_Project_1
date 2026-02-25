import time
from celery import shared_task

@shared_task
def export():
    print('Process Start!')
    time.sleep(10)
    print('Process End!')