from django.db import models
from django.contrib.postgres.fields import JSONField


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
    POINT       = 'point'
    POLYGON     = 'polygon'
    STATICTYPE  = 'static'
    
    SUBCATTYPES = (
        (POINT, 'Punkt'),
        (POLYGON, 'Polygon'),
        (STATICTYPE, 'Statisch')
    )

    id_category     = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name = 'Hauptkategorie')
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    description     = models.TextField(verbose_name = 'Beschreibung')
    type            = models.CharField(max_length=20, choices = SUBCATTYPES, verbose_name = 'Typ der Kategorie')
    image           = models.ImageField(upload_to = 'images/subcategory/', verbose_name = 'Bild')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Unterkategorie"
        verbose_name_plural = "Unterkategorien"



class Entry(models.Model):
    id_subcategory  = models.ForeignKey(Subcategory, on_delete = models.PROTECT, verbose_name = 'Unterkategorie')
    title           = models.CharField(max_length=1024, verbose_name = 'Titel')
    content         = models.TextField(verbose_name = 'Inhalt')
    coordinates     = JSONField(verbose_name = 'Koordinaten')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Eintrag"
        verbose_name_plural = "Einträge"