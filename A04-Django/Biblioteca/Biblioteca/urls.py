from django.contrib import admin
from django.urls import path
from Biblioteca.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ini/<nombre>', inicio),
]
