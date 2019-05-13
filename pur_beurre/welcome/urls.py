from django.urls import path

from welcome.views import HomePageView

app_name = 'welcome'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]