from django.db import models

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

# Create your models here.
