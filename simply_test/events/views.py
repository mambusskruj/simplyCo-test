from django.shortcuts import render, render_to_response, redirect

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

# def filter_paid(request, type='free'):
#     if request.POST:
#         if request.POST.get('type')=='free':
#             free_events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date') 
#             context = {
#                 'events' : free_events,
#                 'type' : type,
#             }
#             return render(request, 'events/events.html', context)
#         elif request.POST.get('type')=='paid':
#             type='paid'
#             paid_events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
#             context = {
#                 'events' : paid_events,
#                 'type' : type,
#             }
#             return render(request, 'events/events.html', context)

#     return HttpResponseRedirect('/events')


def filter_paid(request):
    if request.POST:
        if request.POST.get('type')=='free':
            if request.POST.get('city')!='all':
                return redirect('/events/type/free/city/'+request.POST.get('city'))
            return redirect('/events/type/free')
            
        elif request.POST.get('type')=='paid':
            if request.POST.get('city')!='all':
                return redirect('/events/type/paid/city/'+request.POST.get('city'))
            return redirect('/events/type/paid')

        if request.POST.get('city')!='all':
            return redirect('/events/city/'+request.POST.get('city'))

        return HttpResponseRedirect('/events')


def filter(request, filter1, value1):
    if filter1=='type':
        if value1=='free':
            free_events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date') 
            context = {
                'events' : free_events,
            }
            return render(request, 'events/events.html', context)

        if value1=='paid':
            free_events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date') 
            context = {
                'events' : free_events,
            }
            return render(request, 'events/events.html', context)
            
    if filter1=='city':
        city_events = Event.objects.filter(city_event=City.objects.get(slug=value1))
        context = {
                'events' : city_events,
            }
        return render(request, 'events/events.html', context)
    return HttpResponseRedirect('/events')


def filter2(request, filter1, filter2, value1, value2):
    events = []
    if filter1=='type':
        if value1=='free':
            events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date')
        if value1=='paid':
            events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
        if filter2=='city':
            city_events = events.filter(city_event=City.objects.get(slug=value2))
            context = {
                'events' : city_events,
            }
            return render(request, 'events/events.html', context)

    if filter1=='city':
        city_events = Event.objects.filter(city_event=City.objects.get(slug=value1))
        if filter2=='type':
            if value2=='free':
                events = city_events.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date')
                context = {
                    'events' : events,
                }
                return render(request, 'events/events.html', context)
            if value2=='paid':
                events = city_events.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
                context = {
                    'events' : events,
                }
                return render(request, 'events/events.html', context)
    return HttpResponseRedirect('/events')