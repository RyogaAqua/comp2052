# COMP 2052 -- Server-Side Web Development and Back-End Microservices

Autor: Emmanuel A. Arguelles Ocasio  
Fecha: 20 de abril de 2025  

## 📋 Descripción del Proyecto

Este proyecto es una aplicación Flask que implementa un sistema de autenticación y autorización basado en roles (usuarios y administradores). El objetivo principal es proteger rutas específicas según los permisos asignados a cada rol, utilizando Flask-Principal y Flask-Login. Además, se incluyen pruebas para las rutas del API y una interfaz de usuario básica.

## 🚀 Funcionalidades Principales

1. **Autenticación y Autorización**:
   - Inicio de sesión con validación de credenciales.
   - Roles definidos: `user` y `admin`.
   - Protección de rutas según permisos.

2. **Rutas Implementadas**:
   - `/`: Redirige al formulario de inicio de sesión.
   - `/login`: Maneja el inicio de sesión.
   - `/home`: Página de bienvenida tras iniciar sesión.
   - `/articulos`: Muestra artículos accesibles para usuarios autenticados.
   - `/admin/articulos`: Muestra artículos exclusivos para administradores.
   - `/logout`: Cierra la sesión del usuario.

3. **Pruebas de API**:
   - Pruebas realizadas con archivos `.rest` para verificar las rutas `/login`, `/articulos`, y `/admin/articulos`.

4. **Interfaz de Usuario**:
   - Diseño responsivo utilizando CSS.
   - Mensajes de error y éxito mostrados dinámicamente en la interfaz.

## 📂 Estructura del Proyecto

![Diagrama de Flujo](./imagenes_prueba/Flow_M3_L2.png)

## 🧪 Pruebas Realizadas

Se realizaron pruebas manuales y automáticas para verificar el correcto funcionamiento de las rutas y permisos. A continuación, se muestran las capturas de pantalla de las pruebas:

### Pruebas de Inicio de Sesión
- **Inicio de sesión exitoso**:
  ![Inicio de Sesión Exitoso de Admin](./imagenes_prueba/admin_home.png)

  ![Inicio de Sesión Exitoso de Usuario](./imagenes_prueba/usuario_home.png)

- **Inicio de sesión fallido**:
  ![Inicio de Sesión Fallido](./imagenes_prueba/invalido.png)

### Pruebas de Acceso a Rutas
- **Acceso a artículos como usuario**:
  ![Artículos Usuario](./imagenes_prueba/usuario_articulo.png)

- **Acceso a artículos como administrador**:
  ![Artículos Admin](./imagenes_prueba/admin_articulo.png)

- **Acceso denegado a ruta protegida**:
  ![Acceso Denegado](./imagenes_prueba/error_403.png)

## 🌐 Rutas del Proyecto

1. **Página Principal** (`/`):
   - Redirige al formulario de inicio de sesión.

2. **Inicio de Sesión** (`/login`):
   - Procesa las credenciales ingresadas por el usuario.
   - Redirige a `/home` si las credenciales son válidas.

3. **Página de Bienvenida** (`/home`):
   - Muestra un mensaje de bienvenida con el rol del usuario autenticado.

4. **Artículos para Usuarios** (`/articulos`):
   - Muestra artículos accesibles para usuarios autenticados.

5. **Artículos Exclusivos para Administradores** (`/admin/articulos`):
   - Muestra artículos exclusivos para administradores.

6. **Cerrar Sesión** (`/logout`):
   - Cierra la sesión del usuario y redirige al formulario de inicio de sesión.

## 🔗 Enlace al Repositorio

GitHub:  
[https://github.com/RyogaAqua/comp2052](https://github.com/RyogaAqua/comp2052)
