from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Squirrel
from .forms import SquirrelForm


def index(request):
    return render(request, 'sightings/index.html', {})

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings,
        }
    return render(request, 'sightings/map.html', context)

def sighting(request):
    squirrel = Squirrel.objects.all()
    context = {
            'squirrels': squirrel,
        }
    return render(request, 'sightings/sightings.html',context)

def add_squirrel(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm()
    context ={
            'form':form,
        }
    return render(request,'sightings/add.html',context)

def update_squirrel(request, unique_squirrel_id):
    squirrel= Squirrel.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'sightings/add.html', context)



def get_stats(request):
    chasing_count = 0
    eating_count = 0
    running_count = 0
    foraging_count = 0
    climbing_count = 0
    length = 0
    for i in Squirrel.objects.all():
        if i.chasing == True:
            chasing_count += 1
        if i.eating == True:
            eating_count += 1
        if i.climbing== True:
            climbing_count += 1
        if i.running == True:
            running_count += 1
        if i.foraging == True:
            foraging_count += 1
        length += 1
    running_percent='{:.2%}'.format(running_count/length)
    chasing_percent='{:.2%}'.format(chasing_count/length)
    eating_percent='{:.2%}'.format(eating_count/length)
    foraging_percent='{:.2%}'.format(foraging_count/length)
    climbing_percent='{:.2%}'.format(climbing_count/length)
    context = {
            'running_percent':running_percent,
            'eating_percent':eating_percent,
            'foraging_percent':foraging_percent,
            'climbing_percent':climbing_percent,
            'chasing_percent':chasing_percent,
            }
    return render(request, 'sightings/stats.html', context)
