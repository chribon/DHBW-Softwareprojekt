from django.test import TestCase
from .models import (
    Category,
    Subcategory,
)

class IntegrationTests(TestCase):
    fixtures = ['geomodels/fixtures/initial_data.yaml']

    def test_number_of_categories_greater_equal_six(self):
        self.assertGreaterEqual(
            Category.objects.count(),
            6
        )

    def test_number_of_subcategories_greater_equal_seventeen(self):
        self.assertGreaterEqual(
            Subcategory.objects.count(),
            17
        )

