from rest_framework import serializers
from catalog.models.director import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'nombre', 'fecha_nacimiento', 'premios_ganados', 'foto']