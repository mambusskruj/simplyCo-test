from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    city_area = models.ForeignKey(Area)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField()
    isFree = models.BooleanField(default=False)
    city_event = models.ForeignKey(City)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/event/%i/" % self.pk 