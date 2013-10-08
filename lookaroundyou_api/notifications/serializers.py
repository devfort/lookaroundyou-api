from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    sent_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Notification


