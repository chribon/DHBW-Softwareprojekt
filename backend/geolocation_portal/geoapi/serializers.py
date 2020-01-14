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
    AddressPlaygroundEntry,
    SchoolEntry,
    AddressSchoolEntry,
)
from category_nature.models import (
    ViewpointEntry,
    OpeningHoursViewpointEntry,
    AddressViewpointEntry,
)
from category_sparetime.models import (
    SportscentreEntry,
    OpeningHoursSportscentreEntry,
    AddressSportscentreEntry,
)
from category_tourism.models import (
    MonumentEntry,
    OpeningHoursMonumentEntry,
    AddressMonumentEntry,
    TrailEntry,
    AddressTrailEntry,
    ChurchEntry,
    AddressChurchEntry,
    OpeningHoursChurchEntry,
    AccommodationEntry,
    AddressAccommodationEntry,
)
from category_traffic.models import (
    ParkingEntry,
    OpeningHoursParkingEntry,
)
from category_trash.models import (
    GlassEntry,
    OpeningHoursGlassEntry,
    AddressGlassEntry,
    ClothingEntry,
    OpeningHoursClothingEntry,
    AddressClothingEntry,
    BatteryEntry,
    OpeningHoursBatteryEntry,
    AddressBatteryEntry,
    IlluminantEntry,
    OpeningHoursIlluminantEntry,
    AddressIlluminantEntry,
    ElectroEntry,
    OpeningHoursElectroEntry,
    AddressElectroEntry,
    RecyclingcentreEntry,
    OpeningHoursRecyclingcentreEntry,
    AddressRecyclingcentreEntry,
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
        fields = ('title', 'coordinates', 'price', 'using_type', 'description')

class BuildingareaEntrySerializer(PointEntrySerializer):
    class Meta(PolygonEntrySerializer.Meta):
        model = BuildingareaEntry
        fields = ('title', 'coordinates', 'areanumber', 'no_buildingplaces', 'no_free_buildingplaces', 'description')

class AddressPlaygroundEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressPlaygroundEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class PlaygroundEntrySerializer(PointEntrySerializer):
    address = AddressPlaygroundEntrySerializer(read_only=True, source = 'addressplaygroundentry')
    class Meta(PointEntrySerializer.Meta):
        model = PlaygroundEntry
        fields = ('title', 'coordinates', 'description', 'address')

class AddressSchoolEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressSchoolEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class SchoolEntrySerializer(PointEntrySerializer):
    address = AddressSchoolEntrySerializer(read_only=True, source = 'addressschoolentry')
    class Meta(PointEntrySerializer.Meta):
        model = SchoolEntry
        fields = ('title', 'coordinates', 'school_type', 'address')


# Category Nature
class OpeningHoursViewpointEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursViewpointEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressViewpointEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressViewpointEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class ViewpointEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursViewpointEntrySerializer(read_only=True, source = 'openinghoursviewpointentry')
    address = AddressViewpointEntrySerializer(read_only=True, source = 'addressviewpointentry')
    class Meta(PointEntrySerializer.Meta):
        model = ViewpointEntry
        fields = ('title', 'coordinates', 'openinghours', 'address')


# Category Sparetime
class OpeningHoursSportscentreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursSportscentreEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressSportscentreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressSportscentreEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class SportscentreEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursSportscentreEntrySerializer(read_only=True, source = 'openinghourssportscentreentry')
    address = AddressSportscentreEntrySerializer(read_only=True, source = 'addresssportscentreentry')
    class Meta(PointEntrySerializer.Meta):
        model = SportscentreEntry
        fields = ('title', 'coordinates', 'openinghours', 'address')


# Category Tourism
class OpeningHoursMonumentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursMonumentEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressMonumentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressMonumentEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class MonumentEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursMonumentEntrySerializer(read_only=True, source = 'openinghoursmonumententry')
    address = AddressMonumentEntrySerializer(read_only=True, source = 'addressmonumententry')
    class Meta(PointEntrySerializer.Meta):
        model = MonumentEntry
        fields = ('title', 'coordinates', 'description', 'buildingyear', 'openinghours', 'address')


class AddressTrailEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressTrailEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class TrailEntrySerializer(PointEntrySerializer):
    address = AddressTrailEntrySerializer(read_only=True, source = 'addresstrailentry')
    class Meta(PointEntrySerializer.Meta):
        model = TrailEntry
        fields = ('title', 'coordinates', 'description', 'length', 'difficulty', 'address')


class OpeningHoursChurchEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursChurchEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressChurchEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressChurchEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class ChurchEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursChurchEntrySerializer(read_only=True, source = 'openinghourschurchentry')
    address = AddressChurchEntrySerializer(read_only=True, source = 'addresschurchentry')
    class Meta(PointEntrySerializer.Meta):
        model = ChurchEntry
        fields = ('title', 'coordinates', 'buildingyear', 'denomination', 'openinghours', 'address')


class AddressAccommodationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressAccommodationEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class AccommodationEntrySerializer(PointEntrySerializer):
    address = AddressAccommodationEntrySerializer(read_only=True, source = 'addressaccommodationentry')
    class Meta(PointEntrySerializer.Meta):
        model = AccommodationEntry
        fields = ('title', 'coordinates', 'description', 'address')


# Category Traffic
class OpeningHoursParkingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursParkingEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class ParkingEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursParkingEntrySerializer(read_only=True, source = 'openinghoursparkingentry')
    class Meta(PointEntrySerializer.Meta):
        model = ParkingEntry
        fields = ('title', 'coordinates', 'openinghours', 'no_places')


# Category Trash
class OpeningHoursGlassEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursGlassEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressGlassEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressGlassEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class GlassEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursGlassEntrySerializer(read_only=True, source = 'openinghoursglassentry')
    address = AddressGlassEntrySerializer(read_only=True, source = 'addressglassentry')
    class Meta(PointEntrySerializer.Meta):
        model = GlassEntry
        fields = ('title', 'coordinates', 'description', 'openinghours', 'address')

class OpeningHoursClothingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursClothingEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressClothingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressClothingEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class ClothingEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursClothingEntrySerializer(read_only=True, source = 'openinghoursclothingentry')
    address = AddressClothingEntrySerializer(read_only=True, source = 'addressclothingentry')
    class Meta(PointEntrySerializer.Meta):
        model = ClothingEntry
        fields = ('title', 'coordinates', 'description', 'openinghours', 'address')

class OpeningHoursBatteryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursBatteryEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressBatteryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressBatteryEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class BatteryEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursBatteryEntrySerializer(read_only=True, source = 'openinghoursbatteryentry')
    address = AddressBatteryEntrySerializer(read_only=True, source = 'addressbatteryentry')
    class Meta(PointEntrySerializer.Meta):
        model = BatteryEntry
        fields = ('title', 'coordinates', 'openinghours', 'address')

class OpeningHoursIlluminantEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursIlluminantEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressIlluminantEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressIlluminantEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class IlluminantEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursIlluminantEntrySerializer(read_only=True, source = 'openinghoursilluminantentry')
    address = AddressIlluminantEntrySerializer(read_only=True, source = 'addressilluminantentry')
    class Meta(PointEntrySerializer.Meta):
        model = IlluminantEntry
        fields = ('title', 'coordinates', 'openinghours', 'address')

class OpeningHoursElectroEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursElectroEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressElectroEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressElectroEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class ElectroEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursElectroEntrySerializer(read_only=True, source = 'openinghourselectroentry')
    address = AddressElectroEntrySerializer(read_only=True, source = 'addresselectroentry')
    class Meta(PointEntrySerializer.Meta):
        model = ElectroEntry
        fields = ('title', 'coordinates', 'openinghours', 'address')

class OpeningHoursRecyclingcentreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHoursRecyclingcentreEntry
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
class AddressRecyclingcentreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressRecyclingcentreEntry
        fields = ['street', 'housenumber', 'zipcode', 'city']
class RecyclingcentreEntrySerializer(PointEntrySerializer):
    openinghours = OpeningHoursRecyclingcentreEntrySerializer(read_only=True, source = 'openinghoursrecyclingcentreentry')
    address = AddressRecyclingcentreEntrySerializer(read_only=True, source = 'addressrecyclingcentreentry')
    class Meta(PointEntrySerializer.Meta):
        model = RecyclingcentreEntry
        fields = ('title', 'coordinates', 'description', 'openinghours', 'address')
