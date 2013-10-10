from apns import APNs, Payload
import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..common.fields import StringUUIDField
from ..events.models import Event
from ..people.models import Person, Location


class Notification(models.Model):
    id = StringUUIDField(primary_key=True, auto=True, hyphenate=True)
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event, blank=True, null=True, help_text="The event that this notification is about")
    location = models.ForeignKey(Location, blank=True, null=True, help_text="The location that triggered this notification")
    created_at = models.DateTimeField(auto_now=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def get_alert(self):
        if self.event:
            return unicode(self.event)
        else:
            return ''

    def send(self):
        apns = APNs(
            use_sandbox=True,
            cert_file='certs/push_cert.pem',
            key_file='certs/push_cert.pem'
        )
        payload = Payload(alert=self.body, sound="default", badge=1)
        apns.gateway_server.send_notification(self.person.apns_token, payload)
        self.sent_at = datetime.datetime.now()
        self.save()

    def __unicode__(self):
        return '%s at %s' % (self.person, self.created_at)


@receiver(post_save, sender=Notification)
def notification_post_save(sender, instance, **kwargs):
    if not instance.sent_at:
        instance.send()


