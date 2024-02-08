import pytz
from datetime import datetime, timedelta
from django.test import TestCase

from . import services
from .models import City


class ServicesTestCase(TestCase):
    fixtures = ['weather/fixtures/City.json']

    def test_get_yandex_weather(self):
        # Test for Moscow
        lat = 55.753215
        lon = 37.622504

        response = services.get_yandex_weather(lat, lon)

        self.assertTrue(isinstance(response, dict))
        self.assertIsNotNone(response.get('temp'))
        self.assertIsNotNone(response.get('pressure_mm'))
        self.assertIsNotNone(response.get('wind_speed'))

    def test_check_if_city_needs_to_fetch(self):
        time_now = datetime.now().astimezone(pytz.utc)
        time_29_mins_before = time_now - timedelta(minutes=29)
        time_30_mins_before = time_now - timedelta(minutes=30)
        time_31_mins_before = time_now - timedelta(minutes=31)

        city1 = City(name='moscow', last_fetch_time=time_29_mins_before)
        city2 = City(name='moscow', last_fetch_time=time_30_mins_before)
        city3 = City(name='moscow', last_fetch_time=time_31_mins_before)
        city4 = City(name='moscow')

        self.assertFalse(services.check_if_city_needs_to_fetch(city1))
        self.assertTrue(services.check_if_city_needs_to_fetch(city2))
        self.assertTrue(services.check_if_city_needs_to_fetch(city3))
        self.assertTrue(services.check_if_city_needs_to_fetch(city4))

    def test_update_weather_in_city(self):
        time_now = datetime.now().astimezone(pytz.utc)
        time_31_mins_before = time_now - timedelta(minutes=31)
        lat = 55.753215
        lon = 37.622504

        city_update = City(name='moscow', last_fetch_time=time_31_mins_before, lat=lat, lon=lon)
        city_not_update = City(name='moscow', last_fetch_time=time_now, lat=lat, lon=lon)

        city_update = services.update_weather_in_city(city_update)
        city_not_update = services.update_weather_in_city(city_not_update)

        self.assertIsNone(city_not_update.temp)
        self.assertIsNotNone(city_update.temp)
