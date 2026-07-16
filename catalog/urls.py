from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from catalog.views.director_view import DirectorViewSet
from catalog.views.vendedor_view import VendedorViewSet
from catalog.views.pelicula_view import PeliculaViewSet

# Registramos las vistas en el Router
router = DefaultRouter()
router.register(r'directores', DirectorViewSet, basename='director')
router.register(r'vendedores', VendedorViewSet, basename='vendedor')
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')
urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)