from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog.views.user_view import PerfilView, RegistroView
from catalog.views.director_view import DirectorViewSet
from catalog.views.pelicula_view import PeliculaViewSet
from catalog.views.vendedor_view import VendedorViewSet

router = DefaultRouter()
router.register(r"directores", DirectorViewSet, basename="director")
router.register(r"peliculas", PeliculaViewSet, basename="pelicula")
router.register(r"vendedores", VendedorViewSet, basename="vendedor")

urlpatterns = [
    path("usuarios/registro/", RegistroView.as_view(), name="usuario-registro"),
    path("usuarios/perfil/", PerfilView.as_view(), name="usuario-perfil"),
    path("", include(router.urls)),
]