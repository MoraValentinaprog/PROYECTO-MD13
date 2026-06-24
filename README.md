# 📘 Blog Django (Proyecto Final)

## 🧩 Descripción del proyecto
Este proyecto es una aplicación web tipo blog desarrollada con Django. Permite gestionar publicaciones, autores y etiquetas, aplicando conceptos fundamentales del framework como modelos, vistas basadas en clases, formularios, templates, autenticación y organización de URLs.

El objetivo es consolidar los conocimientos adquiridos durante el curso mediante una aplicación funcional, estructurada y lista para ser presentada como proyecto final.

## 🚀 Funcionalidades principales

### 📝 Posts (Publicaciones)
* Crear publicaciones nuevas
* Listar todas las publicaciones
* Ver detalle de cada publicación
* Editar publicaciones existentes
* Eliminar publicaciones

### 👤 Autores
* Búsqueda de autores por nombre
* Visualización de datos básicos (nombre y email)

### 🔐 Autenticación
* Registro de usuarios
* Login de usuarios
* Logout seguro

### 🧠 Panel de administración
* Gestión completa desde Django Admin

## 🧱 Tecnologías utilizadas
* Python
* Django
* SQLite (base de datos por defecto)
* HTML + CSS
* Class Based Views (CBV)
* Django Templates

## ⚙️ Instalación y ejecución local

**1. Clonar repositorio**
```bash
git clone https://github.com/MoraValentinaprog/PROYECTO-MD13.git
cd PROYECTO-MD13

### 2. Crear entorno virtual

```
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

### 4. Crear migraciones

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```
python manage.py createsuperuser
```

### 6. Ejecutar servidor

```
python manage.py runserver
```

## 🌐 URLs principales

- / → Home
- /posts/ → Listado de posts
- /posts/create/ → Crear post
- /posts/<id>/ → Detalle
- /posts/<id>/edit/ → Editar
- /posts/<id>/delete/ → Eliminar
- /search/ → Búsqueda de autores
- /admin/ → Panel de administración

## 🔑 Autenticación

- Registro de usuarios disponible desde la app
- Login y logout integrados en la navegación
- Algunas acciones requieren usuario autenticado

## 🎯 Conceptos aplicados

- Modelos con relaciones (ForeignKey / ManyToMany)
- Validaciones personalizadas (clean())
- Class Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
- Templates con herencia
- Context processors
- Template tags y filtros personalizados
- URLs con namespacing
- Formularios Django con validación
- Seguridad CSRF
- Django Admin

## 📌 Notas del proyecto

Este proyecto fue desarrollado con fines educativos como práctica integral de Django, consolidando el flujo completo de desarrollo de una aplicación web desde modelos hasta vistas y templates.

## 🧑‍💻 Autor

Proyecto realizado como práctica de desarrollo web con Django.
