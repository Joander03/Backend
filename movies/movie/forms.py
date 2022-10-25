from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Director, Movie

class MovieForm(ModelForm):

    class Meta: 
        model = Movie
        fields = ['nombre', 'comentarios', 'imdb']

class DirectorForm(ModelForm):

    class Meta:
        model = Director
        fields = ['nombre', 'apellido']