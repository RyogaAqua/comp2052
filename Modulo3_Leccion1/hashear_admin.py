import json
from werkzeug.security import generate_password_hash

# Cargar archivo
with open("data/admin.json", "r") as f:
    admins = json.load(f)

# Convertir las contraseñas a hash
for admin in admins:
    admin["password"] = generate_password_hash(admin["password"])

# Guardar el archivo actualizado
with open("data/admin.json", "w") as f:
    json.dump(admins, f, indent=4)

print("Contraseñas hasheadas correctamente.")