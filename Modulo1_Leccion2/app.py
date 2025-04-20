from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "nombre": "Applicacion basade en Modulo 1 Leccion 2",
        "versión": "1.0",
        "desarrollador": "Emmanuel A. Arguelles Ocasio"
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    nombre = data.get("nombre", "usuario")
    return jsonify({"respuesta": f"Hola, {nombre}, tu mensaje ha sido recibido."})

if __name__ == '__main__':
    app.run(debug=True)
