import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import RestaurantLocation

# Create your views here.


def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset
	