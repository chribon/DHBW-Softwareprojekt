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


    def test_valid_entry_types_happy_payh(self):
        valid_entry_types = ('groundvalueliving', 'buildingarealiving', 'playgroundliving', 'schoolliving', 'viewpointnature', 'sportscentresparetime', 'monumenttourism', 'trailtourism', 'churchtourism', 'accommodationtourism', 'parkingtraffic', 'glasstrash', 'clothingtrash', 'batterytrash', 'illuminanttrash', 'electrotrash', 'recyclingcentretrash')

        subcategory = Mock()
        subcategory.title = ""

        for entry in valid_entry_types:
            subcategory.entry_types = entry

            try:
                SubcategoryResponse(subcategory)
            except ValueError:
                self.fail("Subcategory.__init__ raised exception for a valid subcagetory.entry_types value.")



