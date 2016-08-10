from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^type/$', views.filter_form, name='filter-form'),
    url(r'^(?P<filter1>\w+)/(?P<value1>\w+)/$', views.filter, name='filter'),
    url(r'^(?P<filter1>\w+)/(?P<value1>\w+)/(?P<filter2>\w+)/(?P<value2>\w+)/$', views.filter2, name='filter2'),
]

#(?P<type>\w+)