import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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


def other(request):
	context = {

		}
	return render(request, "other.html", context )

class AboutView(View):
	def get(self, request, *args, **kwargs):
		print(kwargs)
		context = {}
		return render(request, "about.html", context)

