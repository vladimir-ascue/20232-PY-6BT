from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class libro(models.Model):
    codigo = models.CharField(max_length=45, null=False)
    titulo = models.CharField(max_length=150, null=False)
    autor = models.CharField(max_length=150, null=False)
    genero = models.CharField(max_length=150, null=False)
    estado = models.CharField(max_length=150, null=False)

    def __str__ (self):
        return f'%s\n%s\n%s' % (self.codigo, self.titulo, self.autor)

class usurioData(models.Model):
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=9)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
