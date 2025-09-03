import pytest
from validaciones import (
    validar_nombre,
    validar_tipo,
    validar_nivel,
    validar_velocidad,
    validar_datos_completos,
)
from config import *


# Tests para validar_nombre
def test_nombre_vacio():
    assert validar_nombre("") == (False, mensaje_error["nombre_vacio"])

def test_nombre_muy_corto():
    nombre = "A" * (longitud_minima_nombre - 1)
    assert validar_nombre(nombre) == (False, mensaje_error["nombre_longitud"])

def test_nombre_muy_largo():
    nombre = "A" * (longitud_maxima_nombre + 1)
    assert validar_nombre(nombre) == (False, mensaje_error["nombre_longitud"])

def test_nombre_sin_mayuscula():
    assert validar_nombre("juan") == (False, mensaje_error["nombre_mayuscula"])

def test_nombre_con_caracter_invalido():
    assert validar_nombre("Juan123") == (False, mensaje_error["nombre_caracteres"])

def test_nombre_valido():
    assert validar_nombre("Juan") == (True, "Juan")


# Tests para validar_tipo
def test_tipo_vacio():
    assert validar_tipo("") == (False, mensaje_error["tipo_vacio"])

def test_tipo_invalido():
    assert validar_tipo("Invalido") == (False, mensaje_error["tipo_invalido"])

def test_tipo_valido():
    tipo = tipos_monas[0]
    assert validar_tipo(tipo) == (True, tipo)


# Tests para validar_nivel
def test_nivel_no_es_numero():
    assert validar_nivel("abc") == (False, mensaje_error["nivel_numero"])

def test_nivel_fuera_de_rango():
    assert validar_nivel(nivel_maximo + 1) == (False, mensaje_error["nivel_rango"])

def test_nivel_valido():
    nivel = (nivel_minimo + nivel_maximo) // 2
    assert validar_nivel(nivel) == (True, nivel)


# Tests para validar_velocidad
def test_velocidad_no_es_numero():
    assert validar_velocidad("abc") == (False, mensaje_error["velocidad_numero"])

def test_velocidad_fuera_de_rango():
    assert validar_velocidad(velocidad_maxima + 1) == (False, mensaje_error["velocidad_rango"])

def test_velocidad_valida():
    velocidad = (velocidad_minima + velocidad_maxima) // 2
    assert validar_velocidad(velocidad) == (True, velocidad)


# Tests para validar_datos_completos
def test_datos_incompletos_nombre():
    datos = {"nombre": "", "tipo": tipos_monas[0], "nivel": 5, "velocidad": 5}
    assert validar_datos_completos(datos) == (False, mensaje_error["nombre_vacio"])

def test_datos_incompletos_tipo():
    datos = {"nombre": "Juan", "tipo": "Invalido", "nivel": 5, "velocidad": 5}
    assert validar_datos_completos(datos) == (False, mensaje_error["tipo_invalido"])

def test_datos_incompletos_nivel():
    datos = {"nombre": "Juan", "tipo": tipos_monas[0], "nivel": 0, "velocidad": 5}
    assert validar_datos_completos(datos) == (False, mensaje_error["nivel_rango"])

def test_datos_incompletos_velocidad():
    datos = {"nombre": "Juan", "tipo": tipos_monas[0], "nivel": 5, "velocidad": 0}
    assert validar_datos_completos(datos) == (False, mensaje_error["velocidad_rango"])

def test_datos_completos_validos():
    datos = {"nombre": "Juan", "tipo": tipos_monas[0], "nivel": nivel_minimo, "velocidad": velocidad_minima}
    assert validar_datos_completos(datos) == (True, "Datos válidos")
