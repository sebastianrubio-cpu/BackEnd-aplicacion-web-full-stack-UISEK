from rest_framework import viewsets
from catalog.models.pelicula import Pelicula
from catalog.serializers.pelicula_serializer import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer