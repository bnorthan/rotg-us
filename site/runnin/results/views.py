from django.http import HttpResponse
from django.shortcuts import render
from .models import Member
from .models import Race
from django.shortcuts import get_object_or_404, render

import django_tables2 as tables
from django_tables2 import RequestConfig

# Create your views here.
def index(request):
    l_members=Member.objects.all()
    context= {'l_members':l_members}
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


class SimpleRace(tables.Table):
    first_name=tables.Column()
    last_name=tables.Column()
    time=tables.Column()

    def render_time(self, value):
        return value.strftime('%M:%S')

def race(request, race_id):
    race=SimpleRace(Race.objects.get(pk=race_id).result_set.all())
    #race=Race.objects.get(pk=race_id).result_set.all()

    RequestConfig(request).configure(race)
    
    return render(request, 'race/index.html', {'l_race':race})







