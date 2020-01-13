from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    ParkingEntry,
    OpeningHoursParkingEntry,
)

class OpeningHoursParkingEntryAdmin(admin.TabularInline):
    model = OpeningHoursParkingEntry

class ParkingEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursParkingEntryAdmin, ]

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(ParkingEntry, ParkingEntryAdmin)
