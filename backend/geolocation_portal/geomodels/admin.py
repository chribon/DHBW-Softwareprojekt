from django.contrib import admin
from geoadmin.admin import admin_site

from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from .models import (
    Category,
    Subcategory,
)

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ['title', 'description']

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CategoryAdmin(ReadOnlyAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title']

admin_site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'hauptkategorie']
    ordering = ['title']
    search_fields = ['title']

    def hauptkategorie(self, instance):
        return instance.id_category.title

admin_site.register(Subcategory, SubcategoryAdmin)

