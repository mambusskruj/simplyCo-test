from django.contrib import admin

# Register your models here.
from .models import Area, City, Event

admin.site.register(Area)
admin.site.register(City)
admin.site.register(Event)

