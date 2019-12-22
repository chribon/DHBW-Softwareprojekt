from geomodels.models import Subcategory
from .serializers import (
    GlassTrashEntrySerializer,
)

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class SubcategoryResponse():

    mapping = {
        "glasstrash": {
            "get_queryset": lambda sc: sc.glasstrashentry_set.all(),
            "serializer": lambda qs: GlassTrashEntrySerializer(qs, many = True)
        },
        # define new entry_types here
    }

    def __init__(self, subcategory):
        self.subcategory = subcategory

    def __get_queryset(self):
        try:
            self.queryset = self.mapping[self.subcategory.entry_types]["get_queryset"](self.subcategory)
        except KeyError:
            raise Exception("There is no mapping defined for the specified subcategory.entry_types\nError for subcategory: " + str(self.subcategory.title) + ", and entry_types: " + str(self.subcategory.entry_types))

    def get_response(self):
        self.__get_queryset()

        serializer = self.mapping[self.subcategory.entry_types]["serializer"](self.queryset)

        return Response(serializer.data, status = status.HTTP_200_OK)
