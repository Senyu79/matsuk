from django.shortcuts import render, HttpResponse
from .models import *

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    
    trainerrr = Trainer.objects.all()[:7]
    posttt = Position.objects.all()[:7]

    context = {
        'trainerrr': trainerrr,
        'posttt': posttt,
        }

    return render(request, 'page3.html', context)

def page4(request):
    return render(request, 'page4.html')