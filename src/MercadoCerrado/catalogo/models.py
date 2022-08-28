from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Producto (models.Model):
    precio = models.DecimalField ( max_digits = 5, decimal_places = 2)
    nombre = models.CharField ( max_length = 20)
    descripcion = models.TextField ( max_length = 50)
    agregado = models.DateTimeField (auto_now_add = True)
    imagen = models.ImageField ( upload_to = "productos", null = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = [ 'agregado']