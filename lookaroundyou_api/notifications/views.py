from rest_framework import mixins, viewsets
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Notification
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(
            person__id=self.kwargs['person_id']
        ).exclude(sent_at=None)


