from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('curso/',views.curso),
    path('curso/new/',views.post_curso),
    path('cursodrf/',views.CursoList.as_view())
]