from django.db import models


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto"""
        return f"{self.marca},{self.modelo},{self.año}"



