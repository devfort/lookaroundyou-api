from django.contrib.gis.db import models
from ..common.fields import StringUUIDField
from ..events.models import Event


class Person(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    send_push_notifications = models.BooleanField(default=True)
    apns_token = models.CharField(max_length=64, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)


class Location(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    person = models.ForeignKey(Person, related_name="locations")
    point = models.PointField()
    altitude = models.FloatField(blank=True, null=True)
    horizontal_accuracy = models.FloatField(default=0)
    vertical_accuracy = models.FloatField(default=0)
    course = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    measured_at = models.DateTimeField()

    class Meta:
        get_latest_by = 'created_at'

    def __unicode__(self):
        return "%s at %s" % (self.person, self.measured_at)

    def events(self):
        # ask @andrewgodwin.
        return Event.objects.extra(
            where=["ST_Distance_Sphere(ST_GeomFromText('%s', 4326), events_event.point) < events_event.radius" % self.point],
        )

