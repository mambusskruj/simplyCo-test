from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import City, Event
from datetime import datetime

from .forms import EventForm
from django.views.generic.edit import FormView

# Create your views here.
city_list = City.objects.all()

#################################

class EventView(FormView):
    """Сlass-based view for ModelForm. Create new Event object.

    """
    template_name = 'event_form.html'
    form_class = EventForm

    def get(self, request, city=None):
        if city is not None:
            city = City.objects.filter(slug=city)[0].id
        form = self.form_class(initial={'city_event': city, 'isFree': False})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events')

        return render(request, self.template_name, {'form': form})

#################################

def index(request):
    """
    Render EVENT-APP index page, filter form post-request. 
    Redirect to views that render filtered query. 

    """
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

    event_list = Event.objects.filter(date__gte=datetime.now()).order_by('date')
    context = {
        'events' : event_list,
        'cities' : city_list,
    }

    return render(request, 'events/events.html', context)


def filter_simple(request, filter1, value1):
    """First filter render. Makes url like: /type/free/ or /city/kyiv/

    """

    if filter1=='type':
        if value1=='free':
            free_events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date') 
            context = {
                'events' : free_events,
                'cities' : city_list,
            }
            return render(request, 'events/events.html', context)

        if value1=='paid':
            free_events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date') 
            context = {
                'events' : free_events,
                'cities' : city_list,
            }
            return render(request, 'events/events.html', context)
            
    if filter1=='city':
        city_events = Event.objects.filter(city_event=City.objects.get(slug=value1)).filter(date__gte=datetime.now()).order_by('date')
        context = {
                'events' : city_events,
                'cities' : city_list,
                'city_url' : City.objects.get(slug=value1),
            }
        return render(request, 'events/events.html', context)
    return HttpResponseRedirect('/events')


def filter_mix(request, filter1, filter2, value1, value2):
    """Second filter render. Makes url like: /type/free/city/kyiv/ or /city/kyiv/type/free/

    """
    events = []

    if filter1=='type':
        if value1=='free':
            events = Event.objects.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date')
        if value1=='paid':
            events = Event.objects.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
        if filter2=='city':
            city_events = events.filter(city_event=City.objects.get(slug=value2)).filter(date__gte=datetime.now()).order_by('date')
            context = {
                'events' : city_events,
                'cities' : city_list,
                'city_url' : City.objects.get(slug=value2),
            }
            return render(request, 'events/events.html', context)

    if filter1=='city':
        city_events = Event.objects.filter(city_event=City.objects.get(slug=value1)).filter(date__gte=datetime.now()).order_by('date')
        if filter2=='type':
            if value2=='free':
                events = city_events.filter(isFree=True).filter(date__gte=datetime.now()).order_by('date')
                context = {
                    'events' : events,
                    'cities' : city_list,
                    'city_url' : City.objects.get(slug=value1),
                }
                return render(request, 'events/events.html', context)
            if value2=='paid':
                events = city_events.filter(isFree=False).filter(date__gte=datetime.now()).order_by('date')
                context = {
                    'events' : events,
                    'cities' : city_list,
                    'city_url' : City.objects.get(slug=value1),
                }
                return render(request, 'events/events.html', context)
    return HttpResponseRedirect('/events')


################################# 

def page_not_found(request):
    """Custom 404 page

    """
    response = render_to_response(
        'events/errors/404.html',
        context_instance=RequestContext(request)
    )
    
    response.status_code = 404
    
    return response

def server_error(request):
    """Custom 500 page
    
    """
    response = render_to_response(
        'events/errors/500.html',
        context_instance=RequestContext(request)
    )
    
    response.status_code = 500
    
    return response
    
################################# 