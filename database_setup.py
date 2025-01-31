import sqlite3

# Conectar con la base de datos (se creará si no existe)
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    usuario TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

print("Base de datos creada exitosamente.")