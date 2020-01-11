from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_title = "GeoMosbach Datenpflege" # text is entered at the end of the <title>-content
    site_header = "GeoMosbach Datenpflege" # <h1> at each page and login form
    index_title = "Willkommen auf dem GeoMosbach Datenpflegeportal" # text at admin index page

admin_site = CustomAdminSite()
