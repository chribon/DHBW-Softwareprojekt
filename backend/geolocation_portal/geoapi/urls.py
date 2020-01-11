from .views import CategoryView, SubcategoryView
from rest_framework import routers

class MosbachOpenDataAPIView(routers.APIRootView):
    """
    Es wird unterschieden zwischen den beiden Einstiegen **[Hauptkategorien][refcategories]** und **[Unterkategorien][refsubcategories]**. Diese ermöglichen die Abfrage einer Liste aller Hauptkategorien, sowie aller Unterkategorien.

    Über den Einstieg [Hauptkategorien][refcategories] können alle Haupt- und deren entsprechende Unterkategorien abgerufen werden. Der Einstieg [Unterkategorien][refsubcategories] ermöglicht den Zugriff auf eine Liste der Einträge pro Unterkategorie. Diese Einträge sind nach dem [GeoJSON][refgeojson] Standard aufgebaut.

    Auf jeder Seite gibt es die Möglichkeit, die Daten über den 'GET' Button auch direkt im 'json'-Format abzurufen.
    [refcategories]: ./categories/
    [refsubcategories]: ./subcategories/
    [refgeojson]: https://geojson.org/
    """
    pass

class DokuDefaultRouter(routers.DefaultRouter):
    APIRootView = MosbachOpenDataAPIView

router = DokuDefaultRouter()
router.register(r'categories', CategoryView, 'categories')
router.register(r'subcategories', SubcategoryView, 'subcategories')
