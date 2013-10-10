import datetime
from django.test import TestCase
from .models import Event
from ..people.models import Person, Location

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

