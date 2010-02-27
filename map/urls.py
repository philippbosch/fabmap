from django.conf.urls.defaults import *

urlpatterns = patterns('map.views',
    url(r'^$', 'index', name="map_index"),
    url(r'^add/$', 'add_location', name="map_add_location"),
    url(r'^locations.json$', 'locations', name="map_locations_json"),
)
