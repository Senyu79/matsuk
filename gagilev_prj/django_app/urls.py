from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import page1, page2, page3

urlpatterns = [
    path('', page1, name=''),
    path('Subscription', page2, name='subscription'),
    path('Staff', page3, name='staff')
]
