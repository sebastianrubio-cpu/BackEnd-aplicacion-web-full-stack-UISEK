from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # OAuth 2.0 endpoints para login y tokens
    path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/v1/catalog/', include('catalog.urls')),
]