from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    ViewpointEntry,
    OpeningHoursViewpointEntry,
)

class OpeningHoursViewpointEntryAdmin(admin.TabularInline):
    model = OpeningHoursViewpointEntry

class ViewpointEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursViewpointEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ViewpointEntry, ViewpointEntryAdmin)
