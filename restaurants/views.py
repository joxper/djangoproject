import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

# Create your views here.
@login_required()
def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():	
		if request.user.is_authenticated():	
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect("/restaurants/")
		else:
			return HttpResponseRedirect("/login/")
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

class RestaurantListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
			)
		else:
			queryset = RestaurantLocation.objects.filter(owner=self.request.user)
		return queryset

class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user) #.filter(category__iexact='asian')

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
	# 	return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	template_name =	'form.html'
	# success_url = "/restaurants"
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	template_name =	'restaurants/detail-update.html'
	# success_url = "/restaurants"

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = 'Update'
		return context		

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)