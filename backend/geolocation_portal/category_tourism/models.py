from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours

# Create your models here.
class MonumentEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 11)

    class Meta:
        verbose_name = "Denkmal"
        verbose_name_plural = "Denkmäler"

class OpeningHoursMonumentEntry(OpeningHours):
    monument_entry = models.OneToOneField(MonumentEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class TrailEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 12)

    class Meta:
        verbose_name = "Wanderweg"
        verbose_name_plural = "Wanderwege"


class ChurchEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 13)

    class Meta:
        verbose_name = "Kirche"
        verbose_name_plural = "Kirchen"
        
class OpeningHoursChurchEntry(OpeningHours):
    church_entry = models.OneToOneField(ChurchEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class AccommodationEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 14)

    class Meta:
        verbose_name = "Unterkunft"
        verbose_name_plural = "Unterkünfte"