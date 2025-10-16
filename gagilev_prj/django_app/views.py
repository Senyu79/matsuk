from django.shortcuts import render, HttpResponse
from .models import *

def index(request):

    client = Client.first_name

    return render(request, 'main.html', {'client': client})