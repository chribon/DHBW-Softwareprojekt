from rest_framework import serializers
from geomodels.models import (
    Category,
    Subcategory,
    Entry,
    PointEntry,
    PolygonEntry,
    GlassTrashEntry,
)


class CategorySerializer(serializers.ModelSerializer):
    #subcategories = SubcategorySerializer(many = True, read_only = True) # + Feld in fields auflisten, dann werden bei der Abfrage der Kategorien gleich die Subkategorien mitgegeben

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image')


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'id_category', 'title', 'description', 'image')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'content')

class PointEntrySerializer(EntrySerializer):
    class Meta(EntrySerializer.Meta):
        model = PointEntry
        fields = ('title', 'content', 'point')

class PolygonEntrySerializer(EntrySerializer):
    class Meta(EntrySerializer.Meta):
        model = PointEntry
        fields = ('title', 'content', 'polygon')

class GlassTrashEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = GlassTrashEntry
        fields = ('title', 'content', 'point')
