from messages_app.models import Message
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text_message = serializers.CharField(default='no text')
    user = serializers.CharField(read_only=True)
    data_create = serializers.DateField(read_only=True)
    date_last_chenges = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.text_message = validated_date.get('text_message', instance.text_message)
        return instance


    def getMessagesOnPk(self, primKey):
        return Message.objects.get(pk=primKey)


    def deleteMessagesOnPk(self, primKey):
        return Message.objects.filter(pk=primKey).delete()


    def getAllMessages(self):
        return Message.objects.all()

"""
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'data_create', 'data_last_cheges', 'text_message')
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
