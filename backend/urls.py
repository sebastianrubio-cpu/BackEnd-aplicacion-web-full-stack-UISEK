# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/catalog/', include('catalog.urls')),
    path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

# PASO CRÍTICO: Habilitar la entrega de archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)