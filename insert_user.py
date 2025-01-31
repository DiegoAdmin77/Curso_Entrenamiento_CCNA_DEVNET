import sqlite3
import hashlib

# Función para hashear la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Conectar a la base de datos
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
usuario = input("Ingrese un nombre de usuario único: ")
password = input("Ingrese su contraseña: ")

# Hashear la contraseña
password_hash = hash_password(password)

# Insertar usuario en la base de datos
try:
    cursor.execute("INSERT INTO usuarios (nombre, apellido, usuario, password_hash) VALUES (?, ?, ?, ?)", 
                   (nombre, apellido, usuario, password_hash))
    conexion.commit()
    print("Usuario registrado correctamente.")
except sqlite3.IntegrityError:
    print("Error: El nombre de usuario ya está en uso.")

# Cerrar conexión
conexion.close()