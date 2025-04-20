from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", error=None)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    return f"Usuario: {username}, Contraseña: {password}"

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Validaciones
        if not username or not email or not password:
            error = "Todos los campos son requeridos."
        elif len(username) < 3:
            error = "El nombre de usuario debe tener al menos 3 caracteres."
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error = "El correo electrónico no es válido."
        elif len(password) < 6:
            error = "La contraseña debe tener al menos 6 caracteres."
        else:
            message = f"Usuario {username} registrado con éxito con el correo {email}."
            return render_template("home.html", message=message)

    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
