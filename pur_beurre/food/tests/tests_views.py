from django.test import TestCase
from food.models import Food
from datetime import datetime

class FoodViewsTest(TestCase):
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

    def test_food_page_template(self):
        self.first_food.save()
        food = Food.objects.all()
        food_id = food[0].id
        response = self.client.get('/food/%d/' % (food_id) )
        self.assertTemplateUsed(response, 'food/food_details.html')

