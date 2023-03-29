from django.contrib import admin
from librosApp.models import libro, usurioData

# Register your models here.
class libroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'autor','genero','estado')

class usurioDataAdmin(admin.ModelAdmin):
    list_display = ('fechaNacimiento', 'genero', 'idUser')

admin.site.register(libro, libroAdmin)
admin.site.register(usurioData, usurioDataAdmin)