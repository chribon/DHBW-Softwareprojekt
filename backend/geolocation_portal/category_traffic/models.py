from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours

class ParkingEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 16)

    class Meta:
        verbose_name = "Parkplatz"
        verbose_name_plural = "Parkplätze"

class OpeningHoursParkingEntry(OpeningHours):
    parking_entry = models.OneToOneField(ParkingEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"
