from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    premios_ganados = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='directores/', null=True, blank=True)

    def __str__(self):
        return self.nombre