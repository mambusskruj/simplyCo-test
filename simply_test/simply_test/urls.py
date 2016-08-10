"""simply_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from sitemaps import EventsMap
from django.contrib.sitemaps.views import sitemap

from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

sitemaps = { 
    'events': EventsMap() 
}

urlpatterns = [
    url(r'^events/', include('events.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: / \nDisallow: /admin \nDissalow: /events/test \nAllow: /events \nSitemap: http://127.0.0.1:8000/sitemap.xml", content_type="text/plain")),
]

handler404 = 'events.views.page_not_found'
handler500 = 'events.views.server_error'