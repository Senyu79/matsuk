from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, redirect
from .models import *
from django.db.models import Q

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

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainings = Training.objects.filter(trainer_id=trainer)
    clients = Client.objects.filter(training__trainer_id=trainer).distinct()
    
    return render(request, 'search.html', {
        'trainer': trainer,
        'trainings': trainings,
        'clients': clients,
    })

def trainer_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Ищем всех тренеров по запросу
        trainers = Trainer.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(father_name__icontains=query)
        )
        
        return render(request, 'trainer_search_results.html', {
            'trainers': trainers,
            'query': query,
            'results_count': trainers.count()
        })