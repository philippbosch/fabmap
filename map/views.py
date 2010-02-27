from django.conf import settings
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from map.models import Location

class LocationForm(ModelForm):
    class Meta:
        model = Location

class HttpJsonResponse(HttpResponse):
    def __init__(self, content, mimetype=None, status=None, content_type=None, fields=None):
        content_type = 'application/json'
        content_type = 'text/plain' # TODO!
        content = simplejson.dumps(content)
        return super(HttpJsonResponse, self).__init__(content=content, status=status, content_type=content_type)

def index(request):
    add_form = LocationForm()
    return render_to_response('map/index.html', {'add_form': add_form, 'GOOGLE_MAPS_API_KEY': getattr(settings, 'GOOGLE_MAPS_API_KEY', '')}, context_instance=RequestContext(request))

def add_location(request):
    form = LocationForm(request.POST)
    try:
        form.save()
    except ValueError:
        return HttpJsonResponse({'status': 'INVALID'})
    return HttpJsonResponse({'status': 'OK'})

def locations(request):
    locations = Location.objects.all()
    data = []
    for location in locations:
        location.type_display = location.get_type_display();
        data.append(location.__dict__)
    return HttpJsonResponse(data)
