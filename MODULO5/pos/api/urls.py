from django.urls import path

from . import views

urlpatterns = [
    path('categoria', views.CategoriaListView.as_view()),
    path('categoria/<int:categoria_id>/productos', views.CategoriaProductosView.as_view()),
    path('producto', views.ProductoListView.as_view()),
    path('cliente',views.ClienteView.as_view()),
    path('cliente/<int:cliente_id>',views.ClienteDetailView.as_view()),
    path('pedido',views.PedidoCreateView.as_view())
]