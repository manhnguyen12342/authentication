from django.db import models


class WeatherData(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()

