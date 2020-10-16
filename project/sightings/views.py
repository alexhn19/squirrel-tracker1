from django.http import HttpResponse
from django.shortcuts import render

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
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context ={
            'form':form,
        }
    return render(request,'sightings/add.html',context)

def update_squirrel(request, unique_squirrel_ID):
    squirrel= Squirrel.objects.get(unique_squirrel_ID = unique_squirrel_ID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'sightings/update.html', context)



def get_stats(request):
    Chasing_count = 0
    Eating_count = 0
    Running_count = 0
    Foraging_count = 0
    Climbing_count = 0
    length = 0
    for i in Squirrel.objects.all():
        if i.Chasing == True:
            Chasing_count += 1
        if i.Eating == True:
            Eating_count += 1
        if i.Climbing== True:
            Climbing_count += 1
        if i.Running == True:
            Running_count += 1
        if i.Foraging == True:
            Foraging_count += 1
        length += 1
    running_percent='{:.2%}'.format(Running_count/length)
    chasing_percent='{:.2%}'.format(Chasing_count/length)
    eating_percent='{:.2%}'.format(Eating_count/length)
    foraging_percent='{:.2%}'.format(Foraging_count/length)
    climbing_percent='{:.2%}'.format(Climbing_count/length)
    context = {
            'running_percent':running_percent,
            'eating_percent':eating_percent,
            'foraging_percent':foraging_percent,
            'climbing_percent':climbing_percent,
            'chasing_percent':chasing_percent,
            }
    return render(request, 'sightings/stats.html', context)
