from dataclasses import fields
from pyexpat import model
from xml.etree.ElementTree import Comment
from django import forms
from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):

    class Meta: 
        model = Movie
        fields = ['nombre', 'comentarios', 'imdb']


##class MovieForm(forms.Form):nombre = forms.CharField(label='Agregar nombre', max_length=100, required=True)  Comment = forms.CharField(      label="Agregar comentario", 
# max_length=200,      required=False)