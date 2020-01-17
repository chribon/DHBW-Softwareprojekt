from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours, Address

# Create your models here.
class ViewpointEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 15)

    class Meta:
        verbose_name = "Aussichtspunkt"
        verbose_name_plural = "Aussichtspunkte"

class OpeningHoursViewpointEntry(OpeningHours):
    viewpoint_entry = models.OneToOneField(ViewpointEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"
class AddressViewpointEntry(Address):
    viewpoint_entry = models.OneToOneField(ViewpointEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name_plural = "Adresse"
