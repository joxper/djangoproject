import random
from django.shortcuts import render
from django.http import HttpResponse

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


def about(request):
	context = {

		}
	return render(request, "about.html", context )