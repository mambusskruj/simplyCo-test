from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Area, City, Event
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    event_list = Event.objects.filter(date__gte=datetime.now()).order_by('date')
    context = {
        'events' : event_list,
    }
    return render(request, 'events/events.html', context)

def filter_paid(request):
    if request.POST:
        if request.POST.get('type')=='free':
            free_events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date') 
            context = {
                'events' : free_events,
            }
            return render(request, 'events/events.html', context)
        elif request.POST.get('type')=='paid':
            paid_events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
            context = {
                'events' : paid_events,
            }
            return render(request, 'events/events.html', context)
        return HttpResponseRedirect('/events')