from django.db import models

class Vendedor(models.Model):
    TIPO_CHOICES = [
        ('DIGITAL', 'Digital'),
        ('CINE', 'Cine'),
        ('STREAMING', 'Streaming'),
        ('FISICO', 'Físico'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"