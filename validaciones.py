# validaciones.py
from config import *

# Verificar que el nombre exista y cumpla las reglas
def validar_nombre(nombre):
    if not isinstance(nombre, str) or nombre.strip() == '':
        return False, mensaje_error["nombre_vacio"]
    nombre = nombre.strip()
    if len(nombre) < longitud_minima_nombre or len(nombre) > longitud_maxima_nombre:
        return False, mensaje_error["nombre_longitud"]
    if not nombre[0].isupper():
        return False, mensaje_error["nombre_mayuscula"]
    for char in nombre:
        if not char.isalpha() and char != '-':
            return False, mensaje_error["nombre_caracteres"]
    return True, nombre

# Validar tipo de mona
def validar_tipo(tipo):
    if not isinstance(tipo, str) or tipo.strip() == '':
        return False, mensaje_error["tipo_vacio"]
    tipo = tipo.strip()
    if tipo not in tipos_monas:
        return False, mensaje_error["tipo_invalido"]
    return True, tipo

# Validar nivel
def validar_nivel(nivel):
    try:
        nivel = int(nivel)
        if nivel < nivel_minimo or nivel > nivel_maximo:
            return False, mensaje_error["nivel_rango"]
        return True, nivel
    except ValueError:
        return False, mensaje_error["nivel_numero"]

# Validar velocidad
def validar_velocidad(velocidad):
    try:
        velocidad = int(velocidad)
        if velocidad < velocidad_minima or velocidad > velocidad_maxima:
            return False, mensaje_error["velocidad_rango"]
        return True, velocidad
    except ValueError:
        return False, mensaje_error["velocidad_numero"]

# Validar todos los datos juntos
def validar_datos_completos(datos):
    try:
        valido, mensaje = validar_nombre(datos['nombre'])
        if not valido:
            return False, mensaje
        valido, mensaje = validar_tipo(datos['tipo'])
        if not valido:
            return False, mensaje
        valido, mensaje = validar_nivel(datos['nivel'])
        if not valido:
            return False, mensaje
        valido, mensaje = validar_velocidad(datos['velocidad'])
        if not valido:
            return False, mensaje
        return True, "Datos válidos"
    except KeyError as e:
        return False, f"Falta el campo {str(e)} en los datos."
    except Exception as e:
        return False, f"Error inesperado: {str(e)}"
