from django.db import models
from django.contrib.auth.models import User #lo importo para hacer la parte de publisher

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=30)
    descripcion_breve_receta = models.CharField(max_length=100)
    lista_de_ingredientes = models.CharField(max_length=100)
    pasos_a_seguir = models.CharField(max_length=100)
    publisher = models.ForeignKey(to=User, on_delete = models.CASCADE, related_name="publisher")

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"