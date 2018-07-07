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
def clear_old_history_messages():
    days_old = 30
    data_history_for_delete = datetime.datetime.now() - datetime.timedelta(days=days_old)
    record_history = Message.history
    record_history.all().filter(history_date__lte=data_history_for_delete).delete()
            
