from django.shortcuts import render
from cgitb import html
from django.http import HttpResponse
# Create your views here.

def bienvenida(request):
    saludo = {
        'mensaje' : 'Bienvenido !'
    }
    return render(request, 'index.html', saludo)

def listado(request):

    dicc = {
        'Gatos': [
            {'nombre': 'Figaro', 'raza' : 'persa', 'edad' : 4, 'genero' : 'macho', 'color' : 'blanco y negro', 'peso' : '4kl'},
            {'nombre': 'Luna', 'raza' : 'callejero', 'edad' : 4, 'genero' : 'hembra', 'color' : 'tricolor', 'peso' : '4kl'},
            {'nombre': 'Candy', 'raza' : 'persa', 'edad' : 4, 'genero' : 'hembra', 'color' : 'naranja', 'peso' : '4kl'},
            {'nombre': 'Tom', 'raza' : 'Callejero', 'edad' : 4, 'genero' : 'macho', 'color' : 'plomo', 'peso' : '4kl'},
            ]
        }
    return render(request, 'list.html', dicc)


def agregar(request):
    return render(
        request,
        'wena.html'
    )