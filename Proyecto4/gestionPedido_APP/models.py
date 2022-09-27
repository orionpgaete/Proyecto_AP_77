from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

    # python manage.py makemigrations

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    nropedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()