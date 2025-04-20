# COMP 2052 -- Server-Side Web Development and Back-End Microservices

Autor: Emmanuel A. Arguelles Ocasio

Fecha: 20 de abril de 2025

## 🏠 Pantalla de Inicio
![Interfaz de usuario gráfica, Aplicación](./Imagenes_Prueba/inicio.png)

Descripción:\
La pantalla principal muestra una cuadrícula con los productos
disponibles. Cada producto incluye su nombre, precio y un botón de
compra.

Funcionalidad:\
Los datos de los productos se cargan dinámicamente desde el archivo
productos.json en el Back-End y se renderizan en esta plantilla
utilizando Jinja2.

Ruta:\
http://127.0.0.1:5000/

## 📊 Pantalla de Tabla de Productos
![Interfaz de usuario gráfica](./Imagenes_Prueba/tabla.png)

Descripción:\
Esta pantalla muestra los productos en formato de tabla, con columnas
para el número, nombre y precio de cada producto.

Funcionalidad:\
Los datos se cargan dinámicamente desde el archivo JSON y se organizan
en una tabla HTML.

Ruta:\
http://127.0.0.1:5000/tabla

## 📋 Pantalla de Lista de Productos
![Interfaz de usuario gráfica, Aplicación](./Imagenes_Prueba/lista.png)

Descripción:\
Esta pantalla muestra los productos en formato de lista, con solo el
nombre de cada producto.

Funcionalidad:\
Los datos se cargan dinámicamente desde el archivo JSON y se renderizan
como una lista HTML.

Ruta:\
http://127.0.0.1:5000/lista

## 🧪 Pruebas de API

Descripción:\
Se realizaron pruebas para las rutas del API utilizando los archivos
.rest en la carpeta test. Estas pruebas verifican las operaciones de
creación, actualización, eliminación y obtención de productos.

Rutas probadas:\
- GET /productos\
- POST /productos\
- PUT /productos\
- DELETE /productos

![Captura de pantalla de computadora](./Imagenes_Prueba/get.png)
![Texto](./Imagenes_Prueba/post.png)
![Texto](./Imagenes_Prueba/put.png)
![Texto](./Imagenes_Prueba/delete.png)

## 💡 Reflexión

Separación entre Back-End y Front-End:\
La separación entre Back-End y Front-End permite mantener el código
organizado y escalable. El Back-End maneja la lógica y los datos,
mientras que el Front-End se encarga de la presentación. Esto facilita
el mantenimiento y la colaboración en proyectos más grandes.

## 🔗 Enlace al Repositorio

GitHub:\
https://github.com/RyogaAqua/comp2052