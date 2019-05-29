""" Test file for urls in food application """
from django.test import TestCase
from django.urls import resolve, reverse
from food.views import ResearchView, food_page


class FoodTests(TestCase):
    """ test urls for the food application """

    def test_url_resolve_to_result_page_view(self):
        """ test url for the result_page """
        found = resolve('/results/')
        self.assertEqual(found.func.view_class, ResearchView)

    def test_url_resolve_to_food_page_view(self):
        """ test url for the food page """
        url = reverse('food:food_detail', args=['22'])
        self.assertEqual(resolve(url).func, food_page)
