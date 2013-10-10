from django.contrib.gis.db import models
from ..common.fields import StringUUIDField


class Event(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    point = models.PointField()
    radius = models.IntegerField(help_text="The area this event will notify in metres")
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title





