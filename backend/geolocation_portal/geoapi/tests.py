from django import test
import unittest
# tests that rely on database access have to inherit from django.test.TestCase!

from .subcategory_response import SubcategoryResponse

class Mock(): # allows dynamic assignment of values
    pass

class SubcategoryResponseUnitTests(unittest.TestCase):

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

from geomodels.models import Subcategory
from category_trash.models import GlassEntry, OpeningHoursGlassEntry
from django.contrib.gis.geos import Point
from datetime import time
import pdb
class SubcategoryResponseIntegrationTests(test.TestCase):
    fixtures = ['geomodels/fixtures/initial_data.yaml']

    @staticmethod
    def get_entry_of_response_data_via_title(response_data, title):
        for response_entry in response_data['features']['properties']:
            pdb.set_trace()
            breakpoint()
            if response_entry['title'] == title:
                return response_entry

        raise Exception(f'Entry with title: {title} should be present in SubcategoryResponse but was not found in response.data: {response_data}')

    def test_new_glass_entry_included_in_response(self):
        test_title = '###test###'
        test_coordinates = Point(5,23)

        glass_entry = GlassEntry.objects.create(
            title = test_title,
            coordinates = test_coordinates,
        )

        opening_hours = OpeningHoursGlassEntry.objects.create(
            monday = [ time(hour = 8, minute = 42), time(hour = 17, minute = 59) ],
            tuesday = None,
            wednesday = [time(hour = 0, minute = 1)],
            thursday = None,
            friday = None,
            saturday = None,
            sunday = None,
            glass_entry  = glass_entry
        )

        glass_subcategory = Subcategory.objects.get(title__iexact = 'glassmüll')
        response = SubcategoryResponse(glass_subcategory).get_response()

        response_entry = self.get_entry_of_response_data_via_title(response.data, test_title)

        self.assertEqual(response_entry['openingHours'], test_opening_hours)

        response_point = Point(response_entry['coordinates']['coordinates']) # reponse_entry contains a GeoJsonDict for the coordinates
        self.assertEqual(
            response_point.geojson,
            test_coordinates.geojson # the saved entry in the db automatically gets a SRID, so they are not equal any more, so we have to compare the simple geojson coordinates
        )
