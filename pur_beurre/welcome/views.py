from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import SearchForm
from food.models import Food

class HomePageView(TemplateView):
    template_name = 'welcome/index.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})
