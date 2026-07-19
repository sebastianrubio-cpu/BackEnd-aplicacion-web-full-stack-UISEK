# catalog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import pelicula_view, director_view, vendedor_view
from catalog.views import pelicula_view, director_view, vendedor_view, user_view

router = DefaultRouter()

# Registro de los ViewSets asociados a cada uno los 3 modelos
router.register(r'peliculas', pelicula_view.PeliculaViewSet, basename='pelicula')
router.register(r'directores', director_view.DirectorViewSet, basename='director')
router.register(r'vendedores', vendedor_view.VendedorViewSet, basename='vendedor')


urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/registro/', user_view.RegistroView.as_view(), name='user-registro'),
    path('usuarios/perfil/', user_view.PerfilView.as_view(), name='user-perfil'),
]