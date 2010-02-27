from django.db import models
from django.utils.translation import ugettext_lazy as _

LOCATION_TYPE_FABLAB = 1
LOCATION_TYPE_SERVICELAB = 2
LOCATION_TYPE_INDIVIDUAL = 3
LOCATION_TYPES = (
    (LOCATION_TYPE_FABLAB, _("FabLab")),
    (LOCATION_TYPE_SERVICELAB, _("ServiceLab")),
    (LOCATION_TYPE_INDIVIDUAL, _("Individual")),
)

class Location(models.Model):
    type = models.PositiveSmallIntegerField(_("Type"), choices=LOCATION_TYPES)
    location_name = models.CharField(_("Location name"), max_length=100, blank=True)
    contact_name = models.CharField(_("Your name"), max_length=100, blank=True)
    address = models.CharField(_("Address"), max_length=255)
    latitude = models.FloatField(_("Latitude"), blank=True, null=True)
    longitude = models.FloatField(_("Longitude"), blank=True, null=True)
    website = models.URLField(_("URL"), blank=True, verify_exists=False)
    twitter = models.CharField(_("Twitter username"), max_length=64, blank=True)
    description = models.TextField(_("Description"), blank=True)
    email = models.EmailField(_("E-Mail"))