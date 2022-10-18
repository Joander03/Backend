from django.db import models

# Create your models here.

class Movie(models.Model):
    nombre = models.CharField(max_length=100)
    comentarios = models.TextField()
    imdb = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre +" "+ self.apellido