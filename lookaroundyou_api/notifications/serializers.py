from rest_framework import serializers
from ..people.models import Person
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    person = serializers.CharField(read_only=True)
    sent_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Notification


