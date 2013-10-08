from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Location, Person
from .serializers import LocationSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    model = Location
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(
            person__id=self.kwargs['person_id']
        )

    def pre_save(self, obj):
        obj.person = get_object_or_404(Person, id=self.kwargs['person_id'])


