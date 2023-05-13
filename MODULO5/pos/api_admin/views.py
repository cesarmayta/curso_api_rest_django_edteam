from rest_framework import viewsets

from api.models import (
    Categoria,Producto
)

from api.serializers import(
    CategoriaSerializer,
    ProductoSerializer
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer