import datetime
from django.test import TestCase
from .models import Event
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

