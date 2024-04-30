from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    nuevo = models.BooleanField(default=True)
