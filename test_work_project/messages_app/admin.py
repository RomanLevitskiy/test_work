from django.contrib import admin
from .models import Message
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class MessageAdmin(SimpleHistoryAdmin, admin.ModelAdmin):

    #admin.site.register(Message, MessageAdmin)
    admin.site.register(Message)
