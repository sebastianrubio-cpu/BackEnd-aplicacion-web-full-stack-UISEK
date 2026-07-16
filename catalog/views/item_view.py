from rest_framework import viewsets
from catalog.models.item import Item
from catalog.serializers.item_serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer