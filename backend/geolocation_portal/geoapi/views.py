from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from geomodels.models import Category, Subcategory, Entry
from .serializers import CategorySerializer, SubcategorySerializer

from .subcategory_response import SubcategoryResponse

# /categories/
# /categories/1/
# /categories/1/subcategories/
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ['get']
    queryset = Category.objects.all()

    @action(methods = ['get'], detail = True,  url_path = 'subcategories')
    def subcategories(self, request, pk, *args, **kwargs):
        queryset = Subcategory.objects.select_related().filter(id_category = pk)

        if queryset:
            serializer = SubcategorySerializer(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        raise Http404()

# /subcategories/ --> aktuell nicht verfügbar, nur bei class SubcategoryView(viewsets.ModelViewSet):
# /subcategories/1/
# /subcategories/1/entries/
class SubcategoryView(viewsets.ModelViewSet): #mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SubcategorySerializer
    http_method_names = ['get']
    queryset = Subcategory.objects.all()

    @action(methods = ['get'], detail = True, url_path = 'entries')
    def entries(self, request, pk, *args, **kwargs):
        # we have to dynamicaly use the right queryset and serializer
        queryset = Subcategory.objects.filter(id = pk)

        if not queryset:
            raise Http404()

        subcategory = queryset[0]

        return SubcategoryResponse(subcategory).get_response()


# /entries/ --> aktuell nicht verfügbar, nur bei class EntryView(viewsets.ModelViewSet):
# /entries/1/
class EntryView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get']
