""" File which generate the database from
OpenfoodFacts API """
import datetime
import requests
from food.models import Food, Categorie


def api_research_off():
    """ Launch the API Request to OpenFoodFacts"""

    criteria_api = {
        "search_terms2": 'aliment',
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "sort_by": "unique_scans_n",
        "page_size": 1000,
        "json": 1,
        "action": "process",
    }

    request = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
                           params=criteria_api)
    data = request.json()
    return data


class Database:
    """ Class which allows to manage the database commands.
    You can modify each class method at your convenience """
    def __init__(self):
        pass

    def get_product_name(self, product):
        """ Get product name from API, if product_name_fr
        doesn't exist, get the product_name"""
        product_name = product.get('product_name_fr')
        if product_name is None:
            product_name = product['product_name']
        return product_name

    def get_and_insert_categories_in_db(self, product, food):
        """Get categories from the product and insert directly in db """
        categories = product.get('categories')
        list_categories = categories.split(",")
        for categorie in list_categories:
            print(categorie)
            categorie, _ = Categorie.objects.get_or_create(name=categorie)
            food.categories.add(categorie)

    def get_nutriscore(self, product):
        """ Get the nutriscore, if it doesn't exist
        return None """
        return product.get('nutrition_grade_fr')

    def get_url_page(self, product):
        """ Get the url of the product """
        return product.get('url')

    def get_url_image(self, product):
        """ Get the url image """
        return product.get('image_front_url')

    def get_nutritional_mark_for_100g(self, product):
        """ Get the nutritional marks, return None if one the
        variable is None to avoid to implement a incomplete product"""
        fat_100g = product['nutriments'].get('fat_100g')
        saturated_fat_100g = product['nutriments'].get('saturated-fat_100g')
        sugars_100g = product['nutriments'].get('sugars_100g')
        salt_100g = product['nutriments'].get('salt_100g')
        fat_level = product['nutrient_levels'].get('fat')
        saturated_fat_level = product['nutrient_levels'].get('saturated-fat')
        sugars_level = product['nutrient_levels'].get('sugars')
        salt_level = product['nutrient_levels'].get('salt')

        if fat_100g is None or fat_level is None:
            return None
        elif saturated_fat_100g is None or saturated_fat_level is None:
            return None
        elif sugars_100g is None or sugars_level is None:
            return None
        elif salt_100g is None or salt_level is None:
            return None
        else:
            return[fat_100g,
                   fat_level,
                   saturated_fat_100g,
                   saturated_fat_level,
                   sugars_100g,
                   sugars_level,
                   salt_100g,
                   salt_level]

    def get_id_product(self, product):
        """ Get the id_product from the API, pay attention
        that on each method, we receive data from parameter """
        return product.get('id')

    def get_last_modified(self, product):
        """ Get last_modified date to know if the product
        has been updated lastly and convert it"""
        timestamp = product.get('last_modified_t')
        return datetime.date.fromtimestamp(timestamp)

    def populate(self):
        """ Class method, which allows the user to populate the Database """
        data = api_research_off()
        for product in data['products']:
            product_name = self.get_product_name(product)
            nutriscore = self.get_nutriscore(product)
            if nutriscore is None:
                continue
            nutritional_list = self.get_nutritional_mark_for_100g(product)
            if nutritional_list is None:
                continue
            url_page = self.get_url_page(product)
            url_image = self.get_url_image(product)
            if(not url_image):
                continue
            id_product = self.get_id_product(product)
            if(not id_product):
                continue
            last_modified_date = self.get_last_modified(product)
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
            self.get_and_insert_categories_in_db(product, food)
