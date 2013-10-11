import datetime
from django.test import TestCase
import mock
from ..events.models import Event
from ..notifications.models import Notification
from .models import Person, Location

class TestPerson(TestCase):
    @mock.patch.object(Notification, 'send')
    def test_send_notifications(self, send_patch):
        dt = datetime.datetime.now() + datetime.timedelta(seconds=60*2)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )
        person = Person.objects.create()
        location = Location.objects.create(
            person=person,
            measured_at=datetime.datetime.now(),
            point='POINT(51.5 0)',
        )
        notifications = person.send_notifications()
        self.assertEqual(len(notifications), 1)
        self.assertEqual(notifications[0].event, event)
        self.assertEqual(notifications[0].location, location)

    @mock.patch.object(Notification, 'send')
    def test_send_notifications_in_future(self, send_patch):
        dt = datetime.datetime.now() + datetime.timedelta(seconds=60*10)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )
        person = Person.objects.create()
        location = Location.objects.create(
            person=person,
            measured_at=datetime.datetime.now(),
            point='POINT(51.5 0)',
        )
        notifications = person.send_notifications()
        self.assertEqual(len(notifications), 0)

    @mock.patch.object(Notification, 'send')
    def test_send_notifications_with_old_locations(self, send_patch):
        dt = datetime.datetime.now() + datetime.timedelta(seconds=60*2)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )
        person = Person.objects.create()
        location = Location.objects.create(
            person=person,
            measured_at=datetime.datetime.now() - datetime.timedelta(days=2),
            point='POINT(51.5 0)',
        )
        location.created_at = location.measured_at
        location.save()
        notifications = person.send_notifications()
        self.assertEqual(len(notifications), 0)


class TestLocation(TestCase):
    def test_events(self):
        location = Location.objects.create(
            person=Person.objects.create(),
            measured_at=datetime.datetime.now(),
            point='POINT(51.5 0)',
        )
        event = Event.objects.create(
            title='test',
            date_start=datetime.datetime.now(),
            date_end=datetime.datetime.now(),
            point='POINT(51.51 0.01)',
            radius=2000
        )

        self.assertEqual(list(location.events()), [event])

    def test_events_no_locations(self):
        location = Location.objects.create(
            person=Person.objects.create(),
            measured_at=datetime.datetime.now(),
            point='POINT(51.5 0)',
        )
        event = Event.objects.create(
            title='test',
            date_start=datetime.datetime.now(),
            date_end=datetime.datetime.now(),
            point='POINT(51.6 0.01)',
            radius=1
        )

        self.assertEqual(list(location.events()), [])



