from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'sightings/index.html', {})

def map(request):
    return render(request, 'sightings/map.html', {})
