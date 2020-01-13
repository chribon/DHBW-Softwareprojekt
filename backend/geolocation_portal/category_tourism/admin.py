from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    MonumentEntry,
    OpeningHoursMonumentEntry,
    AddressMonumentEntry,
    TrailEntry,
    AddressTrailEntry,
    ChurchEntry,
    OpeningHoursChurchEntry,
    AddressChurchEntry,
    AccommodationEntry,
    AddressAccommodationEntry,
)

class OpeningHoursMonumentEntryAdmin(admin.TabularInline):
    model = OpeningHoursMonumentEntry
class AddressMonumentEntryAdmin(admin.TabularInline):
    model = AddressMonumentEntry
class MonumentEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursMonumentEntryAdmin, AddressMonumentEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(MonumentEntry, MonumentEntryAdmin)


class AddressTrailEntryAdmin(admin.TabularInline):
    model = AddressTrailEntry
class TrailEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [AddressTrailEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(TrailEntry, TrailEntryAdmin)


class OpeningHoursChurchEntryAdmin(admin.TabularInline):
    model = OpeningHoursChurchEntry
class AddressChurchEntryAdmin(admin.TabularInline):
    model = AddressChurchEntry
class ChurchEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursChurchEntryAdmin, AddressChurchEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ChurchEntry, ChurchEntryAdmin)


class AddressAccommodationEntryAdmin(admin.TabularInline):
    model = AddressAccommodationEntry
class AccommodationEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [AddressAccommodationEntryAdmin]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(AccommodationEntry, AccommodationEntryAdmin)
