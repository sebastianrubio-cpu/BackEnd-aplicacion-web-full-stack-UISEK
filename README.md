# Examen Final - Aplicación Web Full-Stack UISEK

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-REST-darkgreen?style=for-the-badge&logo=django)
![React](https://img.shields.io/badge/React-18-61dafb?style=for-the-badge&logo=react)
![License](https://img.shields.io/badge/License-Academic-orange?style=for-the-badge)

**Una aplicación web Full-Stack moderna con autenticación OAuth 2.0 y gestión de catálogos**

</div>

---

## 1. Introducción del Proyecto
Este proyecto consiste en el diseño, desarrollo e implementación de una aplicación web full-stack desacoplada destinada a la gestión y visualización de un catálogo de películas, directores y vendedores. El sistema integra un Backend robusto basado en el framework Django (Django REST Framework) que actúa como proveedor de datos y servidor de autenticación bajo el estándar OAuth 2.0, y un Frontend ágil e interactivo desarrollado en React mediante Vite. La comunicación entre ambas capas se realiza de manera segura mediante peticiones asíncronas HTTP/HTTPS protegidas por tokens de acceso Bearer.

### Integrantes
- Sebastian Andres Rubio Rivera

### Carrera
Ingeniería en Informática

### Universidad
Universidad Internacional SEK (UISEK)
---

## 2. Objetivos del Proyecto

### Objetivo Académico
- Demostrar la capacidad práctica e intelectual para diseñar una arquitectura de software distribuida y desacoplada, aplicando patrones de diseño de software correctos.
- Implementar mecanismos rigurosos de seguridad y control de acceso utilizando el protocolo de autorización OAuth 2.0 a nivel de API REST.
- Consolidar habilidades en el manejo de bases de datos relacionales, persistencia de archivos multimedia y control de políticas de intercambio de recursos de origen cruzado (CORS).

### Expansión hacia un Modelo de Producción Profesional (Teoría de Escalabilidad)
Para transformar este prototipo académico en una plataforma lista para el mercado con alta disponibilidad, se contemplan los siguientes ejes de expansión:


1. **Desacoplamiento de Base de Datos y Almacenamiento:** Migrar el motor local SQLite a una base de datos relacional administrada de nivel empresarial (como PostgreSQL o Amazon RDS). Los archivos multimedia (pósteres y fotos) se trasladarían desde el disco local hacia un servicio de almacenamiento de objetos en la nube, como Amazon S3, distribuyéndolos mediante una red de entrega de contenido (CDN) como Cloudflare.

2. **Contenerización y Orquestación:** Empaquetar de manera independiente las aplicaciones de Frontend y Backend utilizando contenedores Docker. Esto garantizaría que el sistema se ejecute bajo las mismas variables y dependencias exactas en cualquier infraestructura, permitiendo su orquestación automatizada en clústeres mediante Kubernetes.

3. **Escalabilidad Horizontal e Infraestructura Serverless:** Desplegar el Backend detrás de un balanceador de carga (Nginx o AWS ALB) con auto-scaling para levantar instancias dinámicamente según la demanda. El Frontend de React se compilaría a archivos estáticos puros para ser servidos directamente desde infraestructuras Edge (como AWS Amplify, Vercel o Netlify), reduciendo la latencia de carga global a milisegundos.

4. **Seguridad y CI/CD:** Implementar HTTPS mandatorio mediante certificados SSL/TLS administrados, resguardar las credenciales sensibles y llaves maestras en administradores de secretos (como AWS Secrets Manager) e integrar flujos de Integración y Despliegue Continuos (CI/CD) automatizados mediante GitHub Actions.

---


## 🛠️ Tecnologías utilizadas

### 🔙 Backend

```
┌─────────────────────────────────────┐
│      Django REST Framework          │
├─────────────────────────────────────┤
│  • Django ORM                       │
│  • OAuth 2.0 Integration            │
│  • Serializers & Validators         │
│  • Authentication & Permissions     │
└─────────────────────────────────────┘
         ↓
    SQLite Database
```

### 🎨 Frontend

```
┌─────────────────────────────────────┐
│        React + Vite                 │
├─────────────────────────────────────┤
│  • Material UI Components           │
│  • Axios para HTTP Requests         │
│  • State Management                 │
│  • Responsive Design                │
└─────────────────────────────────────┘
```

### 🔧 Herramientas

- **Control de versiones**: Git & GitHub
- **Testing de APIs**: Postman
- **Editor**: VS Code (recomendado)

---

## 📚 Características principales

### 🔐 Autenticación

- ✅ Inicio de sesión mediante **OAuth 2.0**
- ✅ Protección de endpoints
- ✅ Manejo seguro de tokens de acceso
- ✅ Cierre de sesión

### 📊 Gestión de datos (CRUD)

- ✅ **Crear** registros
- ✅ **Leer** información
- ✅ **Actualizar** registros
- ✅ **Eliminar** registros

### 🌐 API REST

```
GET    /api/items/          → Listar todos los registros
POST   /api/items/          → Crear nuevo registro
GET    /api/items/{id}/     → Obtener un registro específico
PUT    /api/items/{id}/     → Actualizar completo
PATCH  /api/items/{id}/     → Actualización parcial
DELETE /api/items/{id}/     → Eliminar registro
```

---

## 📂 Estructura del proyecto

```
examen-final-UISEK/
│
├── 📂backend/                  # Directorio raíz del Backend (Django)
│   ├── 📂backend/              # Configuración global del proyecto de Django
│   │   ├── settings.py       # Variables de entorno, APPS, Middlewares y seguridad
│   │   ├── urls.py           # Enrutador principal del sistema (Admin, OAuth2)
│   │   └── wsgi.py / asgi.py # Interfaces de pasarela para servidores web
│   ├── 📂catalog/              # Aplicación local encargada del catálogo de películas
│   │   ├── migrations/       # Historial de cambios y mutaciones de la base de datos
│   │   ├── models/           # Definición de las entidades (Pelicula, Director, Vendedor)
│   │   ├── serializers/      # Lógica de transformación de Modelos a JSON (y viceversa)
│   │   ├── views/            # Lógica de control y ViewSets que procesan las peticiones
│   │   ├── admin.py          # Registro de modelos en el panel de administración nativo
│   │   └── urls.py           # Enrutamiento específico del API de catálogo
│   ├── 📂media/                # Almacenamiento local de archivos multimedia (Pósteres/Fotos)
│   ├── 📂manage.py             # Utilidad de línea de comandos para la gestión del Backend
│   └── 📂requirements.txt      # Manifiesto de dependencias y librerías de Python
│
├── 📂frontend/                 # Directorio raíz del Frontend (React + Vite)
│   ├── 📂public/               # Recursos estáticos globales abiertos (Favicon, SVGs)
│   ├── 📂src/                  # Código fuente ejecutable de la interfaz
│   │   ├── assets/           # Imágenes y hojas de estilo base
│   │   ├── App.jsx           # Componente raíz y lógica principal de la aplicación
│   │   └── main.jsx          # Punto de entrada de renderizado de React en el DOM
│   ├── 📂index.html            # Lienzo HTML5 principal de la aplicación
│   ├── 📂package.json          # Manifiesto de dependencias de Node.js y scripts de ejecución
│   └── 📂vite.config.js        # Configuración del compilador y servidor de desarrollo Vite
│
└──readme.me                   #Archivo actual

```

---

## 🚀 Instalación rápida

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/sebastianrubio-cpu/examen-final.-aplicacion-web-full-stack-UISEK.git
cd examen-final.-aplicacion-web-full-stack-UISEK
```

### 2️⃣ Configurar el Backend

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor Django
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000`

### 3️⃣ Configurar el Frontend

```bash
# En otra terminal, navegar a frontend
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:5173`

---

## 📬 Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/auth/login/` | Iniciar sesión |
| `POST` | `/api/auth/logout/` | Cerrar sesión |
| `POST` | `/api/auth/token/refresh/` | Refrescar token |

### Catálogo

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/items/` | Listar todos | ✓ |
| `POST` | `/api/items/` | Crear nuevo | ✓ |
| `GET` | `/api/items/{id}/` | Obtener uno | ✓ |
| `PUT` | `/api/items/{id}/` | Actualizar | ✓ |
| `PATCH` | `/api/items/{id}/` | Actualizar parcial | ✓ |
| `DELETE` | `/api/items/{id}/` | Eliminar | ✓ |

---

## 🔐 Seguridad

La aplicación implementa múltiples capas de seguridad:

```
🔒 OAuth 2.0 Authentication
    ↓
🔑 JWT Tokens (Access & Refresh)
    ↓
🛡️ CORS Configuration
    ↓
✅ HTTPS (en producción)
    ↓
🔐 Encrypted Passwords (bcrypt)
```

**⚠️ Nota**: Los endpoints protegidos requieren un Access Token válido en el header:

```
Authorization: Bearer {access_token}
```

---

## 🧪 Pruebas con Postman

Se incluye una colección de Postman con:

- ✅ Flujo completo de autenticación
- ✅ CRUD completo
- ✅ Variables de entorno preconfiguradas
- ✅ Ejemplos de request y response
- ✅ Endpoints protegidos

**Ubicación**: `/postman/coleccion.json`

---

## 📋 Requisitos del sistema

| Requisito | Versión mínima |
|-----------|-----------------|
| Node.js | 16.x |
| npm | 7.x |
| Python | 3.8+ |
| Django | 4.0+ |
| Git | 2.x |

---

## 📊 Composición del código

```
Python   ███████░░░░░░░░ 53.5%
CSS      ████░░░░░░░░░░░ 24.9%
JavaScript ███░░░░░░░░░░░ 19.8%
HTML     ░░░░░░░░░░░░░░░  1.8%
```

---

## 📖 Comandos útiles

### Backend

```bash
# Crear superuser
python manage.py createsuperuser

# Acceder a shell interactivo
python manage.py shell

# Ver migraciones
python manage.py showmigrations

# Crear nueva app
python manage.py startapp nombre_app
```

### Frontend

```bash
# Compilar para producción
npm run build

# Preview de build
npm run preview

# Linting
npm run lint
```

---

## 🎓 Conceptos aplicados

- ✅ Arquitectura REST
- ✅ Principios SOLID
- ✅ MVC Pattern (Backend)
- ✅ Component-Based Design (Frontend)
- ✅ DRY (Don't Repeat Yourself)
- ✅ Separación de responsabilidades
- ✅ Versionado semántico
- ✅ Documentación clara

---

## 📧 Contacto & Contribuciones

Este es un proyecto académico de la **Universidad Internacional SEK (UISEK)**.

**Estudiantes**:
- Nombre del estudiante 1
- Nombre del estudiante 2

---

## 📄 Licencia

```
© 2024 Proyecto desarrollado con fines académicos
Universidad Internacional SEK (UISEK)
Asignatura: Desarrollo Web
```

<div align="center">

**Hecho con ❤️ para Pablito**

[⬆ Volver arriba](#examen-final---aplicación-web-full-stack-uisek)

</div>
