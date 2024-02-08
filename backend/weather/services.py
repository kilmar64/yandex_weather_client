'''
Services module for main business logic
'''

from typing import Optional

import requests
from django.conf import settings


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


