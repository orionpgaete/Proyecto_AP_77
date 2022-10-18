from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fono = models.CharField(max_length=20)

    