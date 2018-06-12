from rest_framework.viewsets import ModelViewSet

from .serializers import MessageSerializer
from .models import Message
#from rest_framework.permissions import IsAuthenticated



class SubscriberViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    #permission_classes = (IsAuthenticated,)


"""
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
"""
