"""
INTERFAZ DE USUARIO Y MENÚS PARA CARRERA DE MONAS CHINAS
"""
from database import *
from validaciones import *
from config import *

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    print("\n" * 50)

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("=" * 60)
    print("🏁 CARRERA DE MONAS CHINAS - Gestión de Monas")
    print("=" * 60)
    print("1. Agregar Mona")
    print("2. Eliminar Mona")
    print("3. Buscar Mona")
    print("4. Listar todas las Monas")
    print("5. Actualizar Mona")
    print("6. Ver tipos disponibles")
    print("7. Estadísticas")
    print("8. Salir")
    print("=" * 60)

def mostrar_tipos_monas():
    """Muestra los tipos disponibles"""
    print("\n" + "=" * 40)
    print("🎨 TIPOS DE MONAS DISPONIBLES")
    print("=" * 40)
    
    for i, tipo in enumerate(tipos_monas, 1):
        print(f"{i:2d}. {tipo}", end="   ")
        if i % 4 == 0:
            print()
    print(f"\n\nTotal: {len(tipos_monas)} tipos disponibles")

def mostrar_estadisticas():
    """Muestra estadísticas del juego"""
    total = total_monas()
    monas = obtener_todas_monas()
    
    print("\n" + "=" * 40)
    print("📊 ESTADÍSTICAS DE LAS MONAS")
    print("=" * 40)
    
    print(f"Total de Monas: {total}")
    
    # Contar monas por tipo
    tipos_contador = {}
    for mona in monas:
        tipo = mona['tipo']
        tipos_contador[tipo] = tipos_contador.get(tipo, 0) + 1
    
    print("\n📈 Monas por tipo:")
    for tipo, cantidad in sorted(tipos_contador.items()):
        print(f"  {tipo}: {cantidad}")

def solicitar_datos_mona():
    """Solicita y valida los datos de una mona"""
    datos = {}
    
    try:
        # Validar nombre
        while True:
            nombre = input("Nombre de la Mona: ").strip()
            valido, mensaje = validar_nombre(nombre)
            if valido:
                datos['nombre'] = mensaje
                break
            print(f"❌ {mensaje}")
        
        # Validar tipo
        while True:
            print(f"\nTipos disponibles: {', '.join(tipos_monas)}")
            tipo = input("Tipo de Mona: ").strip()
            valido, mensaje = validar_tipo(tipo)
            if valido:
                datos['tipo'] = mensaje
                break
            print(f"❌ {mensaje}")
        
        # Validar nivel
        while True:
            nivel = input(f"Nivel ({nivel_minimo}-{nivel_maximo}): ").strip()
            valido, mensaje = validar_nivel(nivel)
            if valido:
                datos['nivel'] = mensaje
                break
            print(f"❌ {mensaje}")
        
        # Validar velocidad
        while True:
            velocidad = input(f"Velocidad ({velocidad_minima}-{velocidad_maxima}): ").strip()
            valido, mensaje = validar_velocidad(velocidad)
            if valido:
                datos['velocidad'] = mensaje
                break
            print(f"❌ {mensaje}")
        
        return True, datos
        
    except KeyboardInterrupt:
        return False, "Operación cancelada por el usuario"
    except Exception as e:
        return False, f"Error inesperado: {e}"

def menu_agregar_mona():
    """Menú para agregar Mona"""
    print("\n" + "=" * 40)
    print("➕ AGREGAR NUEVA MONA")
    print("=" * 40)
    
    exito, resultado = solicitar_datos_mona()
    if not exito:
        print(f"❌ {resultado}")
        return
    
    datos = resultado
    exito, mensaje = agregar_mona(datos['nombre'], datos)
    print(f"\n{mensaje}")

def menu_eliminar_mona():
    """Menú para eliminar Mona"""
    print("\n" + "=" * 40)
    print("🗑️ ELIMINAR MONA")
    print("=" * 40)
    
    nombre = input("Nombre de la Mona a eliminar: ").strip()
    
    if not mona_existe(nombre):
        print("❌ Mona no encontrada")
        return
    
    mona = buscar_mona(nombre)[1]
    print(f"\n📋 Información de la Mona:")
    print(f"   Nombre: {mona['nombre']}")
    print(f"   Tipo: {mona['tipo']}")
    print(f"   Nivel: {mona['nivel']}")
    print(f"   Velocidad: {mona['velocidad']}")
    
    confirmacion = input("\n¿Está seguro de eliminar esta Mona? (s/n): ").lower().strip()
    if confirmacion in ['s', 'si', 'sí']:
        exito, mensaje = eliminar_mona(nombre)
        print(mensaje)
    else:
        print("ℹ️ Eliminación cancelada")

def menu_buscar_mona():
    """Menú para buscar Mona"""
    print("\n" + "=" * 40)
    print("🔍 BUSCAR MONA")
    print("=" * 40)
    
    nombre = input("Nombre de la Mona: ").strip()
    exito, mona = buscar_mona(nombre)
    
    if not exito:
        print("❌ Mona no encontrada")
        return
    
    print(f"\n📋 INFORMACIÓN DE {mona['nombre'].upper()}")
    print("=" * 30)
    for clave, valor in mona.items():
        print(f"{clave.capitalize()}: {valor}")

def menu_listar_monas():
    """Menú para listar Monas"""
    print("\n" + "=" * 40)
    print("📋 LISTA DE MONAS")
    print("=" * 40)
    
    monas = obtener_todas_monas()
    
    if not monas:
        print("❌ No hay Monas registradas")
        return
    
    for i, mona in enumerate(monas, 1):
        print(f"\n{i}. 🎯 {mona['nombre']} (Nivel {mona['nivel']})")
        print(f"   Tipo: {mona['tipo']}")
        print(f"   Velocidad: {mona['velocidad']}")
    
    print(f"\nTotal: {len(monas)} Monas")

def menu_actualizar_mona():
    """Menú para actualizar Mona"""
    print("\n" + "=" * 40)
    print("✏️ ACTUALIZAR MONA")
    print("=" * 40)
    
    nombre = input("Nombre de la Mona a actualizar: ").strip()
    
    if not mona_existe(nombre):
        print("❌ Mona no encontrada")
        return
    
    mona = buscar_mona(nombre)[1]
    print(f"\nEditando: {mona['nombre']}")
    
    print("\nValores actuales:")
    campos = [
        ("nivel", "Nivel", str(mona['nivel']), validar_nivel),
        ("velocidad", "Velocidad", str(mona['velocidad']), validar_velocidad),
        ("tipo", "Tipo", mona['tipo'], validar_tipo)
    ]
    
    for i, (clave, nombre_campo, valor_actual, _) in enumerate(campos, 1):
        print(f"{i}. {nombre_campo}: {valor_actual}")
    
    try:
        opcion = int(input("\n¿Qué campo desea actualizar? (1-3): "))
        if opcion < 1 or opcion > 3:
            print("❌ Opción no válida")
            return
        
        clave, nombre_campo, valor_actual, validador = campos[opcion - 1]
        nuevo_valor = input(f"Nuevo valor para {nombre_campo} ({valor_actual}): ").strip()
        
        if nuevo_valor:
            valido, resultado = validador(nuevo_valor)
            if valido:
                exito, mensaje = actualizar_mona(nombre, {clave: resultado})
                print(mensaje)
            else:
                print(f"❌ {resultado}")
        else:
            print("ℹ️ No se realizaron cambios")
            
    except ValueError:
        print("❌ Ingrese un número válido")
    except Exception as e:
        print(f"❌ Error: {e}")
