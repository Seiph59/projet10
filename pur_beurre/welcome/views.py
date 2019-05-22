from django.shortcuts import render, redirect
from .forms import SearchForm
from food.models import Food


def index(request):
    template_name = 'welcome/index.html'
    form = SearchForm()
    return render(request, template_name, {'form': form})
