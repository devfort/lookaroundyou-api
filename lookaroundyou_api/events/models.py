import datetime
from django.contrib.gis.db import models
from django.contrib.gis.db.models.query import QuerySet
from ..common.fields import StringUUIDField


class EventQuerySet(QuerySet):
    def in_next(self, mins):
        """
        Returns events occuring in next `mins` minutes.
        """
        return self.filter(
            date_start__gt=datetime.datetime.now(),
            date_start__lte=datetime.datetime.now() + datetime.timedelta(seconds=mins*60)
        )

    def without_notifications(self, person):
        """
        Returns list of events which have no notifications for a person.
        """
        l = []
        for event in self:
            if event.notifications.filter(person=person).count() == 0:
                l.append(event)
        return l


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)


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

    objects = EventManager()

    def __unicode__(self):
        return self.title





