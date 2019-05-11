from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    name = models.CharField(max_length=200)

class Food(models.Model):
    name = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField(max_length=250)
    url_picture = models.URLField(max_length=250)
    fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=5, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=5, decimal_places=2)
    fat_level = models.CharField(max_length=10)
    salt_level = models.CharField(max_length=10)
    saturated_fat_level = models.CharField(max_length=10)
    sugars_level = models.CharField(max_length=10)
    last_modified = models.DateField()
    openff_id = models.BigIntegerField()
    categories = models.ManyToManyField(Categorie)

    def get_substitute(self, product_name):
        f = Food.objects.filter(id=product_name)
        categories = f[0].categories.all()
        categorie_id = categories[0].id
        c = Categorie.objects.filter(pk=categorie_id)
        b = c[0].food_set.all().order_by('nutriscore')
        substitute = b[0].name
        return substitute

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_foods = models.ManyToManyField(Food)

# Create your models here.
