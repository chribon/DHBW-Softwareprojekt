from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    SportscentreEntry,
    OpeningHoursSportscentreEntry,
    AddressSportscentreEntry,
)

class OpeningHoursSportscentreEntryAdmin(admin.TabularInline):
    model = OpeningHoursSportscentreEntry
class AddressSportscentreEntryAdmin(admin.TabularInline):
    model = AddressSportscentreEntry
class SportscentreEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']
    exclude = ['id_subcategory']
    inlines = [OpeningHoursSportscentreEntryAdmin, AddressSportscentreEntryAdmin]    

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin_site.register(SportscentreEntry, SportscentreEntryAdmin)
