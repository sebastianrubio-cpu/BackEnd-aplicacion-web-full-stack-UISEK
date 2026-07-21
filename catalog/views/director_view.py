from rest_framework import viewsets
from catalog.models.director import Director
from catalog.serializers.director_serializer import DirectorSerializer
from catalog.permissions import IsAdminOrAuthenticatedReadOnly 

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]