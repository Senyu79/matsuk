from django.urls import path
from .views import page1, page2, page3, page4, trainer_search

urlpatterns = [
    path('', page1, name=''),
    path('Subscription', page2, name='subscription'),
    path('Staff', page3, name='staff'),
    path('Timetable', page4, name='timetable'),
    path('search/', trainer_search, name='trainer_search'),  # это имя не используется в main.html
]
