from django.shortcuts import render
from geomodels.models import Category, Subcategory, Entry
from .serializers import CategorySerializer, SubcategorySerializer, EntrySerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
#from django.http import HttpResponse, JsonResponse
from rest_framework import status


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

        serializer = SubcategorySerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)



# /subcategories/ --> aktuell nicht verfügbar, nur bei class SubcategoryView(viewsets.ModelViewSet):
# /subcategories/1/
# /subcategories/1/entries/
class SubcategoryView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SubcategorySerializer
    http_method_names = ['get']
    queryset = Subcategory.objects.all()

    @action(methods = ['get'], detail = True, renderer_classes = [renderers.StaticHTMLRenderer], url_path = 'entries')
    def entries(self, request, *args, **kwargs):
        queryset = Entry.objects.filter(id_subcategory = self.kwargs.get('pk'))
        
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        
        serializer = EntrySerializer(queryset, many = True)
        return JsonResponse(serializer.data, safe = False)



# /entries/ --> aktuell nicht verfügbar, nur bei class EntryView(viewsets.ModelViewSet):
# /entries/1/
class EntryView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = EntrySerializer
    http_method_names = ['get']
#    queryset = Entry.objects.all()
