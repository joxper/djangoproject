import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

# Create your views here.

def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():		
		form.save()
		return HttpResponseRedirect("/restaurants")
	if form.errors:
		print(form.errors)
		errors = form.errors

	template_name =	'restaurants/form.html'
	context = {"form": form, "errors":errors}
	return render(request, template_name, context)

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):

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

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all() #.filter(category__iexact='asian')

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
	# 	return obj

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name =	'restaurants/form.html'
	success_url = "/restaurants"