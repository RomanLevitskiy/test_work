from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime, date, time
# Create your models here.
"""
class Role(models.Model):
    user_role = models.CharField(max_length = 128, verbose_name = "User role", unique = True)

def __str__(self):
    return self.user_role

class User(models.Model):
    first_name = models.CharField(max_length = 128, verbose_name = "User first name")
    last_name = models.CharField(max_length = 128, verbose_name = "User last name")
    email = models.EmailField(unique = True, verbose_name = "User email", help_text = "Unique email")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
"""

class Message(models.Model):
    """user = models.ForeignKey(User, on_delete=models.CASCADE)"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_create = models.DateField(auto_now_add = True, verbose_name = "Date create message")
    data_last_chenges = models.DateField(auto_now = True, verbose_name = "Date chenges message")
    title = models.CharField("title message", max_length = 128, default="message " + settings.AUTH_USER_MODEL)
    text_message = models.TextField(max_length = 512, verbose_name = "Text", help_text ="message max length 512 chars")

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
