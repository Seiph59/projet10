from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from .models import Food
import json


def food_page(request, food_id):
    article = Food.objects.get(pk=food_id)
    return render(request, 'food/food_details.html', {'article': article})


class ResearchView(View):
    food = Food()
    template_name = 'food/search_page.html'

    def get(self, request):
        query = request.GET.get('search')
        list = self.food.get_substitute(query)
        substitutes_list = list[0]
        paginator = Paginator(substitutes_list, 6)
        page = request.GET.get('page')
        substitutes_list = paginator.get_page(page)
        args = ({'food_search': list[1], 'articles_found': substitutes_list, 'image': list[2],'page': page, 'query': query})
        return render(request, self.template_name, args)


@require_POST
def favorite(request):
    if request.is_ajax():
        food_id = json.loads(request.body.decode('utf-8')).get('id')
        food = Food.objects.get(pk=food_id)
        current_user = request.user
        user = User.objects.get(pk=current_user.id)
        food.favorite_users.add(user.id)
        data = "le produit a été enregistré"
    return HttpResponse(data)

def my_foods(request):
    foods_saved = request.user.favorite_foods.all()
    paginator = Paginator(foods_saved, 6)
    page = request.GET.get('page')
    foods_saved = paginator.get_page(page)
    return render(request, 'food/my_foods.html', {'foods_saved': foods_saved})