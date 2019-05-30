""" Views associated to the Welcome application """
from django.shortcuts import render, redirect, reverse
from .forms import SearchForm


def index(request):
    """ Method associated to the homepage """
    template_name = 'welcome/index.html'
    form = SearchForm()
    return render(request, template_name, {'form': form})


def legal(request):
    """ Method associated to the legal_notice page """
    return render(request, 'welcome/legalnotice.html')

def contact(request):
    """ Method to go directly on contact section"""
    return redirect(reverse('welcome:home') + '#contact')
