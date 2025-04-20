from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, UserNeed, AnonymousIdentity, PermissionDenied
import json
from werkzeug.security import check_password_hash

# Inicializar la app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"

# Setup de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Setup de Flask-Principal
principal = Principal(app)

# Cargar los usuarios desde el archivo JSON
def load_users():
    with open('data/usuarios.json', 'r') as f:
        return json.load(f)

def load_admins():
    with open('data/admin.json', 'r') as f:
        return json.load(f)

# Cargar los artículos desde el archivo JSON
def load_articles():
    with open('data/articulos.json', 'r') as f:
        return json.load(f)

# Crear permisos
admin_permission = Permission(RoleNeed("admin"))
user_permission = Permission(RoleNeed("user"))

# Clase de usuario
class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    # Cargar usuarios y administradores desde JSON
    users = load_users()
    admins = load_admins()

    # Buscar en usuarios
    for user in users:
        if user['username'] == user_id:
            return User(user['username'], 'user')

    # Buscar en administradores
    for admin in admins:
        if admin['username'] == user_id:
            return User(admin['username'], 'admin')
    
    return None

# Formulario de Login
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3)],
                           render_kw={"placeholder": "Your email"})
    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={"placeholder": "Your password"})
    submit = SubmitField("Login", render_kw={"class": "btn btn-primary"})

# Ruta principal
@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("login"))

# Ruta de login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Cargar usuarios y administradores
        users = load_users()
        admins = load_admins()

        # Verificar si el usuario existe y la contraseña es correcta en usuarios
        for user in users:
            if user["username"] == username and check_password_hash(user["password"], password):
                user_obj = User(username, 'user')
                login_user(user_obj)

                # Actualizar identidad de Flask-Principal
                identity_changed.send(app, identity=Identity(user_obj.id))

                return redirect(url_for("home"))

        # Verificar si el usuario existe y la contraseña es correcta en administradores
        for admin in admins:
            if admin["username"] == username and check_password_hash(admin["password"], password):
                admin_obj = User(username, 'admin')
                login_user(admin_obj)

                # Actualizar identidad de Flask-Principal
                identity_changed.send(app, identity=Identity(admin_obj.id))

                return redirect(url_for("home"))

        # Si no encuentra el usuario o admin
        return render_template("index.html.jinja2", form=form, error="Invalid credentials")

    return render_template("index.html.jinja2", form=form)

# Ruta protegida accesible por cualquier usuario autenticado
@app.route("/home")
@login_required
def home():
    return render_template("home.html.jinja2", message=f"Bienvenido, {current_user.id}. Rol: {current_user.role}")

# Ruta para mostrar artículos accesibles para todos los usuarios autenticados
@app.route("/articulos")
@login_required
@user_permission.require(http_exception=403)  # Solo usuarios con rol "user" o "admin"
def articulos():
    articles = load_articles()
    visible_articles = [article for article in articles if current_user.role in article["visible_para"]]
    return render_template("usuario_articulos.html", articles=visible_articles)

# Ruta para mostrar artículos exclusivos para administradores
@app.route("/admin/articulos")
@login_required
@admin_permission.require(http_exception=403)  # Solo usuarios con rol "admin"
def admin_articulos():
    articles = load_articles()
    admin_articles = [article for article in articles if "admin" in article["visible_para"]]
    return render_template("admin_articulos.html", articles=admin_articles)

# Ruta exclusiva para admins
@app.route("/admin")
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return f"Hola Admin {current_user.id}, tienes acceso especial."

# Ruta exclusiva para usuarios estándar
@app.route("/user")
@login_required
@user_permission.require(http_exception=403)
def user():
    return f"Hola Usuario {current_user.id}, bienvenido a tu panel."

# Ruta para cerrar sesión
@app.route("/logout")
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for("login"))

# Vincular roles a la identidad del usuario
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if current_user.is_authenticated:
        identity.user = current_user
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.role))

# Manejo de errores 403 (Prohibido)
@app.errorhandler(403)
def forbidden(e):
    return render_template("error.html.jinja2", error_code=403, error_message="No tienes permiso para acceder a esta página."), 403

# Manejo de errores 404 (No encontrado)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html.jinja2", error_code=404, error_message="Página no encontrada."), 404

# Manejo de errores 500 (Error interno del servidor)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html.jinja2", error_code=500, error_message="Ocurrió un error interno en el servidor."), 500

if __name__ == "__main__":
    app.run(debug=True)
