import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para cargar los datos desde el archivo JSON
def cargar_datos():
    try:
        with open('estructura_datos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, devolver datos vacíos
        return {"usuarios": [], "productos": []}

# Ruta para guardar los datos en el archivo JSON
def guardar_datos(datos):
    with open('estructura_datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Cargar los datos al iniciar el servidor
datos = cargar_datos()

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "nombre": "Aplicación basada en Módulo 1 Lección 3",
        "versión": "1.0",
        "desarrollador": "Emmanuel A. Arguelles Ocasio"
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    nombre = data.get('nombre')
    correo = data.get('correo')

    # Validación de campos
    if not nombre or not correo:
        return jsonify({"error": "Faltan campos requeridos: nombre y correo"}), 400

    # Verificar si ya existe un usuario con ese correo
    for usuario in datos['usuarios']:
        if usuario['correo'] == correo:
            return jsonify({"error": "El usuario ya existe con ese correo"}), 409

    # Crear usuario y agregar a la lista
    nuevo_usuario = {
        "id": len(datos['usuarios']) + 1,
        "nombre": nombre,
        "correo": correo
    }
    datos['usuarios'].append(nuevo_usuario)

    # Guardar los datos actualizados
    guardar_datos(datos)

    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(datos['usuarios'])

if __name__ == '__main__':
    app.run(debug=True)
