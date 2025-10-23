from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import index, pag1

urlpatterns = [
    path('', pag1),
]

urlpatterns = [
    path('', index),
]