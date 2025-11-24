from django.urls import path
from .views import page1, page2, page3, page4, trainer_detail, search_trainers

urlpatterns = [
    path('', page1, name=''),
    path('Subscription/', page2, name='subscription'),
    path('Staff/', page3, name='staff'),
    path('Timetable/', page4, name='timetable'),
    path('trainer/<int:trainer_id>/', trainer_detail, name='trainer_detail'),
    path('search/', search_trainers, name='search_trainers'),
]
