from geomodels.models import Subcategory
from .serializers import (
    GroundvalueEntrySerializer,
    BuildingareaEntrySerializer,
    PlaygroundEntrySerializer,
    SchoolEntrySerializer,

    ViewpointEntrySerializer,

    SportscentreEntrySerializer,

    MonumentEntrySerializer,
    TrailEntrySerializer,
    ChurchEntrySerializer,
    AccommodationEntrySerializer,

    ParkingEntrySerializer,

    GlassEntrySerializer,
    ClothingEntrySerializer,
    BatteryEntrySerializer,
    IlluminantEntrySerializer,
    ElectroEntrySerializer,
    RecyclingcentreEntrySerializer,
)

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class SubcategoryResponse():

    mapping = {
        "groundvalueliving": {
            "get_queryset": lambda sc: sc.groundvalueentry_set.all(),
            "serializer": lambda qs: GroundvalueEntrySerializer(qs, many = True)
        },
        "buildingarealiving": {
            "get_queryset": lambda sc: sc.buildingareaentry_set.all(),
            "serializer": lambda qs: BuildingareaEntrySerializer(qs, many = True)
        },
        "playgroundliving": {
            "get_queryset": lambda sc: sc.playgroundentry_set.all(),
            "serializer": lambda qs: PlaygroundEntrySerializer(qs, many = True)
        },
        "schoolliving": {
            "get_queryset": lambda sc: sc.schoolentry_set.all(),
            "serializer": lambda qs: SchoolEntrySerializer(qs, many = True)
        },

        "viewpointnature": {
            "get_queryset": lambda sc: sc.viewpointentry_set.all(),
            "serializer": lambda qs: ViewpointEntrySerializer(qs, many = True)
        },

        "sportscentresparetime": {
            "get_queryset": lambda sc: sc.sportscentreentry_set.all(),
            "serializer": lambda qs: SportscentreEntrySerializer(qs, many = True)
        },

        "monumenttourism": {
            "get_queryset": lambda sc: sc.monumententry_set.all(),
            "serializer": lambda qs: MonumentEntrySerializer(qs, many = True)
        },
        "trailtourism": {
            "get_queryset": lambda sc: sc.trailentry_set.all(),
            "serializer": lambda qs: TrailEntrySerializer(qs, many = True)
        },
        "churchtourism": {
            "get_queryset": lambda sc: sc.churchentry_set.all(),
            "serializer": lambda qs: ChurchEntrySerializer(qs, many = True)
        },
        "accommodationtourism": {
            "get_queryset": lambda sc: sc.accommodationentry_set.all(),
            "serializer": lambda qs: AccommodationEntrySerializer(qs, many = True)
        },

        "parkingtraffic": {
            "get_queryset": lambda sc: sc.parkingentry_set.all(),
            "serializer": lambda qs: ParkingEntrySerializer(qs, many = True)
        },

        "glasstrash": {
            "get_queryset": lambda sc: sc.glassentry_set.all(),
            "serializer": lambda qs: GlassEntrySerializer(qs, many = True)
        },
        "clothingtrash": {
            "get_queryset": lambda sc: sc.clothingentry_set.all(),
            "serializer": lambda qs: ClothingEntrySerializer(qs, many = True)
        },
        "batterytrash": {
            "get_queryset": lambda sc: sc.batteryentry_set.all(),
            "serializer": lambda qs: BatteryEntrySerializer(qs, many = True)
        },
        "illuminanttrash": {
            "get_queryset": lambda sc: sc.illuminantentry_set.all(),
            "serializer": lambda qs: IlluminantEntrySerializer(qs, many = True)
        },
        "electrotrash": {
            "get_queryset": lambda sc: sc.electroentry_set.all(),
            "serializer": lambda qs: ElectroEntrySerializer(qs, many = True)
        },
        "recyclingcentretrash": {
            "get_queryset": lambda sc: sc.recyclingcentreentry_set.all(),
            "serializer": lambda qs: RecyclingcentreEntrySerializer(qs, many = True)
        },
        # define new entry_types here
    }

    def __init__(self, subcategory):
        if subcategory is None:
            raise ValueError("Subcategory can't be None")

        self.subcategory = subcategory

    def __get_queryset(self):
        try:
            self.queryset = self.mapping[self.subcategory.entry_types]["get_queryset"](self.subcategory)
        except KeyError:
            raise ValueError("There is no mapping defined for the specified subcategory.entry_types\nError for subcategory: " + str(self.subcategory.title) + ", and entry_types: " + str(self.subcategory.entry_types))

    def get_response(self):
        self.__get_queryset()

        serializer = self.mapping[self.subcategory.entry_types]["serializer"](self.queryset)

        return Response(serializer.data, status = status.HTTP_200_OK)
