from django.db import models


class City(models.Model):
    name = models.CharField(max_length=127)
    lat = models.FloatField()
    lon = models.FloatField()
    last_fetch_time = models.DateTimeField(null=True)

    # Weather fields
    temp = models.IntegerField(null=True)
    pressure = models.IntegerField(null=True)
    wind_speed = models.IntegerField(null=True)
