from django.contrib.gis.db import models
from geomodels.models import PointEntry, PolygonEntry, Subcategory, Address

class GroundvalueEntry(PolygonEntry):
    using_type_choices = (
        ('privat', 'privat'),
        ('gemischt genutzt', 'gemischt genutzt'),
        ('gewerblich', 'gewerblich')
    )

    price           = models.DecimalField(max_digits = 6, decimal_places = 2, verbose_name = 'Preis (€) pro m²')
    using_type      = models.CharField(max_length = 30, choices = using_type_choices, verbose_name = "Nutzungsart")
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 7)

    class Meta:
        verbose_name = "Bodenrichtwert"
        verbose_name_plural = "Bodenrichtwerte"


class BuildingareaEntry(PolygonEntry):
    areanumber      = models.IntegerField(verbose_name = 'Baugebietnummer')
    no_buildingplaces = models.IntegerField(verbose_name = 'Anzahl Bauplätze')
    no_free_buildingplaces = models.IntegerField(verbose_name = 'Anzahl freie Bauplätze')
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 8)
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)

    class Meta:
        verbose_name = "Baugebiet"
        verbose_name_plural = "Baugebiete"


class PlaygroundEntry(PointEntry):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 9)
    description     = models.TextField(verbose_name = 'Beschreibung', blank=True, null=True)
    class Meta:
        verbose_name = "Spielplatz"
        verbose_name_plural = "Spielplätze"

class AddressPlaygroundEntry(Address):
    playground_entry = models.OneToOneField(PlaygroundEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"


class SchoolEntry(PointEntry):
    school_type_choices = (
        ('Grundschule', 'Grundschule'),
        ('Hauptschule', 'Hauptschule'),
        ('Realschule', 'Realschule'),
        ('Gesamtschule', 'Gesamtschule'),
        ('Gymnasium', 'Gymnasium')
    )
    
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie', default = 10)
    school_type  = models.CharField(max_length = 30, choices = school_type_choices, verbose_name = "Schulart")
    class Meta:
        verbose_name = "Schule"
        verbose_name_plural = "Schulen"

class AddressSchoolEntry(Address):
    school_entry = models.OneToOneField(SchoolEntry, blank=True, null=True, on_delete = models.PROTECT)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"
