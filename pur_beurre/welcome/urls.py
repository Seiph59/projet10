from django.urls import path

from welcome import views

app_name = 'welcome'
urlpatterns = [
    path('', views.index, name='home'),
    path('mentions-legales/', views.legal, name='legalnotice')
]