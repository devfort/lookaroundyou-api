from django.db import models
from ..common.fields import StringUUIDField


class Person(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    send_push_notifications = models.BooleanField(default=True)
    apns_token = models.CharField(max_length=64, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)


