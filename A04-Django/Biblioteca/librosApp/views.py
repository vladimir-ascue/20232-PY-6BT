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

def actualizarLibro(request):
    if request.method == 'POST':
        Codigo = request.POST['codigo']
        nuevoTitulo = request.POST['titulo']

        librito = libro.objects.get(codigo = Codigo)
        print(librito)
        #libro.Objects.all(codigo = Codigo)
        librito.titulo = nuevoTitulo
        librito.save()
        print(librito)

        return render(request, "actualizarLibro.html", {"libro": librito})
    return render(request, "actualizarLibro.html")

def listarLibros(request):
    if request.method == 'POST':
        libros = libro.objects.all()
        print ( libros )
        return render(request, "listarLibros.html", {"libros": libros})
    return render(request, "listarLibros.html")

