from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory

# Create your models here.
class ViewpointEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 15)

    class Meta:
        verbose_name = "Aussichtspunkt"
        verbose_name_plural = "Aussichtspunkte"