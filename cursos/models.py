from django.db import models

class Curso(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        app_label = 'cursos'  # Agrega esta línea
