from .views import CategoryView, SubcategoryView
from rest_framework import routers

class MosbachOpenDataAPIView(routers.APIRootView):
    """
    API steht für "Application Programming Interface” und stellt eine programmierbare Schnittstelle für GeoMosbach dar. Hier können Sie alle Daten, die durch die Stadt Mosbach dargestellt werden, über eine auf dem http-Protokoll basierende Schnittstelle zur Nutzung für Ihre Programme abrufen. Die Dokumentation zur Anwendung der API ist jeweils bei den einzelnen API-Einstiegen zu finden.

    Es wird unterschieden zwischen den beiden Einstiegen **[Hauptkategorien][refcategories]** und **[Unterkategorien][refsubcategories]**. Diese ermöglichen die Abfrage einer Liste aller Hauptkategorien, sowie aller Unterkategorien.

    Über den Einstieg [Hauptkategorien][refcategories] können alle Haupt- und deren entsprechende Unterkategorien abgerufen werden. Der Einstieg [Unterkategorien][refsubcategories] ermöglicht den Zugriff auf eine Liste der Einträge pro Unterkategorie. Diese Einträge sind nach dem [GeoJSON][refgeojson] Standard aufgebaut.

    Auf jeder Seite gibt es die Möglichkeit, die Daten über den 'GET' Button auch direkt im 'json'-Format abzurufen.

    Die GeoMosbach API ist kostenfrei nutzbar und bietet allen Interessierten die Möglichkeit, die bereitgestellten Daten in eigene Anwendungen einzubinden und zu verarbeiten.
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
