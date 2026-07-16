from rest_framework import serializers
from catalog.models.vendedor import Vendedor

class VendedorSerializer(serializers.ModelSerializer):
    # Mostramos la representación legible del 'choice' en modo de solo lectura
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Vendedor
        fields = ['id', 'nombre', 'tipo', 'tipo_display']