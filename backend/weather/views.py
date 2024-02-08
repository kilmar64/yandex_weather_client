from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from . import services
from .serializers import CitySerializer
from .models import City


class WeatherView(APIView):
    def get(self, request, format=None):
        # Get city name from query params
        city_name = request.query_params.get('city')
        if city_name is None:
            raise Http404
        city_name = city_name.lower()

        # Get city model
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            raise Http404

        # Update weather if needed
        city = services.update_weather_in_city(city)
        serializer = CitySerializer(city)

        return Response(serializer.data)
