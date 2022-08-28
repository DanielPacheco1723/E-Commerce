from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Producto


class ListaProductos (ListView):
    model = Producto
    context_object_name = "catalogo"
    template_name = "catalogo/catalogo.html"

class DetalleProductos (DetailView):
    model = Producto
    context_object_name = "producto"
    template_name = "catalogo/productos.html"

class AgregarProducto (CreateView):
    model = Producto
    fields = ["nombre", "precio", "descripcion", "imagen"]
    success_url = reverse_lazy("catalogo")