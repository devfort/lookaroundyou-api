from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    model = Notification
    serializer_class = NotificationSerializer

    def get_query_set(self):
        return Notification.objects.filter(
            person__id=self.kwargs['person_id']
        ).exclude(send_at=None)


