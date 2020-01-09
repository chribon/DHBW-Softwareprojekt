from django.contrib import admin
from geoadmin.admin import admin_site
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import (
    OpeningHours,
    GlassEntry,
    ClothingEntry,
    BatteryEntry,
    IlluminantEntry,
    ElectroEntry,
    RecyclingcentreEntry,
)

class OpeningHoursAdmin(admin.TabularInline):
    model = OpeningHours

class GlassEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(GlassEntry, GlassEntryAdmin)


class ClothingEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ClothingEntry, ClothingEntryAdmin)


class BatteryEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(BatteryEntry, BatteryEntryAdmin)


class IlluminantEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(IlluminantEntry, IlluminantEntryAdmin)


class ElectroEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ElectroEntry, ElectroEntryAdmin)


class RecyclingcentreEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(RecyclingcentreEntry, RecyclingcentreEntryAdmin)
