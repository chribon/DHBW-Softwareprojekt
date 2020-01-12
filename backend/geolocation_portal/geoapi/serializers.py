from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from geomodels.models import (
    Category,
    Subcategory,
    Entry,
    PointEntry,
    PolygonEntry,
)
from category_living.models import (
    GroundvalueEntry,
    BuildingareaEntry,
    PlaygroundEntry,
    SchoolEntry,
)
from category_nature.models import (
    ViewpointEntry,
)
from category_sparetime.models import (
    SportscentreEntry,
)
from category_tourism.models import (
    MonumentEntry,
    TrailEntry,
    ChurchEntry,
    AccommodationEntry,
)
from category_traffic.models import (
    ParkingEntry,
)
from category_trash.models import (
    GlassEntry,
    OpeningHoursGlassEntry,
    ClothingEntry,
    OpeningHoursClothingEntry,
    BatteryEntry,
    OpeningHoursBatteryEntry,
    IlluminantEntry,
    OpeningHoursIlluminantEntry,
    ElectroEntry,
    OpeningHoursElectroEntry,
    RecyclingcentreEntry,
    OpeningHoursRecyclingcentreEntry,
)


class CategorySerializer(serializers.ModelSerializer):
    #subcategories = SubcategorySerializer(many = True, read_only = True) # + Feld in fields auflisten, dann werden bei der Abfrage der Kategorien gleich die Subkategorien mitgegeben
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image')

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'id_category', 'title', 'description', 'entry_types')

class EntrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Entry
        fields = ('title')

class PointEntrySerializer(EntrySerializer):
    class Meta(EntrySerializer.Meta):
        model = PointEntry
        geo_field = "coordinates"
        fields = ('title', 'coordinates')

class PolygonEntrySerializer(EntrySerializer):
    class Meta(EntrySerializer.Meta):
        model = PolygonEntry
        geo_field = "coordinates"
        fields = ('title', 'coordinates')


# Category Living
class GroundvalueEntrySerializer(PointEntrySerializer):
    class Meta(PolygonEntrySerializer.Meta):
        model = GroundvalueEntry
        fields = ('title', 'coordinates', 'price')

class BuildingareaEntrySerializer(PointEntrySerializer):
    class Meta(PolygonEntrySerializer.Meta):
        model = BuildingareaEntry
        fields = ('title', 'coordinates', 'areanumber')

class PlaygroundEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = PlaygroundEntry
        fields = ('title', 'coordinates')

class SchoolEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = SchoolEntry
        fields = ('title', 'coordinates')


# Category Nature
class ViewpointEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = ViewpointEntry
        fields = ('title', 'coordinates')


# Category Sparetime
class SportscentreEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = SportscentreEntry
        fields = ('title', 'coordinates')


# Category Tourism
class MonumentEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = MonumentEntry
        fields = ('title', 'coordinates')

class TrailEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = TrailEntry
        fields = ('title', 'coordinates')

class ChurchEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = ChurchEntry
        fields = ('title', 'coordinates')

class AccommodationEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = AccommodationEntry
        fields = ('title', 'coordinates')


# Category Traffic
class ParkingEntrySerializer(PointEntrySerializer):
    class Meta(PointEntrySerializer.Meta):
        model = ParkingEntry
        fields = ('title', 'coordinates')


# Category Trash
class OpeningHoursGlassEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursGlassEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class GlassEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursGlassEntrySerializer(read_only=True, source = 'openinghoursglassentry')

    class Meta(PointEntrySerializer.Meta):
        model = GlassEntry
        fields = ('title', 'coordinates', 'openinghours')

class OpeningHoursClothingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursClothingEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class ClothingEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursClothingEntrySerializer(read_only=True, source = 'openinghoursclothingentry')

    class Meta(PointEntrySerializer.Meta):
        model = ClothingEntry
        fields = ('title', 'coordinates', 'openingHours')

class OpeningHoursBatteryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursBatteryEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class BatteryEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursBatteryEntrySerializer(read_only=True, source = 'openinghoursbatteryentry')

    class Meta(PointEntrySerializer.Meta):
        model = BatteryEntry
        fields = ('title', 'coordinates')

class OpeningHoursIlluminantEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursIlluminantEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class IlluminantEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursIlluminantEntrySerializer(read_only=True, source = 'openinghoursilluminantentry')

    class Meta(PointEntrySerializer.Meta):
        model = IlluminantEntry
        fields = ('title', 'coordinates')

class OpeningHoursElectroEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursElectroEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class ElectroEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursElectroEntrySerializer(read_only=True, source = 'openinghourselectroentry')

    class Meta(PointEntrySerializer.Meta):
        model = ElectroEntry
        fields = ('title', 'coordinates')

class OpeningHoursRecyclingcentreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursRecyclingcentreEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class RecyclingcentreEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursRecyclingcentreEntrySerializer(read_only=True)

    class Meta(PointEntrySerializer.Meta):
        model = RecyclingcentreEntry
        fields = ('title', 'coordinates')
