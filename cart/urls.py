from django.conf.urls import url
from .views import view_cart, cart_add, change_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', cart_add, name='cart_add'),
    url(r'^change/(?P<id>\d+)', change_cart, name='change_cart'),
]
