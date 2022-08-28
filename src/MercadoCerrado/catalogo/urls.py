from django.urls import path
from .views import DetalleProductos, ListaProductos

urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'productos'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion')
]