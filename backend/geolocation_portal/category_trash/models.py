from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from geomodels.models import PointEntry, PolygonEntry, Subcategory


class GlassEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 1)

    class Meta:
        verbose_name = "Glassammelstelle"
        verbose_name_plural = "Glassammelstellen"


class OpeningHoursGlassEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    glass_entry = models.OneToOneField(GlassEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class ClothingEntry(PointEntry):
    openingHours = models.TextField(verbose_name = 'Öffnungszeiten') #andere Feldart verwenden
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 2)

    class Meta:
        verbose_name = "Altkleidersammelstelle"
        verbose_name_plural = "Altkleidersammelstellen"

class OpeningHoursClothingEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    clothing_entry = models.OneToOneField(ClothingEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class BatteryEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 3)

    class Meta:
        verbose_name = "Batteriesammelstelle"
        verbose_name_plural = "Batteriesammelstellen"

class OpeningHoursBatteryEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    battery_entry = models.OneToOneField(BatteryEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class IlluminantEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 4)

    class Meta:
        verbose_name = "Leuchtmittelsammelstelle"
        verbose_name_plural = "Leuchtmittelsammelstelle"

class OpeningHoursIlluminantEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    illuminant_entry = models.OneToOneField(IlluminantEntry, blank=True, null=True, on_delete = models.PROTECT)



class ElectroEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 5)

    class Meta:
        verbose_name = "Elektroschrottsammelstelle"
        verbose_name_plural = "Elektroschrottsammelstellen"

class OpeningHoursElectroEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    electro_entry = models.OneToOneField(ElectroEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class RecyclingcentreEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 6)

    class Meta:
        verbose_name = "Wertstoffhof"
        verbose_name_plural = "Wertstoffhöfe"

class OpeningHoursRecyclingcentreEntry(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    recyclingcentre_entry = models.OneToOneField(RecyclingcentreEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"
