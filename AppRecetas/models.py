from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=30)
    descripcion_breve_receta = models.CharField(max_length=100)
    lista_de_ingredientes = models.CharField(max_length=100)
    pasos_a_seguir = models.CharField(max_length=100)
    publisher = models.ForeignKey(to=User, on_delete = models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="recetas", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    instagram = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True) #Si no logro que funcione el CSS en la linea 57, entnonces le borro el null y el blank asi me obliga a poner una foto


class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")