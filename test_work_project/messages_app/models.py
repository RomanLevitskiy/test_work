from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime, date, time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from simple_history.models import HistoricalRecords
# Create your models here.

class Message(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_create=models.DateField("date create", auto_now_add=True)
    data_last_chenges=models.DateField("date chenges", auto_now=True)
    text_message=models.TextField(verbose_name="Text")
    history = HistoricalRecords()

    def __str__(self):
        return self.text_message

 

