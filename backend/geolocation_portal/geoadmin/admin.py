from django.contrib.admin import AdminSite
from django.contrib.admin import *

class CustomAdminSite(AdminSite):
    site_title = "GeoMosbach Datenpflege" # text is entered at the end of the <title>-content
    site_header = "GeoMosbach Datenpflege" # <h1> at each page and login form
    index_title = "Willkommen auf dem GeoMosbach Datenpflegeportal" # text at admin index page

    def __init__(self, *args, **kwargs):
        super(CustomAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

admin_site = CustomAdminSite()
