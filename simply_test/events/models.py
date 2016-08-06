from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    city_area = models.ForeignKey(Area)

class Event(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField()
    isFree = models.BooleanField(default=False)
    city_event = models.ForeignKey(City)

