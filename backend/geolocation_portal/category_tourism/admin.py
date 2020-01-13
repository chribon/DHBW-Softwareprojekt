from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    MonumentEntry,
    OpeningHoursMonumentEntry,
    TrailEntry,
    ChurchEntry,
    OpeningHoursChurchEntry,
    AccommodationEntry,
)

class OpeningHoursMonumentEntryAdmin(admin.TabularInline):
    model = OpeningHoursMonumentEntry

class MonumentEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursMonumentEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(MonumentEntry, MonumentEntryAdmin)


class TrailEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(TrailEntry, TrailEntryAdmin)


class OpeningHoursChurchEntryAdmin(admin.TabularInline):
    model = OpeningHoursChurchEntry

class ChurchEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursChurchEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ChurchEntry, ChurchEntryAdmin)


class AccommodationEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(AccommodationEntry, AccommodationEntryAdmin)
