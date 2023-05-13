from django.db import models

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=250)
    
    def __str__(self):
        return self.titulo