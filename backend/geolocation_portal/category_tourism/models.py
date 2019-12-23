from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory

# Create your models here.
class MonumentEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 11)

    class Meta:
        verbose_name = "Denkmal"
        verbose_name_plural = "Denkmäler"


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


class AccommodationEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 14)

    class Meta:
        verbose_name = "Unterkunft"
        verbose_name_plural = "Unterkünfte"