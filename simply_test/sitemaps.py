from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from events.models import Event

class StaticEventMap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['index',]

    def location(self, item):
        return reverse(item)

class EventsMap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Event.objects.all()