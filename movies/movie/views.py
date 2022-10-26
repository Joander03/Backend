from multiprocessing import context
from django.shortcuts import render
from .models import Movie, Director
from .forms import DirectorForm, MovieForm
# Create your views here.

def home(request):
    movie_list = Movie.objects.all()
    Director_list = Director.objects.all()
    context = {
        "movies": movie_list,
        "Directores": Director_list 
    }

    return render(
        request,
        'index.html',
        context
    )
def add(request):
    form = MovieForm()
    context = {
        'titulo' : 'Pelicula',
        'form' : form
    }
    return render(
        request,
        'add.html',
        context
    )

def add_director(request):
    form = DirectorForm()
    context = {
        'titulo' : 'Director',
        'form': form
    }
    return render(
        request,
        'add.html',
        context

    )
