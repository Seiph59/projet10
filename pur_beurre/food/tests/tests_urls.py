from django.test import Client, TestCase
from django.urls import resolve, reverse
from food.views import ResearchView, food_page

class FoodTests(TestCase):

    def test_url_resolve_to_result_page_view(self):
        found = resolve('/results/')
        self.assertEquals(found.func.view_class, ResearchView)

    def test_url_resolve_to_food_page_view(self):
        url = reverse('food:food_detail', args=['22'])
        self.assertEquals(resolve(url).func, food_page)