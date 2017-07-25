from django.conf.urls import url


from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    )

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
#    url(r'^restaurants/create/$', restaurant_createview),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
#    url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'), #pk default
]
