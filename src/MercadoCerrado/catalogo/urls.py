from django.urls import path
from .views import DetalleProductos, ListaProductos, AgregarProducto

urlpatterns = [
    path ('', ListaProductos.as_view(), name = 'catalogo'),
    path ('producto/<int:pk>', DetalleProductos.as_view(), name = 'descripcion_producto'),
    path ('agregar-producto/', AgregarProducto.as_view(), name = 'form-producto')
]