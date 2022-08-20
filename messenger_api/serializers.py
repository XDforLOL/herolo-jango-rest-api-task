from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message
import arrow


class MessageSerializer(serializers.ModelSerializer):
    sent_by = serializers.StringRelatedField()
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = [
            'sent_by',
            'subject',
            'body',
            'recipient',
            'read'
        ]
        read_only_fields = (
            'sent_by',
            'read'
        )


