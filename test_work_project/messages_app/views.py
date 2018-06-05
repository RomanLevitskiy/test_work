from django.shortcuts import render
from messages_app.models import Message
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from messages_app.serializers import MessageSerializer, UserSerializer, GroupSerializer


# Create your views here.

def empty_page(request):
    return render(request, 'messages_app/empty_page.html', {})


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
