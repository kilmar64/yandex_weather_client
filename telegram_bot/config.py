'''
Main configuration for telegram bot
'''

import os


TG_API_KEY = os.environ.get('TG_API_KEY')
WEATHER_API_URL = 'http://127.0.0.1:8000/weather'