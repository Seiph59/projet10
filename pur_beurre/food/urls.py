from django.urls import path
from django.contrib.auth import views as auth_views
from food.views import ResearchView

from . import views


app_name = 'food'
urlpatterns = [
    path('results/', ResearchView.as_view(), name='resultpage'),
    path('food/<int:food_id>/', views.food_page, name='foodpage'),
]