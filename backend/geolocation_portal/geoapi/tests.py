from django import test
import unittest
# tests that rely on database access have to inherit from django.test.TestCase!

from .subcategory_response import SubcategoryResponse

class Mock(): # allows dynamic assignment of values
    pass

class SubcategoryResponseTest(unittest.TestCase):

    def test_none_subcategory_raise_value_error(self):
        with self.assertRaises(ValueError):
            SubcategoryResponse(None)

    def test_subcategory_without_mapping_raises_value_error(self):
        subcategory = Mock()
        subcategory.entry_types = "XXnovalueXX"
        subcategory.title = ""

        with self.assertRaises(ValueError):
            SubcategoryResponse(subcategory)
