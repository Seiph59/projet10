from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'accounts/create_account.html')

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte de {username} a été créée')
            return redirect('http://127.0.0.1:8000/')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/create_account.html', {'form': form})

@login_required
def my_account(request):
    return render(request, 'accounts/my_account.html')
