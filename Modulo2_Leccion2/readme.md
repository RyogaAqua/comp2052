REGISTER App
Una aplicación web para gestionar tareas, construida con Flask, Jinja2 y Bootstrap 5. Incluye una REST API integrada y una interfaz web responsiva que permite entrar y validar un registro de usuario.

Register Form

🚀 Tecnologías utilizadas
Flask – Backend y servidor web
Jinja2 – Motor de plantillas HTML
Bootstrap 5 – Framework CSS para diseño moderno y responsivo
HTML5, CSS3, JavaScript (mínimo)
📁 Estructura del Proyecto
simple-form/
│
├── static/
│   └── css/
│       └── styles.css         # Estilos personalizados
│
├── templates/
│   ├── base.html              # Layout principal
│   ├── home.html              # Página para entradas válidas.
│   └── index.html             # Página principal con formulario
│
├── app.py                     # App principal con vistas y lógica de frontend
└── requirements.txt           # Dependencias del proyecto
✨ Características
✅ Interfaz limpia y responsiva con Bootstrap 5 ✅ Simulación de registro de usuarios (uso de forms) ✅ Simulación de login de usuarios (uso de forms) ✅ API REST integrada (/register) ✅ Código modular y mantenible

🔧 Instalación del App
Clona el repositorio:
git clone https://github.com/tu-usuario/comp2052.git
cd simple-form
Instala las dependencias:
pip install -r requirements.txt
Ejecuta la aplicación:
python app.py
Abre tu navegador y ve a http://localhost:5000

📡 Endpoints de la API
GET /register
Presenta la página web que contiene el formulario para registro de usuario.

Register Form

POST /register
Procesa la entrada de un formulario. Resultado esperado:

Home Page