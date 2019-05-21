from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .models import Food



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

