'''
Services module for main business logic
'''

import pytz
from typing import Optional
from datetime import datetime, timedelta

import requests
from django.conf import settings

from .models import City


def get_yandex_weather(lat: float, lon: float) -> Optional[dict]:
    '''
    Main API interaction function. Proceeds request to yandex weather.
    '''
    yandex_response = requests.get(
        settings.YANDEX_API_URL,
        params={
            'lat': lat,
            'lon': lon,
            'lang': 'en_US',
            'limit': 1,
            'hours': False,
            'extra': False,
        },
        headers={
            'X-Yandex-API-Key': settings.YANDEX_API_KEY
        }
    )

    if yandex_response.status_code != 200:
        return None

    fact_weather = yandex_response.json().get('fact')
    return fact_weather


def check_if_city_needs_to_fetch(city: City) -> bool:
    '''
    Checks saved fetch time and returns if it is old
    '''
    time_now = datetime.now().astimezone(pytz.utc) # Get current time in UTC timezone
    time_old = time_now - timedelta(minutes=30)

    return city.last_fetch_time is None or city.last_fetch_time < time_old


def update_weather_in_city(city: City) -> City:
    '''
    Updates city model with fresh data from yandex api
    '''

    if check_if_city_needs_to_fetch(city):
        print('Request to Yandex') # debug

        fetched_data = get_yandex_weather(city.lat, city.lon)
        if not fetched_data:
            return city

        # Parse response
        temp = int(fetched_data.get('temp'))
        pressure = int(fetched_data.get('pressure_mm'))
        wind_speed = int(fetched_data.get('wind_speed'))

        # Update actual model
        city.last_fetch_time = datetime.now().astimezone(pytz.utc)
        city.temp = temp
        city.pressure = pressure
        city.wind_speed = wind_speed
        city.save()

    return city