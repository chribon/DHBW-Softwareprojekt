from django.shortcuts import render
from rest_framework import viewsets
from geomodels.models import Category, Subcategory, Entry
from .serializers import CategorySerializer, SubcategorySerializer, EntrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from django.http import HttpResponse, JsonResponse

# Create your views here.

# /categories/
# /categories/1/
# /categories/1/subcategories/
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ['get']
    queryset = Category.objects.all()

    @action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
    def subcategories(self, request, *args, **kwargs):
        subcats = Subcategory.objects.filter(id_category = 1)
        serializer = SubcategorySerializer(subcats, many = True)
        return JsonResponse(serializer.data, safe = False)



# /subcategories/
# /subcategories/1/
# /subcategories/1/entries/
class SubcategoryView(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer
    http_method_names = ['get']
    queryset = Subcategory.objects.all()

    @action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
    def entries(self, request, *args, **kwargs):
        entrs = Entry.objects.filter(id_subcategory = 1)
        serializer = EntrySerializer(entrs, many = True)
        return JsonResponse(serializer.data, safe = False)



# /entries/
# /entries/1/
class EntryView(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    http_method_names = ['get']
    queryset = Entry.objects.all()