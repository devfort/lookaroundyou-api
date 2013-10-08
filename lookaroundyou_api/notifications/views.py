from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    model = Notification
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(
            person__id=self.kwargs['person_id']
        ).exclude(sent_at=None)

    def pre_save(self, obj):
        obj.person = get_object_or_404(Person, id=self.kwargs['person_id'])


