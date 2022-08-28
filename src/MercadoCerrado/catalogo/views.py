from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Producto


class ListaProductos (ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "catalogo/catalogo.html"

class DetalleProductos (DetailView):
    model = Producto
    context_object_name = "producto"
    template_name = "catalogo/productos.html"