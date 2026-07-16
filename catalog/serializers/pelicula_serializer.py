from rest_framework import serializers
from catalog.models.pelicula import Pelicula
from catalog.models.director import Director
from catalog.models.vendedor import Vendedor
from .director_serializer import DirectorSerializer
from .vendedor_serializer import VendedorSerializer

class PeliculaSerializer(serializers.ModelSerializer):
    director_detail = DirectorSerializer(source='director', read_only=True)
    vendedores_detail = VendedorSerializer(source='vendedores', many=True, read_only=True)

    class Meta:
        model = Pelicula
        fields = [
            'id', 
            'nombre', 
            'duracion', 
            'fecha_lanzamiento', 
            'director', 
            'director_detail', 
            'vendedores', 
            'vendedores_detail',
            'poster'
        ]
        extra_kwargs = {
            'director': {'write_only': True},
            'vendedores': {'write_only': True}
        }