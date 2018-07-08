from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import MessageSerializer
from .models import Message
#from rest_framework.permissions import IsAuthenticated



class SubscriberViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    #permission_classes = (IsAuthenticated,)

"""
    @action(methods=['get'], detail=True,
            url_path='history', url_name='history')
    def id_history():
        pass
        #return SubscriberViewSet.queryset[1]
"""
