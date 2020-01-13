from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator

class Category(models.Model):
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    description     = models.TextField(verbose_name = 'Beschreibung')
    image           = models.ImageField(verbose_name = 'Bild', upload_to = 'images/category/')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategorie (category)"
        verbose_name_plural = "Kategorien (categories)"


class Subcategory(models.Model):

    id_category     = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name = 'Hauptkategorie')
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    description     = models.TextField(verbose_name = 'Beschreibung')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    entry_type_choices = (
        ('groundvalueliving', 'Bodenrichtwerte'),
        ('buildingarealiving', 'Baugebiete'),
        ('playgroundliving', 'Spielplätze'),
        ('schoolliving', 'Schulen'),

        ('viewpointnature', 'Aussichtspunkte'),

        ('sportscentresparetime', 'Sporthallen'),

        ('monumenttourism', 'Denkmäler'),
        ('trailtourism', 'Wanderwege'),
        ('churchtourism', 'Kirchen'),
        ('accommodationtourism', 'Unterkünfte'),

        ('parkingtraffic', 'Parkplätze'),

        ('glasstrash', 'Glasmüll-Abgabestellen'),
        ('clothingtrash', 'Altkleider-Abgabestellen'),
        ('batterytrash', 'Batterie-Abgabestellen'),
        ('illuminanttrash', 'Leuchtmittel-Abgabestellen'),
        ('electrotrash', 'Elektroschrott-Abgabestellen'),
        ('recyclingcentretrash', 'Recyclingcenter'),
    )
    entry_types      = models.CharField(max_length = 30, choices = entry_type_choices, verbose_name = "Art der möglichen Einträge", default = 'glasstrash')

    coordinates_type_choices = (
        ('point', 'Punkt'),
        ('polygon', 'Polygon')
    )
    coordinates_type     = models.CharField(max_length = 30, choices = coordinates_type_choices, verbose_name = "Art der Koordinaten der Einträge", default = 'point')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Unterkategorie (feature class)"
        verbose_name_plural = "Unterkategorien (feature classes)"

class Entry(models.Model):
    #id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie') # --> bei jeder Eintrag-Klasse gepflegt
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    #content         = models.TextField(null = True, verbose_name = 'Inhalt') # --> bei jeder Eintrag-Klasse gepflegt
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Eintrag"
        verbose_name_plural = "Einträge"
        abstract = True


class PointEntry(Entry):
    coordinates = models.PointField()

    class Meta:
        abstract = True

class PolygonEntry(Entry):
    coordinates = models.PolygonField()

    class Meta:
        abstract = True


class OpeningHours(models.Model):
    monday = ArrayField(models.TimeField(verbose_name = "Montag"), blank = True, null = True)
    tuesday = ArrayField(models.TimeField(verbose_name = "Dienstag"), blank = True, null = True)
    wednesday = ArrayField(models.TimeField(verbose_name = "Mittwoch"), blank = True, null = True)
    thursday = ArrayField(models.TimeField(verbose_name = "Donnerstag"), blank = True, null = True)
    friday = ArrayField(models.TimeField(verbose_name = "Freitag"), blank = True, null = True)
    saturday = ArrayField(models.TimeField(verbose_name = "Samstag"), blank = True, null = True)
    sunday = ArrayField(models.TimeField(verbose_name = "Sonntag"), blank = True, null = True)

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"


class Address(models.Model):
    street          = models.CharField(max_length=1024, verbose_name = 'Straße')
    housenumber     = models.PositiveIntegerField(verbose_name = 'Hausnummer', validators=[MaxValueValidator(99999)])
    zipcode         = models.PositiveIntegerField(verbose_name = 'PLZ', default=74821, validators=[MaxValueValidator(99999)])
    city            = models.CharField(max_length=1024, verbose_name = 'Ort', default = 'Mosbach')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"