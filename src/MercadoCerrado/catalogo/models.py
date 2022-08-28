from distutils.command.upload import upload
from django.db import models

class Producto (models.Model):
    precio = models.DecimalField ( max_digits = 10, decimal_places = 2)
    nombre = models.CharField ( max_length = 60)
    descripcion = models.CharField ( max_length = 200)
    agregado = models.DateTimeField (auto_now_add = True)
    imagen = models.ImageField ( upload_to = "productos", null = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = [ 'agregado']