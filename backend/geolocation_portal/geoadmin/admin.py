from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_title = "Mosportal" # text is entered at the end of the <title>-content
    site_header = "Mosportal - Administration" # <h1> at each page and login form
    index_title = "Willkommen in der Mosportal-Administration" # text at admin index page

admin_site = CustomAdminSite()
