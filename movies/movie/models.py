from django.db import models

# Create your models here.

class Movie(models.Model):
    nombre = models.CharField(max_length=100)
    comentarios = models.TextField()