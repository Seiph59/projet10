from django.shortcuts import render


def index(request):
    template_name = 'welcome/index.html'
    return render(request, template_name)
# Create your views here.
