from django.http import HttpResponse
from django.shortcuts import render

# Request: Cuando requiero parametros en la vista desde la plantilla (Forms)
#           implementa por defencto los token CSRF - Cross Site Scripting
# Response: Cuando enviamos datos de la vista a la plantilla
def inicio(request, nombre):
    data = {"nombre":"Vladimir", "apellido":"Ascue", "parametro":nombre+"#"}
    return render(request, "inicio.html", data)