"""test_work_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from messages_app import models, serializers, views
from messages_app.models import Message
from django.urls import path
from django.contrib.auth import views as  auth_views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from messages_app.serializers import MessageSerializer, UserSerializer, GroupSerializer
from messages_app.views import MessageViewSet, UserViewSet, GroupViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializers


#class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed
    """
#    queryset = Message.objects.all()
#    serializer_class = MessageSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
   # path('admin/', admin.site.urls),
   # url(r'^ login / $', auth_views.login),
   # url(r'^$', views.empty_page, name='empty_page'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
