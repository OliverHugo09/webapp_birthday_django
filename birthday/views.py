from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'ejercicio/calcular.html')

def calcular_edad(request):
    day = int(request.GET.get('day',0))
    mounth = int(request.GET.get('mounth',0))
    year = int(request.GET.get('year',0))
    dayact = int(request.GET.get('dayact',0))
    mounthact = int(request.GET.get('mounthact',0))
    yearact = int(request.GET.get('yearact',0))
    age = ''
    
    if mounthact > mounth:
        age = yearact - year
    elif mounthact == mounth and dayact < day:
        age = yearact - year -1
    else:
        age = yearact - year
    return render(request,'ejercicio/mostrar.html',{'edad':age})