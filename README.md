# Backend — Aplicación Web Full-Stack UISEK

API REST desarrollada con Django REST Framework para la gestión de un catálogo de películas, directores y vendedores.

El backend se encarga de:

- gestionar la base de datos;
- exponer los endpoints REST;
- autenticar usuarios mediante OAuth 2.0;
- almacenar pósteres y fotografías;
- aplicar permisos a las operaciones CRUD;
- comunicarse con el frontend desarrollado en React.

---

## Integrantes

- Alberto Sebastian Andrade Endara
- Sebastián Andrés Rubio Rivera

## Universidad

Universidad Internacional SEK — UISEK

## Carrera

Ingeniería en Informática

## Asignatura

Desarrollo Web

---

## Repositorios

### Backend

```text
https://github.com/sebastianrubio-cpu/BackEnd-aplicacion-web-full-stack-UISEK
```

### Frontend

```text
https://github.com/albertoandrade-gif/FronteEnd-aplicacion-web-full-stack-UISEK
```

---

## Tecnologías utilizadas

- Python 3.12
- Django
- Django REST Framework
- OAuth 2.0
- django-cors-headers
- SQLite
- Pillow
- Git y GitHub
- Postman

---

## Arquitectura del sistema

```text
Usuario
  ↓
Frontend React + Material UI
  ↓
Axios y peticiones HTTP
  ↓
Django REST Framework
  ↓
OAuth 2.0 y permisos
  ↓
SQLite y archivos multimedia
```

El backend no genera las páginas visuales de la aplicación. Su función es recibir peticiones, procesar datos y devolver respuestas en formato JSON.

---

## Modelos

### Director

Campos principales:

- `nombre`
- `fecha_nacimiento`
- `premios_ganados`
- `biografia`
- `foto`

### Película

Campos principales:

- `nombre`
- `duracion`
- `fecha_lanzamiento`
- `genero`
- `poster`
- `director`
- `vendedores`

### Vendedor

Campos principales:

- `nombre`
- `tipo`

---

## Relaciones entre entidades

```text
Director 1 ───────── N Películas

Películas N ───────── N Vendedores
```

Un director puede estar relacionado con varias películas.

Cada película pertenece a un director.

Una película puede distribuirse mediante varios vendedores y un vendedor puede distribuir varias películas.

---

## Funcionalidades

- Autenticación mediante OAuth 2.0.
- Protección global de los endpoints.
- CRUD completo de directores.
- CRUD completo de películas.
- CRUD completo de vendedores.
- Relaciones uno a muchos y muchos a muchos.
- Carga de pósteres de películas.
- Carga de fotografías de directores.
- Administración mediante Django Admin.
- Comunicación con React mediante CORS.
- Pruebas de API mediante Postman.

---

## Estructura principal

```text
BackEnd-aplicacion-web-full-stack-UISEK/
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── catalog/
│   ├── migrations/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── admin.py
│   └── urls.py
│
├── postman/
│   ├── Examen_Final_UISEK_API_Peliculas.postman_collection.json
│   └── UISEK_Local_Entrega.postman_environment.json
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

Las carpetas `venv`, `media` y el archivo `db.sqlite3` se mantienen únicamente de forma local y no se almacenan en GitHub.

---

## Requisitos

- Python 3.12
- pip
- Git
- Postman, opcional para pruebas
- Node.js y npm para ejecutar el frontend

---

## Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/sebastianrubio-cpu/BackEnd-aplicacion-web-full-stack-UISEK.git
```

Entrar al proyecto:

```powershell
cd BackEnd-aplicacion-web-full-stack-UISEK
```

### 2. Crear el entorno virtual

```powershell
py -3.12 -m venv venv
```

### 3. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

En caso de que PowerShell bloquee la activación:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

También se pueden ejecutar los comandos directamente con:

```powershell
.\venv\Scripts\python.exe
```

### 4. Instalar dependencias

```powershell
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Aplicar migraciones

```powershell
.\venv\Scripts\python.exe manage.py migrate
```

### 6. Crear un superusuario

```powershell
.\venv\Scripts\python.exe manage.py createsuperuser
```

### 7. Ejecutar el backend

```powershell
.\venv\Scripts\python.exe manage.py runserver
```

El servidor estará disponible en:

```text
http://127.0.0.1:8000
```

El panel administrativo estará disponible en:

```text
http://127.0.0.1:8000/admin/
```

---

## Configuración de OAuth 2.0

Para crear una aplicación OAuth:

1. Ejecutar el servidor de Django.
2. Entrar a:

```text
http://127.0.0.1:8000/admin/
```

3. Iniciar sesión con el superusuario.
4. Abrir la sección de aplicaciones OAuth.
5. Crear una aplicación para el frontend.
6. Asignar el usuario propietario.
7. Configurar el tipo de cliente y el flujo de autenticación utilizado por el proyecto.
8. Guardar el `client_id` únicamente en la configuración local.

Las contraseñas, tokens y secretos no deben almacenarse en GitHub.

---

## Endpoint de autenticación

### Obtener token OAuth

```text
POST /api/v1/o/token/
```

Parámetros principales:

```text
grant_type=password
username=USUARIO
password=CONTRASEÑA
client_id=CLIENT_ID
scope=read write
```

Cuando el usuario se autentica correctamente, el servidor devuelve un token de acceso.

Las peticiones protegidas deben incluir:

```http
Authorization: Bearer ACCESS_TOKEN
```

---

## Endpoints de directores

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/v1/catalog/directores/` | Listar directores |
| POST | `/api/v1/catalog/directores/` | Crear un director |
| GET | `/api/v1/catalog/directores/{id}/` | Consultar un director |
| PUT | `/api/v1/catalog/directores/{id}/` | Actualizar completamente |
| PATCH | `/api/v1/catalog/directores/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/catalog/directores/{id}/` | Eliminar un director |

