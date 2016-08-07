from django.shortcuts import render

from django.http import HttpResponse
from .models import Area, City, Event

# Create your views here.
def index(request):
    event_list = Event.objects.all()
    context = {
        'events' : event_list,
    }
    return render(request, 'events/events.html', context)