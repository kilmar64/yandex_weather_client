from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('weather', views.WeatherView.as_view()),
]