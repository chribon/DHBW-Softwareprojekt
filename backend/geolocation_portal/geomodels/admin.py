from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    Category,
    Subcategory,
    GlassTrashEntry,
)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'hauptkategorie']
    ordering = ['title']
    search_fields = ['title']

    def hauptkategorie(self, instance):
        return instance.id_category.title


admin.site.register(Subcategory, SubcategoryAdmin)


class GlassTrashEntryAdmin(LeafletGeoAdmin):
    list_display = ['title', 'unterkategorie']
    ordering = ['title']
    search_fields = ['title']

    def unterkategorie(self, instance):
        return instance.id_subcategory.title

admin.site.register(GlassTrashEntry, GlassTrashEntryAdmin)
