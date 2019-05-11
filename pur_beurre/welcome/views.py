from django.shortcuts import render


def index(request):
    template_name = 'welcome/index.html'
    return render(request, template_name)

def product_research(request):
    if request.method == 'POST':
        product_name = form.get('research')
        print(product_name)
# Create your views here.
