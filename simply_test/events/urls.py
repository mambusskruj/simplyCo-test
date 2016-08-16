from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.EventView.as_view(), name='new_event'),
    url(r'^new/(?P<city>\w+)/$', views.EventView.as_view(), name='new_event'),
    url(r'^type/$', views.filter_form, name='filter-form'),
    url(r'^(?P<filter1>\w+)/(?P<value1>\w+)/$', views.filter_simple, name='filter_simple'),
    url(r'^(?P<filter1>\w+)/(?P<value1>\w+)/(?P<filter2>\w+)/(?P<value2>\w+)/$', views.filter_mix, name='filter_mix'),
]
#(?P<type>\w+)