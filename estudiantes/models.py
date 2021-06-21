from clases.models import Clase
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    clase = models.ManyToManyField(
        Clase,
        related_name='clases'
    )

    def __str__(self):
        return self.nombre