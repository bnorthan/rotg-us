from django.http import HttpResponse
from django.shortcuts import render
from .models import Runner
from .models import Race
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    l_runners=Runner.objects.all()
    context= {'l_runners':l_runners}
    return render(request, 'results/index.html', context)

def detail(request, runner_id):
    return HttpResponse("This is runner: %s." % runner_id)

def results(request, runner_id):
    response="You are looking at results of runner %s"
    return HttpResponse(response%runner_id)

def addresult(request, runner_id):
    return HttpResponse("you are adding result for runner %s."%runner_id)

def races(request):
    races=Race.objects.all()
    return render(request, 'races/index.html', {'l_races':races})

def race(request, race_id):
    race=Race.objects.get(pk=race_id)
    return render(request, 'race/index.html', {'l_race':race})







