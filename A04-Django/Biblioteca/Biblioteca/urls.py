from django.contrib import admin
from django.urls import path
from Biblioteca.views import inicio, contacto
from librosApp.views import crearLibro, actualizarLibro, listarLibros

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', inicio),
    path('contacto/', contacto),
    path('clibro/', crearLibro),
    path('alibro/', actualizarLibro),
    path('llibro/', listarLibros),
]