---

## Endpoints de películas

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/v1/catalog/peliculas/` | Listar películas |
| POST | `/api/v1/catalog/peliculas/` | Crear una película |
| GET | `/api/v1/catalog/peliculas/{id}/` | Consultar una película |
| PUT | `/api/v1/catalog/peliculas/{id}/` | Actualizar completamente |
| PATCH | `/api/v1/catalog/peliculas/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/catalog/peliculas/{id}/` | Eliminar una película |

---

## Endpoints de vendedores

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/v1/catalog/vendedores/` | Listar vendedores |
| POST | `/api/v1/catalog/vendedores/` | Crear un vendedor |
| GET | `/api/v1/catalog/vendedores/{id}/` | Consultar un vendedor |
| PUT | `/api/v1/catalog/vendedores/{id}/` | Actualizar completamente |
| PATCH | `/api/v1/catalog/vendedores/{id}/` | Actualizar parcialmente |
| DELETE | `/api/v1/catalog/vendedores/{id}/` | Eliminar un vendedor |

---

## Ejemplos de datos

### Crear un director

```json
{
  "nombre": "Christopher Nolan",
  "fecha_nacimiento": "1970-07-30",
  "premios_ganados": 12,
  "biografia": "Director, guionista y productor de cine."
}
```

### Crear un vendedor

```json
{
  "nombre": "Netflix",
  "tipo": "NETFLIX"
}
```

### Crear una película

```json
{
  "nombre": "Inception",
  "duracion": 148,
  "fecha_lanzamiento": "2010-07-16",
  "genero": "CIENCIA_FICCION",
  "director": 1,
  "vendedores": [
    1
  ]
}
```

Para enviar imágenes, la petición debe utilizar `multipart/form-data`.

Los nombres de los campos son:

```text
poster
foto
```

---

## Archivos multimedia

Los archivos cargados localmente se almacenan en:

```text
media/
├── posters/
└── directores/
```

En desarrollo, Django permite acceder a ellos mediante:

```text
http://127.0.0.1:8000/media/
```

La carpeta `media/` está ignorada por Git porque contiene archivos subidos durante las pruebas locales.

---

## CORS

El backend permite peticiones desde el servidor local de Vite:

```text
http://localhost:5173
http://127.0.0.1:5173
```

Esto permite que el frontend React se comunique con Django aunque se ejecuten en puertos diferentes.

---

## Postman

La carpeta:

```text
postman/
```

contiene:

```text
Examen_Final_UISEK_API_Peliculas.postman_collection.json
UISEK_Local_Entrega.postman_environment.json
```

La colección incluye pruebas para:

- obtener el token OAuth;
- listar registros;
- crear registros;
- consultar registros;
- actualizar registros;
- eliminar registros.

El entorno de entrega no contiene contraseñas, tokens ni secretos reales.

Antes de ejecutar las peticiones deben completarse localmente las variables necesarias.

---

## Verificación del proyecto

Comprobar las dependencias:

```powershell
.\venv\Scripts\python.exe -m pip check
```

Resultado esperado:

```text
No broken requirements found.
```

Comprobar Django:

```powershell
.\venv\Scripts\python.exe manage.py check
```

Resultado esperado:

```text
System check identified no issues (0 silenced).
```

Comprobar cambios de modelos pendientes:

```powershell
.\venv\Scripts\python.exe manage.py makemigrations --check --dry-run
```

Resultado esperado:

```text
No changes detected
```

---

## Seguridad

No deben subirse al repositorio:

```text
.env
.env.local
venv/
db.sqlite3
media/
tokens OAuth
contraseñas
client_secret
```

La clave de Django se obtiene mediante:

```text
DJANGO_SECRET_KEY
```

Existe un valor predeterminado únicamente para el entorno académico local.

Los endpoints de la API requieren autenticación mediante token OAuth.

---

## Ejecución conjunta

### Terminal 1 — Backend

```powershell
cd "C:\Users\Luis Andrade\Documents\DesarrolloWeb\BackEnd-aplicacion-web-full-stack-UISEK"
.\venv\Scripts\python.exe manage.py runserver
```

### Terminal 2 — Frontend

```powershell
cd "C:\Users\Luis Andrade\Documents\DesarrolloWeb\FrontEnd-aplicacion-web-full-stack-UISEK"
npm.cmd run dev
```

Después abrir:

```text
http://localhost:5173
```

---

## Estado del proyecto

- Backend funcional.
- OAuth 2.0 operativo.
- CRUD completo.
- Base de datos relacional.
- Carga de imágenes habilitada.
- Frontend integrado.
- Colección de Postman incluida.
- Configuración sensible excluida de Git.
- Pruebas de Django completadas sin errores.

---

## Licencia

Proyecto desarrollado con fines exclusivamente académicos para la Universidad Internacional SEK.

© 2026 — Alberto Andrade y Sebastián Andrés Rubio Rivera