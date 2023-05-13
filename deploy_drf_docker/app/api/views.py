from rest_framework import generics

from .models import (
    Categoria,Producto,
    Cliente,Pedido)
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer,
    ClienteSerializer,
    CategoriaProductoSerializer,
    PedidoSerializer)


class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    lookup_url_kwarg = 'cliente_id'
    serializer_class = ClienteSerializer
    
class CategoriaProductosView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CategoriaProductoSerializer
    
class PedidoCreateView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer