from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def bienvenido(request):
    return HttpResponse('Hola Mundo !')

def index(request):
    html = '<h1>Hola Mundo - Index</h1>'
    return HttpResponse(html)

def notFound(request):
    if True:
        return HttpResponseNotFound
    else:
        html = '<h3> todo ok </h3>'
        return HttpResponse(html)