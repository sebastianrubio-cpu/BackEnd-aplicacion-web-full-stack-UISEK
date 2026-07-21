from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog.views.director_view import DirectorViewSet
from catalog.views.vendedor_view import VendedorViewSet
from catalog.views.pelicula_view import PeliculaViewSet

router = DefaultRouter()
router.register(r"directores", DirectorViewSet, basename="director")
router.register(r"vendedores", VendedorViewSet, basename="vendedor")
router.register(r"peliculas", PeliculaViewSet, basename="pelicula")
urlpatterns = [
    path("", include(router.urls)),
]
