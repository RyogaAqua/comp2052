import json
from werkzeug.security import generate_password_hash

# Cargar el archivo usuarios.json
with open("data/usuarios.json", "r") as f:
    usuarios = json.load(f)

# Convertir las contraseñas a hash
for usuario in usuarios:
    usuario["password"] = generate_password_hash(usuario["password"])

# Guardar el archivo actualizado
with open("data/usuarios.json", "w") as f:
    json.dump(usuarios, f, indent=4)

print("Contraseñas de usuarios hasheadas correctamente.")
