from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views.item_view import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]