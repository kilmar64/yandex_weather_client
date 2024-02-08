from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
            'lat',
            'lon',
            'temp',
            'pressure',
            'wind_speed',
        ]
        read_only_fields = ['name', 'lat', 'lon']
