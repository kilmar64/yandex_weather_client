from rest_framework.views import APIView
from rest_framework.response import Response

from . import services


class WeatherView(APIView):
    def get(self, request, format=None):
        city = request.query_params.get('city')

        if city is None:
            return Response()

        print(services.get_yandex_weather(44.878414, 39.190289))

        return Response()