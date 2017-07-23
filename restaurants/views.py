import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

def home(request):
#	return HttpResponse("jello")
	num = random.randint(0, 100000000)
	list = [num, random.randint(0, 100000000), random.randint(0,1000000)]
	context = {
		"html_var": "false",
		"num": num,
		"list": list
		}
	return render(request, "home.html", context )

class HomeView(TemplateView):

	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		num = random.randint(0, 100000000)
		list = [
			num,
			random.randint(0, 100000000),
			random.randint(0,1000000)
		]
		context = {
			"html_var": "false",
			"num": num,
			"list": list
		}
		return context

def other(request):
	context = {

		}
	return render(request, "other.html", context )

class AboutView(View):
	def get(self, request, *args, **kwargs):
		print(kwargs)
		context = {}
		return render(request, "about.html", context)

class AboutTemplateView(TemplateView):
	template_name = 'about.html'

