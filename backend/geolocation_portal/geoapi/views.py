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
    """
    Pro Kategorie können die Details einzeln aufgerufen werden durch '/api/categories/**id**/'. [Hier][cat1] beispielsweise die Verlinkung zur Hauptkategorie 1.

    Der Pfad '/api/categories/**id**/subcategories/' führt zu einer Auflistung aller Unterkategorien der Hauptkategorie (auch erreichbar über den Button 'Extra Actions' auf der Seite der Hauptkategorie-Instanz). [Hier][cat1subcats] beispielsweise die Verlinkung zu den Unterkategorien der Hauptkategorie 1. 
    [cat1]: /api/categories/1/
    [cat1subcats]: /api/categories/1/subcategories/
    """
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

# /subcategories/
# /subcategories/1/
# /subcategories/1/entries/
class SubcategoryView(viewsets.ModelViewSet): 
    """
    Pro Unterkategorie können die Details einzeln aufgerufen werden durch '/api/subcategories/**id**/'. [Hier][subcat1] beispielsweise die Verlinkung zur Unterkategorie 1.

    Der Pfad '/api/subcategories/**id**/entries/' führt zu einer Auflistung aller Einträge der Unterkategorie (auch erreichbar über den Button 'Extra Actions' auf der Seite der Unterkategorie-Instanz). [Hier][subcat1entries] beispielsweise die Verlinkung zu den Einträgen der Unterkategorie 1.
    
    [subcat1]: /api/subcategories/1/
    [subcat1entries]: /api/subcategories/1/entries/
    """
    serializer_class = SubcategorySerializer
    http_method_names = ['get']
    queryset = Subcategory.objects.all()

    @action(methods = ['get'], detail = True, url_path = 'entries')
    def entries(self, request, pk, *args, **kwargs):
        queryset = Subcategory.objects.filter(id = pk)

        if not queryset:
            raise Http404()

        subcategory = queryset[0]

        return SubcategoryResponse(subcategory).get_response()
