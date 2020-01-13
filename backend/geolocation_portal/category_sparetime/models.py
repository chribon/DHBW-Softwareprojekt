from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours

# Create your models here.
class SportscentreEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 17)

    class Meta:
        verbose_name = "Sporthalle"
        verbose_name_plural = "Sporthallen"

class OpeningHoursSportscentreEntry(OpeningHours):
    sportscentre_entry = models.OneToOneField(SportscentreEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"