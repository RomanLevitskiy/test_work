
from django.conf.urls import url, include
from django.contrib import admin

from messages_app import urls as messages_urls

urlpatterns = [
    url(r'^api/', include(messages_urls)),
    url(r'^admin/', admin.site.urls),
]
