""" Views.py dedicated for views , in 'accounts' application """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    """ Method for welcome page """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/create_account.html', {'form': form})


@login_required
def my_account(request):
    """ Method for my_account page"""
    return render(request, 'accounts/my_account.html')
