from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    GroundvalueEntry,
    BuildingareaEntry,
    PlaygroundEntry,
    SchoolEntry,
)

class GroundvalueEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(GroundvalueEntry, GroundvalueEntryAdmin)


class BuildingareaEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(BuildingareaEntry, BuildingareaEntryAdmin)


class PlaygroundEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(PlaygroundEntry, PlaygroundEntryAdmin)


class SchoolEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(SchoolEntry, SchoolEntryAdmin)
