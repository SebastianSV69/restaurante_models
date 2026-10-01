from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre  = models.CharField(max_length=100, unique=True)
    orden = models.PositiveSmallIntegerField(default=1)

    class Meta():
        ordering = ['orden']

    def __str__(self) -> str:
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='platos'
    )