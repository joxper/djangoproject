from django.conf.urls import url


from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    )

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
#    url(r'^restaurants/create/$', restaurant_createview),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),

#    url(r'^(?P<slug>[\w-]+)/update/$', RestaurantUpdateView.as_view(), name='update'),
#    url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'), #pk default
]
