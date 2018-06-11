from django.conf.urls import url
from messages_app import views
from .views import hello_world

urlpatterns = [
    url(r'^hello', hello_world, name="hello_world"),
    url(r'^messages/$', views.message_list),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.message_detail),
]
