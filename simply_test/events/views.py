from django.shortcuts import render

from django.http import HttpResponse
from .models import Area, City, Event
from datetime import datetime

# Create your views here.
def index(request):
    event_list = Event.objects.filter(date__gte=datetime.now()).order_by('date')
    context = {
        'events' : event_list,
    }
    return render(request, 'events/events.html', context)