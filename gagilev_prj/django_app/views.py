from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower
from .models import *

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    sort_by = request.GET.get('sort', '')
    search_query = request.GET.get('search', '').strip()
    
    trainers = Trainer.objects.all()
    
    if search_query:
        trainers = trainers.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    if sort_by == 'first_name':
        trainers = trainers.order_by(Lower('first_name'))
    else:
        trainers = trainers.order_by('last_name', 'first_name')

    posttt = Position.objects.all()[:7]

    context = {
        'trainerrr': trainers,
        'posttt': posttt,
        'current_sort': sort_by,
        'search_query': search_query,
    }

    return render(request, 'page3.html', context)

def page4(request):
    return render(request, 'page4.html')

def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainings = Training.objects.filter(trainer_id=trainer)
    clients = Client.objects.filter(training__trainer_id=trainer).distinct()
    
    return render(request, 'trainer_detail.html', {
        'trainer': trainer,
        'trainings': trainings,
        'clients': clients,
    })

def search_trainers(request):
    search_query = request.GET.get('search', '').strip()
    
    if not search_query:
        return redirect('staff')
    
    trainers = Trainer.objects.filter(
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query)
    )
    
    if trainers.count() == 1:
        return redirect('trainer_detail', trainer_id=trainers.first().id)
    
    return render(request, 'page3.html', {
        'trainerrr': trainers,
        'posttt': Position.objects.all()[:7],
        'current_sort': '',
        'search_query': search_query,
    })
