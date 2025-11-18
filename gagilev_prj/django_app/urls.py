from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import page1, page2, page3, page4, trainer_search, trainer_detail

urlpatterns = [
    path('', page1, name=''),
    path('Subscription', page2, name='subscription'),
    path('Staff', page3, name='staff'),
    path('Timetable', page4, name='timetable'),
    path('trainer/<int:trainer_id>/', trainer_detail, name='trainer_detail'),
    path('search/', trainer_search, name='trainer_search'),
]