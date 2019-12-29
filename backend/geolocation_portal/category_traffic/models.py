from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory

class ParkingEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 16)

    class Meta:
        verbose_name = "Parkplatz"
        verbose_name_plural = "Parkplätze"
