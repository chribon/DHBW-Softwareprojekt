from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory

# Create your models here.
class GlassEntry(PointEntry):
    openingHours = models.TextField(verbose_name = 'Öffnungszeiten') #andere Feldart verwenden
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 1)

    class Meta:
        verbose_name = "Glassammelstelle"
        verbose_name_plural = "Glassammelstellen"


class ClothingEntry(PointEntry):
    openingHours = models.TextField(verbose_name = 'Öffnungszeiten') #andere Feldart verwenden
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 2)

    class Meta:
        verbose_name = "Altkleidersammelstelle"
        verbose_name_plural = "Altkleidersammelstellen"


class BatteryEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 3)

    class Meta:
        verbose_name = "Batteriesammelstelle"
        verbose_name_plural = "Batteriesammelstellen"


class IlluminantEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 4)

    class Meta:
        verbose_name = "Leuchtmittelsammelstelle"
        verbose_name_plural = "Leuchtmittelsammelstelle"


class ElectroEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 5)

    class Meta:
        verbose_name = "Elektroschrottsammelstelle"
        verbose_name_plural = "Elektroschrottsammelstellen"


class RecyclingcentreEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 6)

    class Meta:
        verbose_name = "Wertstoffhof"
        verbose_name_plural = "Wertstoffhöfe"