from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def search(request):
    template = loader.get_template('food/search_page.html')
    if request.GET['search']:
        query = request.GET['search']
        args = ({'query': query})
        return HttpResponse(template.render(args, request))

    elif request.GET['']:
        query = request.GET['']
        args = ({'query': query})
        return HttpResponse(template.render(args, request))
