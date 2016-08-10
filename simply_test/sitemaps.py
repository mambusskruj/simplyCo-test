from django.contrib.sitemaps import Sitemap

from events.models import Event

class EventsMap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Event.objects.all()