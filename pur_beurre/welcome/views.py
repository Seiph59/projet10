""" Views associated to the Welcome application """
from django.shortcuts import render
from .forms import SearchForm


def index(request):
    """ Method associated to the homepage """
    template_name = 'welcome/index.html'
    form = SearchForm()
    return render(request, template_name, {'form': form})


def legal(request):
    """ Method associated to the legal_notice page """
    return render(request, 'welcome/legalnotice.html')
