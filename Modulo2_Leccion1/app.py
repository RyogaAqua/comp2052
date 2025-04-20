from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = "data/productos.json"  # Ruta actualizada a la carpeta 'data'

# Función para leer el archivo JSON
def leer_productos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)  # Lista directamente
    else:
        return []  # Retorna lista vacía si no existe el archivo

# Función para guardar los productos en el archivo JSON
def guardar_productos(productos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)  # Escribe los productos en el archivo JSON

@app.route("/", methods=["GET"])
def index():
    productos = leer_productos()
    return render_template("index.html", productos=productos)

@app.route("/tabla", methods=["GET"])
def pagina_tabla():
    productos = leer_productos()
    return render_template("pagina_tabla.html", productos=productos)

@app.route("/lista", methods=["GET"])
def pagina_lista():
    productos = leer_productos()
    return render_template("pagina_lista.html", productos=productos)

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(leer_productos())

@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.json
    producto = data.get("producto")
    if not producto:
        return jsonify({"error": "Datos incompletos"}), 400

    productos = leer_productos()
    productos.append(producto)
    guardar_productos(productos)
    return jsonify({"message": "Nuevo producto creado"}), 201

@app.route("/productos", methods=["DELETE"])
def eliminar_producto():
    data = request.json
    producto = data.get("producto")
    if not producto:
        return jsonify({"error": "Datos incompletos"}), 400

    productos = leer_productos()
    if producto not in productos:
        return jsonify({"error": "Producto no encontrado"}), 404

    productos.remove(producto)
    guardar_productos(productos)
    return jsonify({"message": f"Producto '{producto}' eliminado"}), 200

@app.route("/productos", methods=["PUT"])
def actualizar_producto():
    data = request.json
    antiguo = data.get("old")
    nuevo = data.get("new")

    if not antiguo or not nuevo:
        return jsonify({"error": "Datos incompletos"}), 400

    productos = leer_productos()
    if antiguo not in productos:
        return jsonify({"error": "Producto no encontrado"}), 404

    index = productos.index(antiguo)
    productos[index] = nuevo
    guardar_productos(productos)
    return jsonify({"message": f"Producto actualizado de '{antiguo}' a '{nuevo}'"}), 200

if __name__ == "__main__":
    app.run(debug=True)
