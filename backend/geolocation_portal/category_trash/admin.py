from django.contrib import admin
from geoadmin.admin import admin_site
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import (
    OpeningHoursGlassEntry,
    GlassEntry,
    OpeningHoursClothingEntry,
    ClothingEntry,
    OpeningHoursBatteryEntry,
    BatteryEntry,
    OpeningHoursIlluminantEntry,
    IlluminantEntry,
    OpeningHoursElectroEntry,
    ElectroEntry,
    OpeningHoursRecyclingcentreEntry,
    RecyclingcentreEntry,
)

class OpeningHoursGlassEntryAdmin(admin.TabularInline):
    model = OpeningHoursGlassEntry

class GlassEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursGlassEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(GlassEntry, GlassEntryAdmin)


class OpeningHoursClothingEntryAdmin(admin.TabularInline):
    model = OpeningHoursClothingEntry

class ClothingEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursClothingEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ClothingEntry, ClothingEntryAdmin)



class OpeningHoursBatteryEntryAdmin(admin.TabularInline):
    model = OpeningHoursBatteryEntry

class BatteryEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursBatteryEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(BatteryEntry, BatteryEntryAdmin)



class OpeningHoursIlluminantEntryAdmin(admin.TabularInline):
    model = OpeningHoursIlluminantEntry

class IlluminantEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursIlluminantEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(IlluminantEntry, IlluminantEntryAdmin)



class OpeningHoursElectroEntryAdmin(admin.TabularInline):
    model = OpeningHoursElectroEntry

class ElectroEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursElectroEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ElectroEntry, ElectroEntryAdmin)



class OpeningHoursRecyclingcentreEntryAdmin(admin.TabularInline):
    model = OpeningHoursRecyclingcentreEntry

class RecyclingcentreEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursRecyclingcentreEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(RecyclingcentreEntry, RecyclingcentreEntryAdmin)
