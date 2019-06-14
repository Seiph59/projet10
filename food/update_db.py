import datetime
from food.openff_api import Database, api_research_off
from food.models import Food, Category

db = Database()

def update():
    """ Class method, which update the Database """
    data = api_research_off()
    for product in data['products']:
        product_name = db.get_product_name(product)
        nutriscore = db.get_nutriscore(product)
        if nutriscore is None:
            continue
        nutritional_list = db.get_nutritional_mark_for_100g(product)
        if nutritional_list is None:
            continue
        url_page = db.get_url_page(product)
        url_image = db.get_url_image(product)
        if(not url_image):
            continue
        id_product = db.get_id_product(product)
        if(not id_product) :
            continue
        id_food = db.get_id_product(product)
        food_search = Food.objects.filter(openff_id=id_food)
        if food_search.exists():
            food_date = food_search.first().last_modified
            last_modified_date = db.get_last_modified(product)
            if last_modified_date != food_date:
                food_search = Food.objects.get(openff_id=id_food)
                Food.objects.filter(openff_id=id_food).update(name=product_name,
                                                              nutriscore=nutriscore,
                                                              url=url_page,
                                                              url_picture=url_image,
                                                              fat_100g=nutritional_list[0],
                                                              saturated_fat_100g=nutritional_list[2],
                                                              sugars_100g=nutritional_list[4],
                                                              salt_100g=nutritional_list[6],
                                                              fat_level=nutritional_list[1],
                                                              salt_level=nutritional_list[7],
                                                              saturated_fat_level=nutritional_list[3],
                                                              sugars_level=nutritional_list[5],
                                                              last_modified=last_modified_date)
                db.get_and_insert_categories_in_db(product, food_search)
                food_search.refresh_from_db()
            else:
                continue
        else:
            food = Food(name=product_name,
                        nutriscore=nutriscore,
                        url=url_page,
                        url_picture=url_image,
                        fat_100g=nutritional_list[0],
                        saturated_fat_100g=nutritional_list[2],
                        sugars_100g=nutritional_list[4],
                        salt_100g=nutritional_list[6],
                        fat_level=nutritional_list[1],
                        salt_level=nutritional_list[7],
                        saturated_fat_level=nutritional_list[3],
                        sugars_level=nutritional_list[5],
                        last_modified=last_modified_date,
                        openff_id=id_product)
            food.save()
            db.get_and_insert_categories_in_db(product, food)
