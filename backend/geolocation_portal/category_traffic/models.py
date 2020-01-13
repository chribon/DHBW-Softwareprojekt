from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours
from django.core.validators import MaxValueValidator

class ParkingEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 16)
    no_places    = models.PositiveIntegerField(verbose_name = 'Anzahl Parkplätze', validators=[MaxValueValidator(9999)])

    class Meta:
        verbose_name = "Parkplatz"
        verbose_name_plural = "Parkplätze"

class OpeningHoursParkingEntry(OpeningHours):
    parking_entry = models.OneToOneField(ParkingEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"
