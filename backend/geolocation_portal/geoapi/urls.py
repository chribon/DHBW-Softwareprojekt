from .views import CategoryView, SubcategoryView
from rest_framework import routers

class MosbachOpenDataAPIView(routers.APIRootView):
    """
    Es wird unterschieden zwischen den beiden Einstiegen 'api/categories/' und 'api/subcategories/'. Diese ermöglichen die Abfrage einer Liste aller Hauptkategorien, sowie aller Unterkategorien.

    Auf jeder Seite gibt es die Möglichkeit, die Daten über den 'GET' Button auch direkt im 'json'-Format abzurufen.
    """
    pass

class DokuDefaultRouter(routers.DefaultRouter):
    APIRootView = MosbachOpenDataAPIView

router = DokuDefaultRouter()
router.register(r'categories', CategoryView, 'categories')
router.register(r'subcategories', SubcategoryView, 'subcategories')
