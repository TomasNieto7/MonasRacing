# database.py
# Base de datos y operaciones CRUD para Monas

import random

# Mona inicial por default
mona_database = {
    "luna": {
        "nombre": "Luna",
        "tipo": "Rápida",
        "nivel": 1,
        "velocidad": 5,
        "puntos": 0,
        "logros": []
    },
    "estrella": {
        "nombre": "Estrella",
        "tipo": "Astuta",
        "nivel": 1,
        "velocidad": 3,
        "puntos": 0,
        "logros": []
    },
}

# FUNCIONES CRUD
def agregar_mona(nombre, datos):
    key = nombre.lower()
    if key in mona_database:
        return False, "La mona ya existe."
    datos.setdefault('nivel', 1)
    datos.setdefault('velocidad', 1)
    datos.setdefault('puntos', 0)
    datos.setdefault('logros', [])
    mona_database[key] = datos
    return True, f"Mona {nombre} agregada."

def eliminar_mona(nombre):
    key = nombre.lower()
    if key not in mona_database:
        return False, "La mona no existe."
    nombre_mona = mona_database[key]["nombre"]
    del mona_database[key]
    return True, f"Mona {nombre_mona} eliminada."

def buscar_mona(nombre):
    key = nombre.lower()
    if key not in mona_database:
        return False, None
    return True, mona_database[key]

def obtener_todas_monas():
    return sorted(mona_database.values(), key=lambda x: x['nombre'])

def actualizar_mona(nombre, nuevos_datos):
    key = nombre.lower()
    if key not in mona_database:
        return False, "La mona no existe."
    mona_database[key].update(nuevos_datos)
    return True, f"Mona {mona_database[key]['nombre']} actualizada."

def mona_existe(nombre):
    return nombre.lower() in mona_database

def total_monas():
    return len(mona_database)
