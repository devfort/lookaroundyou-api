import datetime
from django.test import TestCase
import mock
from .models import Event
from ..notifications.models import Notification
from ..people.models import Person, Location


class TestEvent(TestCase):
    def test_in_next(self):
        dt = datetime.datetime.now() + datetime.timedelta(seconds=60*2)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )

        self.assertEqual(list(Event.objects.all().in_next(mins=5)), [event])

    def test_in_next_with_event_in_past(self):
        dt = datetime.datetime.now() - datetime.timedelta(seconds=60*2)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )

        self.assertEqual(list(Event.objects.all().in_next(mins=5)), [])

    def test_in_next_with_event_in_future(self):
        dt = datetime.datetime.now() + datetime.timedelta(seconds=60*9)
        event = Event.objects.create(
            title='test',
            date_start=dt,
            date_end=dt,
            point='POINT(51.51 0.01)',
            radius=2000
        )

        self.assertEqual(list(Event.objects.all().in_next(mins=5)), [])

    def test_without_notifications(self):
        person = Person.objects.create()
        event = Event.objects.create(
            title='test',
            date_start=datetime.datetime.now(),
            date_end=datetime.datetime.now(),
            point='POINT(51.51 0.01)',
            radius=2000
        )
        self.assertEqual(list(Event.objects.all().without_notifications(person)), [event])

    @mock.patch.object(Notification, 'send')
    def test_without_notifications_with_notifications(self, send_patch):
        person = Person.objects.create()
        event = Event.objects.create(
            title='test',
            date_start=datetime.datetime.now(),
            date_end=datetime.datetime.now(),
            point='POINT(51.51 0.01)',
            radius=2000
        )
        notification = Notification.objects.create(
            person=person,
            event=event,
        )
        self.assertEqual(list(Event.objects.all().without_notifications(person)), [])

    @mock.patch.object(Notification, 'send')
    def test_without_notifications_with_notifications_for_other_person(self, send_patch):
        person = Person.objects.create()
        other_person = Person.objects.create()
        event = Event.objects.create(
            title='test',
            date_start=datetime.datetime.now(),
            date_end=datetime.datetime.now(),
            point='POINT(51.51 0.01)',
            radius=2000
        )
        notification = Notification.objects.create(
            person=other_person,
            event=event,
        )
        self.assertEqual(list(Event.objects.all().without_notifications(person)), [event])


