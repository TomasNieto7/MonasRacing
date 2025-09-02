# config.py
# Configuración del proyecto Carrera de Monas Chinas

# Tipos de monas (categorías o habilidades)
tipos_monas = ['Rápida', 'Fuerte', 'Astuta', 'Resistente', 'Veloz', 'Sigilosa']

# Configuración de validaciones
longitud_minima_nombre = 3
longitud_maxima_nombre = 20
nivel_minimo = 1
nivel_maximo = 100
velocidad_minima = 1
velocidad_maxima = 10

# Logros posibles
logros_disponibles = [
    "Primer Victoria",
    "Velocidad Máxima",
    "Ganador de 5 Carreras"
]

# Mensajes de error
mensaje_error = {
    "nombre_vacio": "El nombre no puede estar vacío.",
    "nombre_longitud": f"El nombre debe tener entre {longitud_minima_nombre} y {longitud_maxima_nombre} caracteres.",
    "nombre_mayuscula": "El nombre debe comenzar con mayúscula.",
    "nombre_caracteres": "El nombre solo puede contener letras.",
    "tipo_vacio": "Debe seleccionar al menos un tipo.",
    "tipo_invalido": "Tipo inválido. Elija uno de los tipos disponibles.",
    "nivel_numero": "El nivel debe ser un número entero.",
    "nivel_rango": f"El nivel debe estar entre {nivel_minimo} y {nivel_maximo}.",
    "velocidad_numero": "La velocidad debe ser un número entero.",
    "velocidad_rango": f"La velocidad debe estar entre {velocidad_minima} y {velocidad_maxima}.",
}
