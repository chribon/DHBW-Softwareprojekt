from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory

class GroundvalueEntry(PolygonEntry):
    price = models.TextField(verbose_name = 'Preis')
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 7)

    class Meta:
        verbose_name = "Bodenrichtwert"
        verbose_name_plural = "Bodenrichtwerte"


class BuildingareaEntry(PolygonEntry):
    areanumber = models.IntegerField(verbose_name = 'Baugebietnummer')
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 8)

    class Meta:
        verbose_name = "Baugebiet"
        verbose_name_plural = "Baugebiete"


class PlaygroundEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 9)

    class Meta:
        verbose_name = "Spielplatz"
        verbose_name_plural = "Spielplätze"


class SchoolEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 10)

    class Meta:
        verbose_name = "Schule"
        verbose_name_plural = "Schulen"
