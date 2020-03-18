from django.conf.urls import url
from .views import search, cat_search


urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^heelo/$', cat_search, name='cat_search')
]
