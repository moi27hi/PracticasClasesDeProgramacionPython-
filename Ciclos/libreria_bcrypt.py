import bcrypt

# --- Encriptar una contraseña ---
password = "mi_contraseña_segura".encode('utf-8')

# Generar un "salt" (valor aleatorio para reforzar la seguridad)
salt = bcrypt.gensalt()

# Crear el hash de la contraseña
hashed = bcrypt.hashpw(password, salt)

print("Contraseña original:", password)
print("Hash generado:", hashed)

# --- Verificar la contraseña ---
password_ingresada = "mi_contraseña_segura".encode('utf-8')

if bcrypt.checkpw(password_ingresada, hashed):
    print("✅ La contraseña es correcta.")
else:
    print("❌ La contraseña es incorrecta.")
