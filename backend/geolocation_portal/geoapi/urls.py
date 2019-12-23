from .views import CategoryView, SubcategoryView, EntryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryView, 'api')
router.register(r'subcategories', SubcategoryView, 'api')
# router.register(r'entries', EntryView, 'api')