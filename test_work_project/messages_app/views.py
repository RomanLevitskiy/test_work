from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from messages_app.models import Message
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from messages_app.serializers import MessageSerializer, UserSerializer, GroupSerializer



from django.http.response import JsonResponse

def hello_world(request):
    return JsonResponse({"message":"hello world!"})


# Create your views here.
@csrf_exempt
def message_list(request):
    """
    List all code messages.
    """
    if request.method == 'GET':
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return JsonResponse(serializer.data, safe=false)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def message_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        message.delete()
        return HttpResponse(status=204)


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
