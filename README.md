# Examen Final - Aplicación Web Full-Stack UISEK

## 📖 Descripción

Este proyecto corresponde al examen final de la asignatura de Desarrollo Web de la Universidad Internacional SEK (UISEK). Consiste en el desarrollo de una aplicación web Full-Stack que integra un backend desarrollado con Django REST Framework y un frontend desarrollado en React, utilizando autenticación mediante OAuth 2.0.

La aplicación implementa una arquitectura cliente-servidor donde Django funciona exclusivamente como API REST, mientras que React consume los servicios expuestos para ofrecer una interfaz moderna, intuitiva y responsiva.

---

## 🎯 Objetivo

Desarrollar una aplicación web Full-Stack que permita gestionar un catálogo mediante operaciones CRUD, aplicando los conocimientos adquiridos durante el curso sobre:

- Desarrollo de APIs REST
- React
- OAuth 2.0
- Consumo de APIs
- Arquitectura Cliente-Servidor
- Control de versiones con Git

---

## 🛠️ Tecnologías utilizadas

### Backend

- Django
- Django REST Framework
- OAuth 2.0
- SQLite (desarrollo)

### Frontend

- React
- Vite
- Material UI
- Axios

### Herramientas

- Git
- GitHub
- Postman

---

## 📂 Arquitectura del proyecto

```
Frontend (React)
        │
        │ HTTP + JSON
        ▼
Backend (Django REST Framework)
        │
        ▼
    Base de Datos
```

---

## 📚 Funcionalidades

### Autenticación

- Inicio de sesión mediante OAuth 2.0
- Protección de endpoints
- Manejo de tokens

### Gestión de información

- Listar registros
- Crear registros
- Editar registros
- Eliminar registros

### API REST

- GET
- POST
- PUT / PATCH
- DELETE

---

## 🔐 Seguridad

El proyecto implementa autenticación mediante OAuth 2.0.

Los endpoints protegidos requieren un Access Token válido para permitir el acceso a los recursos.

---

## 📦 Estructura del proyecto

```
/
├── backend/
│   ├── apps/
│   ├── api/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   └── urls.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── App.jsx
│
└── README.md
```

---

## 🚀 Instalación

### Clonar el repositorio

```bash
git clone <url-del-repositorio>
```

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📬 API

La API expone los siguientes métodos HTTP:

| Método | Descripción |
|----------|-------------|
| GET | Obtener información |
| POST | Crear registros |
| PUT | Actualizar registros |
| PATCH | Actualización parcial |
| DELETE | Eliminar registros |

---

## 🧪 Pruebas

Se incluye una colección de Postman con:

- Autenticación
- CRUD completo
- Variables de entorno
- Endpoints protegidos

---

## 📋 Requisitos

- Node.js
- npm
- Python 3.x
- Django
- Git
- VS Code (recomendado)

---

## 👥 Integrantes

- Nombre del estudiante 1
- Nombre del estudiante 2

---

## 📄 Licencia

Proyecto desarrollado con fines académicos para la Universidad Internacional SEK (UISEK).
