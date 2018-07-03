from __future__ import absolute_import, unicode_literals
from celery import task
from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Message
import datetime


app = Celery()
logger = get_task_logger(__name__)

@app.task
def test(arg):
    print(arg)


@periodic_task(
    run_every=(crontab(days=1)),
    name="clear_old_messages",
    ignore_result=True
)
def clear_old_messages():
    daysBeforDeleteMessages = 30
    nowDate = datetime.datetime.now()
    requestMessages = Message.objects.all()
    for i in requestMessages:
        #print("check now message:")
        delta = nowDate.date() - i.data_create
        if int(delta.days) > daysBeforDeleteMessages:
            print("Delete message")
            i.delete()
            
