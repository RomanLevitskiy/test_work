from django.db import models

# Create your models here.
class Role(models.Model):
    user_role = models.CharField(max_length = 128, verbose_name = "User role", unique = True)


class User(models.Model):
    first_name = models.CharField(max_length = 128, verbose_name = "User first name")
    last_name = models.CharField(max_length = 128, verbose_name = "User last name")
    email = models.EmailField(unique = True, verbose_name = "User email", help_text = "Unique email")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_create = models.DateField(auto_now_add = True, verbose_name = "Date create message")
    data_last_chenges = models.DateField(auto_now = True, verbose_name = "Date chenges message")
    text_message = models.TextField(max_length = 512, verbose_name = "Text", help_text ="message max length 512 chars")
