""" File dedicated for urls in food application """
from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('results/', views.get, name='result_page'),
    path('food/<int:food_id>/', views.food_page, name='food_detail'),
    path('ajax/', views.favorite, name='favorite'),
    path('myfoods/', views.my_foods, name='foods_saved')
]
