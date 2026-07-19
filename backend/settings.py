import os
from pathlib import Path


# =========================================================
# RUTAS BASE DEL PROYECTO
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SEGURIDAD
# =========================================================

# La clave puede definirse mediante la variable de entorno
# DJANGO_SECRET_KEY.
#
# El valor predeterminado se utiliza únicamente para desarrollo local.
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "uisek-clave-local-desarrollo-no-usar-en-produccion",
)

# Mantener True únicamente durante el desarrollo.
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# =========================================================
# APLICACIONES INSTALADAS
# =========================================================

INSTALLED_APPS = [
    # Aplicaciones propias de Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Aplicaciones externas
    "corsheaders",
    "rest_framework",
    "oauth2_provider",

    # Aplicaciones del proyecto
    "catalog",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    # CORS debe ubicarse antes de CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # Middleware de OAuth 2.0
    "oauth2_provider.middleware.OAuth2TokenMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# CONFIGURACIÓN PRINCIPAL DE DJANGO
# =========================================================

ROOT_URLCONF = "backend.urls"

WSGI_APPLICATION = "backend.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# PLANTILLAS
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}


# =========================================================
# BASE DE DATOS
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# =========================================================
# VALIDACIÓN DE CONTRASEÑAS
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =========================================================
# INTERNACIONALIZACIÓN
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =========================================================
# ARCHIVOS ESTÁTICOS
# =========================================================

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# ARCHIVOS MULTIMEDIA
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# CORS
# =========================================================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


# =========================================================
# OAUTH 2.0
# =========================================================

OAUTH2_PROVIDER = {
    # Duración del token de acceso en segundos.
    # 36000 segundos equivalen a 10 horas.
    "ACCESS_TOKEN_EXPIRE_SECONDS": 36000,

    # Permite autenticación del cliente OAuth.
    "CLIENT_ID_HTTP_BASIC_AUTH": True,

    # Permisos disponibles para la aplicación.
    "SCOPES": {
        "read": "Acceso de lectura a los datos del catálogo",
        "write": "Acceso de escritura para modificar el catálogo",
    },
}