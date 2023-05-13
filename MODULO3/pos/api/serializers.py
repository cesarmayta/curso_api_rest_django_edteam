from rest_framework import serializers

from .models import (
    Categoria,Producto,
    Cliente,Pedido,PedidoProducto)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['imagen'] = instance.imagen.url
        return representation
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
""" serializers de tablas relacionadas """
class CategoriaProductoSerializer(serializers.ModelSerializer):
    Productos = ProductoSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = ['id','nombre','Productos']

class PedidoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProducto
        fields = ['producto','cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    pedidoproductos = PedidoProductoSerializer(many=True)
    
    class Meta:
        model = Pedido
        fields = ['codigo','cliente','pedidoproductos']
        
    def create(self,validated_data):
        lista_pedido_productos = validated_data.pop('pedidoproductos')
        pedido = Pedido.objects.create(**validated_data)
        for obj_pedido_producto in lista_pedido_productos:
            PedidoProducto.objects.create(pedido=pedido,**obj_pedido_producto)
        return pedido     