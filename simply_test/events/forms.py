from django import forms
from .models import Event
from django.forms import ModelForm

# class EventForm(forms.Form):
#     name = forms.CharField(label='event name', max_length=300)
#     date = forms.DateTimeField()
#     isFree = forms.BooleanField()
#     city_event = forms.ChoiceField(choices=City.objects.all().values_list('slug', 'name'))


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'isFree', 'city_event']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'id': 'datetimepicker'}),
        }