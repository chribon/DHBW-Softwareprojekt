from django.contrib import admin
from geoadmin.admin import admin_site
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import (
    OpeningHoursGlassEntry,
    AddressGlassEntry,
    GlassEntry,
    OpeningHoursClothingEntry,
    AddressClothingEntry,
    ClothingEntry,
    OpeningHoursBatteryEntry,
    AddressBatteryEntry,
    BatteryEntry,
    OpeningHoursIlluminantEntry,
    AddressIlluminantEntry,
    IlluminantEntry,
    OpeningHoursElectroEntry,
    AddressElectroEntry,
    ElectroEntry,
    OpeningHoursRecyclingcentreEntry,
    AddressRecyclingcentreEntry,
    RecyclingcentreEntry,
)

class OpeningHoursGlassEntryAdmin(admin.TabularInline):
    model = OpeningHoursGlassEntry
class AddressGlassEntryAdmin(admin.TabularInline):
    model = AddressGlassEntry

class GlassEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursGlassEntryAdmin, AddressGlassEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(GlassEntry, GlassEntryAdmin)


class OpeningHoursClothingEntryAdmin(admin.TabularInline):
    model = OpeningHoursClothingEntry
class AddressClothingEntryAdmin(admin.TabularInline):
    model = AddressClothingEntry

class ClothingEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursClothingEntryAdmin, AddressClothingEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ClothingEntry, ClothingEntryAdmin)



class OpeningHoursBatteryEntryAdmin(admin.TabularInline):
    model = OpeningHoursBatteryEntry
class AddressBatteryEntryAdmin(admin.TabularInline):
    model = AddressBatteryEntry

class BatteryEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursBatteryEntryAdmin, AddressBatteryEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(BatteryEntry, BatteryEntryAdmin)



class OpeningHoursIlluminantEntryAdmin(admin.TabularInline):
    model = OpeningHoursIlluminantEntry
class AddressIlluminantEntryAdmin(admin.TabularInline):
    model = AddressIlluminantEntry

class IlluminantEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursIlluminantEntryAdmin, AddressIlluminantEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(IlluminantEntry, IlluminantEntryAdmin)



class OpeningHoursElectroEntryAdmin(admin.TabularInline):
    model = OpeningHoursElectroEntry
class AddressElectroEntryAdmin(admin.TabularInline):
    model = AddressElectroEntry

class ElectroEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursElectroEntryAdmin, AddressElectroEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ElectroEntry, ElectroEntryAdmin)



class OpeningHoursRecyclingcentreEntryAdmin(admin.TabularInline):
    model = OpeningHoursRecyclingcentreEntry
class AddressRecyclingcentreEntryAdmin(admin.TabularInline):
    model = AddressRecyclingcentreEntry

class RecyclingcentreEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursRecyclingcentreEntryAdmin, AddressRecyclingcentreEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(RecyclingcentreEntry, RecyclingcentreEntryAdmin)
