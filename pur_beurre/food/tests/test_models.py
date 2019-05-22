from food.models import Food
from django.test import TestCase
from datetime import datetime

class FoodModelTest(TestCase):
    first_food = Food(name="test",
                             nutriscore="a",
                             url="www.off.com",
                             url_picture="www.off.com",
                             fat_100g=0.2,
                             saturated_fat_100g=0.1,
                             sugars_100g=0.7,
                             salt_100g=0.5,
                             fat_level="low",
                             salt_level="low",
                             saturated_fat_level="medium",
                             sugars_level="high",
                             last_modified=datetime(2015, 6, 15),
                             openff_id= 125452)

    def test_saving_and_retrieving_food(self):

        self.first_food.save()

        saved_food = Food.objects.all()
        self.assertEqual (saved_food.count(), 1)