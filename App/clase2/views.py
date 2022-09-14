from django.shortcuts import render
from cgitb import html
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def home(request):
    saludo = {
        'mensaje' : 'Hola Mundo !'
    }
    return render(request, 'index.html', saludo)

def listado(request):

    dicc = {
        'personas': [
            {'nombre': 'juanito', 'edad' : 20, 'vocacion' : 'alpinista'},
            {'nombre': 'maria', 'edad' : 35, 'vocacion' : 'alfarero'},
            {'nombre': 'sandoval', 'edad' : 13, 'vocacion' : 'gamer'},
            {'nombre': 'martha', 'edad' : 60, 'vocacion' : 'arthesana'}
            ]
        }

    return render(request, 'personas.html', dicc)