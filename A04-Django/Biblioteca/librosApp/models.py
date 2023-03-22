from django.db import models

# Create your models here.
class libro(models.Model):
    codigo = models.CharField(max_length=45, null=False)
    titulo = models.CharField(max_length=150, null=False)
    autor = models.CharField(max_length=150, null=False)
    genero = models.CharField(max_length=150, null=False)
    estado = models.CharField(max_length=150, null=False)

