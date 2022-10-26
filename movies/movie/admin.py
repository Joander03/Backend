from django.contrib import admin
from movie.models import Director, Movie
from movie.models import Actor

# Register your models here.

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)