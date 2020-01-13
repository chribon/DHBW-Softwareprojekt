from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, OpeningHours, Address
from django.core.validators import MaxValueValidator

# Create your models here.
class MonumentEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 11)
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)
    buildingyear    = models.PositiveIntegerField(verbose_name = 'Errichtungsjahr', default=1900, validators=[MaxValueValidator(9999)])
    
    class Meta:
        verbose_name = "Denkmal"
        verbose_name_plural = "Denkmäler"

class OpeningHoursMonumentEntry(OpeningHours):
    monument_entry = models.OneToOneField(MonumentEntry, blank=True, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"

class AddressMonumentEntry(Address):
    monument_entry = models.OneToOneField(MonumentEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"


class TrailEntry(PointEntry):
    difficulty_choices = (
        ('1', 'leicht'),
        ('2', 'mittel'),
        ('3', 'schwer')
    )

    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 12)
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)
    length          = models.PositiveIntegerField(verbose_name = 'Länge (km)', default=10, validators=[MaxValueValidator(999)])
    difficulty      = models.CharField(max_length = 30, choices = difficulty_choices, verbose_name = "Schwierigkeitsgrad")

    class Meta:
        verbose_name = "Wanderweg"
        verbose_name_plural = "Wanderwege"

class AddressTrailEntry(Address):
    trail_entry = models.OneToOneField(TrailEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Startadresse"
        verbose_name_plural = "Startadressen"


class ChurchEntry(PointEntry):
    denomination_choices = (
        ('1', 'evangelisch'),
        ('2', 'katholisch'),
        ('3', 'sonstiges')
    )

    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 13)
    buildingyear    = models.PositiveIntegerField(verbose_name = 'Baujahr', default=1900, validators=[MaxValueValidator(9999)])
    denomination    = models.CharField(max_length = 30, choices = denomination_choices, verbose_name = "Konfession")

    class Meta:
        verbose_name = "Kirche"
        verbose_name_plural = "Kirchen"
        
class OpeningHoursChurchEntry(OpeningHours):
    church_entry    = models.OneToOneField(ChurchEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"
class AddressChurchEntry(Address):
    church_entry = models.OneToOneField(ChurchEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"


class AccommodationEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 14)
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)
    
    class Meta:
        verbose_name = "Unterkunft"
        verbose_name_plural = "Unterkünfte"
class AddressAccommodationEntry(Address):
    accommodation_entry = models.OneToOneField(AccommodationEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"