# database.py
# Base de datos y operaciones CRUD para las monas chinas

# Base de datos inicial con una mona por default
mona_database = {
    "luna": {
        "nombre": "Luna",
        "tipo": "Rápida",
        "nivel": 10,
        "velocidad": 7
    }
}

# FUNCIONES CRUD

# Agregar una mona
def agregar_mona(nombre, datos):
    key = nombre.lower()
    if key in mona_database:
        return False, "La mona ya existe en la base de datos."
    mona_database[key] = datos
    return True, f"Mona {nombre} agregada a la base de datos."

# Eliminar una mona
def eliminar_mona(nombre):
    key = nombre.lower()
    if key not in mona_database:
        return False, "La mona no existe en la base de datos."
    nombre_mona = mona_database[key]["nombre"]
    del mona_database[key]
    return True, f"Mona {nombre_mona} eliminada de la base de datos."

# Buscar una mona
def buscar_mona(nombre):
    key = nombre.lower()
    if key not in mona_database:
        return False, "La mona no existe en la base de datos."
    return True, mona_database[key]

# Obtener todas las monas
def obtener_todas_monas():
    return sorted(mona_database.values(), key=lambda x: x['nombre'])

# Actualizar una mona
def actualizar_mona(nombre, nuevos_datos):
    key = nombre.lower()
    if key not in mona_database:
        return False, "La mona no existe en la base de datos."
    mona_database[key].update(nuevos_datos)
    return True, f"Mona {mona_database[key]['nombre']} actualizada en la base de datos."

# Verificar si existe una mona
def mona_existe(nombre):
    return nombre.lower() in mona_database

# Contar cuántas monas hay
def total_monas():
    return len(mona_database)
