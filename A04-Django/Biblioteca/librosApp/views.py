from django.shortcuts import render
from librosApp.models import libro

# Create your views here.
def crearLibro(request):
    if request.method == 'POST':
        Codigo = request.POST['codigo']
        Titulo = request.POST['titulo']
        Autor = request.POST['autor']
        Genero = request.POST['genero']
        Estado = request.POST['estado']

        librito = libro(codigo=Codigo, titulo=Titulo, autor=Autor, genero=Genero, estado=Estado)
        librito.save()

        return render(request, "crearLibro.html", {"titulo": Titulo})
    return render(request, "crearLibro.html")

# def actiualizarLibro(request):
#     if request.method == 'POST':
#         Codigo = request.POST['codigo']
#
#         librito = libro.Objects.all(codigo = Codigo)
#         librito.estado = "inactivo"
#         librito.save()
#
#         return render(request, "actualizarLibro.html", {"titulo": Titulo})
#     return render(request, "creaactualizarLibro.html")