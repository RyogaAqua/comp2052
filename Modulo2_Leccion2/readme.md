# COMP 2052 -- Server-Side Web Development and Back-End Microservices

Autor: Emmanuel A. Arguelles Ocasio  
Fecha: 20 de abril de 2025  

## 📋 Descripción del Proyecto

Este proyecto es una aplicación Flask que implementa un sistema de registro de usuarios utilizando formularios con validaciones. El objetivo principal es demostrar el manejo de formularios en Flask con WTForms, validaciones personalizadas y retroalimentación al usuario. Además, se incluyen pruebas para las rutas del API y una interfaz de usuario básica.

## 🚀 Funcionalidades Principales

1. **Formulario de Registro de Usuarios**:
   - Campos: Nombre de usuario, correo electrónico y contraseña.
   - Validaciones:
     - Nombre de usuario: Obligatorio, mínimo 3 caracteres.
     - Correo electrónico: Obligatorio, debe tener formato válido.
     - Contraseña: Obligatoria, mínimo 6 caracteres.
   - Mensajes de error personalizados para cada validación fallida.

2. **Rutas Implementadas**:
   - `/`: Página principal con el formulario de registro.
   - `/register`: Maneja el registro de usuarios con validaciones.
   - `/login`: Ruta para iniciar sesión (demostración básica).

3. **Pruebas de API**:
   - Pruebas realizadas con archivos `.rest` para verificar las rutas `/register` y `/login`.

4. **Interfaz de Usuario**:
   - Diseño responsivo y limpio utilizando CSS.
   - Mensajes de error y éxito mostrados dinámicamente en la interfaz.

## 📂 Estructura del Proyecto
Claro, aquí tienes un ejemplo de cómo estructurar el proyecto en texto para incluirlo en el readme.md:

```markdown
## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
comp2052/
│
├── static/
│   └── css/
│       └── styles.css          # Archivo de estilos CSS para la interfaz de usuario
│
├── templates/
│   ├── base.html               # Plantilla base para herencia
│   ├── index.html              # Página principal con el formulario de registro
│   └── home.html               # Página de bienvenida tras el registro exitoso
│
├── test/
│   ├── login_example_test.rest # Prueba para la ruta /login
│   ├── register_no_error.rest  # Prueba de registro sin errores
│   ├── register_with_error1.rest # Prueba de registro con errores (nombre vacío)
│   └── register_with_error2.rest # Prueba de registro con errores (faltan datos)
│
├── app.py                      # Código principal de la aplicación Flask
├── readme.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias del proyecto (si aplica)
```
```
## 🧪 Pruebas Realizadas

Se realizaron pruebas manuales y automáticas para verificar el correcto funcionamiento de las rutas y formularios. A continuación, se muestran las capturas de pantalla de las pruebas:

### Pruebas de Registro
- **Registro exitoso**:
  ![Registro Exitoso](./imagenes_prueba/registro_exitoso.png)

- **Errores de validación**:
  ![Errores de Validación](./imagenes_prueba/errores_validacion.png)

### Pruebas de API
- **GET /login**:
  ![Prueba GET Login](./imagenes_prueba/get_login.png)

- **POST /register**:
  ![Prueba POST Register](./imagenes_prueba/registro_exitoso.png)

## 🌐 Rutas del Proyecto

1. **Página Principal** (`/`):
   - Muestra el formulario de registro.
   - Mensajes de error dinámicos en caso de validaciones fallidas.

2. **Registro de Usuarios** (`/register`):
   - Procesa los datos enviados desde el formulario.
   - Realiza validaciones y redirige a la página de bienvenida si el registro es exitoso.

3. **Inicio de Sesión** (`/login`):
   - Ruta básica para manejar el inicio de sesión (demostración).

## 🔗 Enlace al Repositorio

GitHub:  
[https://github.com/RyogaAqua/comp2052](https://github.com/RyogaAqua/comp2052)
