from rest_framework import serializers
from catalog.models.pelicula import Pelicula
from catalog.models.director import Director
from catalog.models.vendedor import Vendedor
from catalog.serializers.director_serializer import DirectorSerializer  # <-- Corregido a importación absoluta
from catalog.serializers.vendedor_serializer import VendedorSerializer  # <-- Corregido a importación absoluta

class PeliculaSerializer(serializers.ModelSerializer):
    director_detail = DirectorSerializer(source='director', read_only=True)
    vendedores_detail = VendedorSerializer(source='vendedores', many=True, read_only=True)

    class Meta:
        model = Pelicula
        fields = [
            "id",
            "nombre",
            "duracion",
            "fecha_lanzamiento",
            "genero",
            "director",
            "director_detail",
            "vendedores",
            "vendedores_detail",
            "poster",
        ]
        extra_kwargs = {
            'director': {'write_only': True},
            'vendedores': {'write_only': True}
        }