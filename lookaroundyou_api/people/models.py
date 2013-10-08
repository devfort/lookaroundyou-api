from django.contrib.gis.db import models
from ..common.fields import StringUUIDField


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
    person = models.ForeignKey(Person)
    point = models.PointField()
    altitude = models.FloatField()
    horizontal_accuracy = models.FloatField()
    vertical_accuracy = models.FloatField()
    course = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    measured_at = models.DateTimeField()

    def __unicode__(self):
        return "%s at %s" % (self.person, self.measured_at)


