from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from .models import Location, Person
from .serializers import LocationSerializer, PersonSerializer


class PersonViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class LocationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = Location
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(
            person__id=self.kwargs['person_id']
        )

    def pre_save(self, obj):
        obj.person = get_object_or_404(Person, id=self.kwargs['person_id'])


