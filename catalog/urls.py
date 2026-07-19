# catalog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import pelicula_view, director_view, vendedor_view

# Inicialización del enrutador global para la app catalog
router = DefaultRouter()

# Registro de los ViewSets asociados a cada uno los 3 modelos
router.register(r'peliculas', pelicula_view.PeliculaViewSet, basename='pelicula')
router.register(r'directores', director_view.DirectorViewSet, basename='director')
router.register(r'vendedores', vendedor_view.VendedorViewSet, basename='vendedor')

# Los patrones de URL de la aplicación ahora dependen completamente del router
urlpatterns = [
    path('', include(router.urls)),
]