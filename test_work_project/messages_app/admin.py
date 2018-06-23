from django.contrib import admin
from .models import Message
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

#admin.site.register(Message)
admin.site.register(Message, SimpleHistoryAdmin)

