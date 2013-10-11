import datetime
from django.contrib.gis.db import models
from ..common.fields import StringUUIDField
from ..events.models import Event
from ..notifications.models import Notification


class Person(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    send_push_notifications = models.BooleanField(default=True)
    apns_token = models.CharField(max_length=64, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)

    def send_notifications(self):
        if not self.send_push_notifications or not self.apns_token:
            return []
        try:
            # Locations in past day
            location = self.locations.filter(
                created_at__gt=datetime.datetime.now() - datetime.timedelta(days=1)
            ).latest()
        except Location.DoesNotExist:
            return []
        return location.send_notifications()


class Location(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    person = models.ForeignKey(Person, related_name="locations")
    point = models.PointField()
    altitude = models.FloatField(blank=True, null=True)
    horizontal_accuracy = models.FloatField(default=0)
    vertical_accuracy = models.FloatField(default=0)
    course = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    measured_at = models.DateTimeField()

    class Meta:
        get_latest_by = 'created_at'

    def __unicode__(self):
        return "%s at %s" % (self.person, self.measured_at)

    def events(self):
        """
        Returns events that cover this location.
        """
        # ask @andrewgodwin.
        return Event.objects.extra(
            where=["ST_Distance_Sphere(ST_GeomFromText('%s', 4326), events_event.point) < events_event.radius" % self.point],
        )

    def send_notifications(self):
        events = self.events().in_next(mins=5).without_notifications(self.person)
        notifications = []
        for event in events:
            notification = Notification.objects.create(
                person=self.person,
                location=self,
                event=event,
            )
            notifications.append(notification)
        return notifications



