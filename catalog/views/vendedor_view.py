from rest_framework import viewsets
from catalog.models.vendedor import Vendedor  
from catalog.serializers.vendedor_serializer import VendedorSerializer
from catalog.permissions import IsAdminOrAuthenticatedReadOnly

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]