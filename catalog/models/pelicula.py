from django.db import models
from catalog.models.director import Director
from catalog.models.vendedor import Vendedor  

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    fecha_lanzamiento = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='peliculas')
    vendedores = models.ManyToManyField(Vendedor, related_name='peliculas', blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    genero_choices = [
        ('ACCION', 'Acción'),
        ('COMEDIA', 'Comedia'),
        ('DRAMA', 'Drama'),
        ('TERROR', 'Terror'),
        ('CIENCIA_FICCION', 'Ciencia Ficción'),
        ('ANIMACION', 'Animación'),
        ('DOCUMENTAL', 'Documental'),
        ('ROMANCE', 'Romance'),
        ('AVENTURA', 'Aventura'),
        ('FANTASIA', 'Fantasía'),
        ('MUSICAL', 'Musical'),
        ('SUSPENSE', 'Suspense'),
        ('WESTERN', 'Western'),
    ]
    genero = models.CharField(max_length=50, choices=genero_choices, default='DRAMA')

    def __str__(self):
        return self.nombre