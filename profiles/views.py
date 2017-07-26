from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from restaurants.models import RestaurantLocation
from menus.models import Item

User = get_user_model()
# Create your views here.
class ProfileDetailView(DetailView):
	queryset = User.objects.filter(is_active=True)
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, **kwargs):
	    context = super(ProfileDetailView, self).get_context_data(**kwargs)
	    user = context['user']
	    query = self.request.GET.get('q')
	    items_exists = Item.objects.filter(user=user).exists()
	    qs = RestaurantLocation.objects.filter(owner=user).search(query)
	    if items_exists and qs.exists():
	    	context['locations'] = qs
	    return context