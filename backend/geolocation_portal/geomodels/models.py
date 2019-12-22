from django.contrib.gis.db import models

class Category(models.Model):
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    description     = models.TextField(verbose_name = 'Beschreibung')
    image           = models.ImageField(verbose_name = 'Bild', upload_to = 'images/category/')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"


class Subcategory(models.Model):

    id_category     = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name = 'Hauptkategorie')
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    description     = models.TextField(verbose_name = 'Beschreibung')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    entry_type_choices = (
        ('glasstrash', 'Glasmüll-Abgabestellen'),
        ('clothing', 'Altkleider-Abgabestellen'),
        ('batterytrash', 'Altbatterien-Abgabestellen'),
    )
    entry_types     = models.CharField(max_length = 30, choices = entry_type_choices, verbose_name = "Art der möglichen Einträge", default = 'glasstrash')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Unterkategorie"
        verbose_name_plural = "Unterkategorien"

class Entry(models.Model):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie')
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    content         = models.TextField(null = True, verbose_name = 'Inhalt')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Eintrag"
        verbose_name_plural = "Einträge"
        abstract = True


class PointEntry(Entry):
    point = models.PointField()

    class Meta:
        abstract = True

class PolygonEntry(Entry):
    polygon = models.PolygonField()

    class Meta:
        abstract = True


"""
Fully specified models
"""
class GlassTrashEntry(PointEntry):
    pass

    class Meta:
        verbose_name = "Glas-Müll-Punkt"
        verbose_name_plural = "Glas-Müll-Punkte"


class ClothingTrashEntry(PointEntry):
    pass

    class Meta:
        verbose_name = "Kleidungs-Müll-Punkt"
        verbose_name_plural = "Kleidungs-Müll-Punkte"


class BatteryTrashEntry(PointEntry):
    pass

    class Meta:
        verbose_name = "Batterien-Müll-Punkt"
        verbose_name_plural = "Batterien-Müll-Punkte"


