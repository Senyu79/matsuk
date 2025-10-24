from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import page1, page2

urlpatterns = [
    path('', page1),
    path('Subscription', page2)
]
