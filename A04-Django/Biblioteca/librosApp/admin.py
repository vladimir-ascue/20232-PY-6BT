from django.contrib import admin
from librosApp.models import libro

# Register your models here.
class libroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'autor','genero','estado')

admin.site.register(libro, libroAdmin)