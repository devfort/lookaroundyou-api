from rest_framework import serializers
from rest_framework_gis.fields import GeometryField
from .models import Location, Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person


class LocationSerializer(serializers.ModelSerializer):
    person = serializers.CharField(read_only=True)
    point = GeometryField()

    class Meta:
        model = Location


