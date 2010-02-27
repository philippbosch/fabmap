from django.contrib import admin

from map.models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'contact_name', 'address',)

admin.site.register(Location, LocationAdmin)
