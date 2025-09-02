from database import *
from validaciones import *
from config import *
import random
import time

def limpiar_pantalla():
    print("\n" * 50)

def mostrar_menu_principal():
    print("="*60)
    print("🏁 CARRERA DE MONAS CHINAS")
    print("="*60)
    print("1. Agregar Mona")
    print("2. Eliminar Mona")
    print("3. Buscar Mona")
    print("4. Listar todas las Monas")
    print("5. Actualizar Mona")
    print("6. Ver tipos disponibles")
    print("7. Estadísticas")
    print("8. Jugar carrera")
    print("9. Ver logros")
    print("10. Salir")
    print("="*60)

def mostrar_tipos_monas():
    print("\nTipos disponibles:")
    for i, tipo in enumerate(tipos_monas,1):
        print(f"{i}. {tipo}")

def mostrar_estadisticas():
    monas = obtener_todas_monas()
    print(f"\nTotal de Monas: {len(monas)}")
    for mona in monas:
        print(f"{mona['nombre']} - Nivel {mona['nivel']} - Velocidad {mona['velocidad']} - Puntos {mona['puntos']}")

def mostrar_logros():
    monas = obtener_todas_monas()
    print("\n📋 LOGROS")
    for mona in monas:
        print(f"\n{mona['nombre']}:")
        for logro in logros_disponibles:
            estado = "✅ Desbloqueado" if logro in mona['logros'] else "❌ No desbloqueado"
            print(f"   {logro}: {estado}")


def solicitar_datos_mona():
    datos = {}
    while True:
        nombre = input("Nombre de la Mona: ").strip()
        valido, mensaje = validar_nombre(nombre)
        if valido:
            datos['nombre'] = mensaje
            break
        print(f"❌ {mensaje}")

    while True:
        print(f"\nTipos disponibles: {', '.join(tipos_monas)}")
        tipo = input("Tipo de Mona: ").strip()
        valido, mensaje = validar_tipo(tipo)
        if valido:
            datos['tipo'] = mensaje
            break
        print(f"❌ {mensaje}")
    
    # Nivel y velocidad inicial
    datos['nivel'] = 1
    datos['velocidad'] = 1
    datos['puntos'] = 0
    datos['logros'] = []
    return True, datos

def menu_agregar_mona():
    print("\n➕ AGREGAR NUEVA MONA")
    exito, datos = solicitar_datos_mona()
    if not exito:
        print("Error al ingresar los datos")
        return
    exito, mensaje = agregar_mona(datos['nombre'], datos)
    print(mensaje)

def menu_eliminar_mona():
    nombre = input("Nombre de la Mona a eliminar: ").strip()
    if not mona_existe(nombre):
        print("❌ Mona no encontrada")
        return
    exito, mensaje = eliminar_mona(nombre)
    print(mensaje)

def menu_buscar_mona():
    nombre = input("Nombre de la Mona: ").strip()
    exito, mona = buscar_mona(nombre)
    if not exito:
        print("❌ Mona no encontrada")
        return
    print(f"{mona['nombre']} - Nivel {mona['nivel']} - Velocidad {mona['velocidad']} - Puntos {mona['puntos']}")

def menu_listar_monas():
    monas = obtener_todas_monas()
    if not monas:
        print("❌ No hay Monas registradas")
        return
    for m in monas:
        print(f"{m['nombre']} - Nivel {m['nivel']} - Velocidad {m['velocidad']} - Puntos {m['puntos']}")

def menu_actualizar_mona():
    nombre = input("Nombre de la Mona a actualizar: ").strip()
    if not mona_existe(nombre):
        print("❌ Mona no encontrada")
        return
    exito, mona = buscar_mona(nombre)
    print(f"Actualizando {mona['nombre']}")
    nuevo_tipo = input(f"Nuevo tipo ({mona['tipo']}): ").strip()
    if nuevo_tipo:
        valido, mensaje = validar_tipo(nuevo_tipo)
        if valido:
            mona['tipo'] = mensaje
            actualizar_mona(nombre, mona)
            print("✅ Mona actualizada")
        else:
            print(f"❌ {mensaje}")

def menu_jugar():
    
    print("\n🏁 CARRERA DE MONAS")
    jugador = input("Seleccione tu Mona: ").strip()
    exito, mona_jugador = buscar_mona(jugador)
    if not exito:
        print("❌ Mona no encontrada")
        return

    rivales = [m for m in obtener_todas_monas() if m['nombre'] != mona_jugador['nombre']]
    if not rivales:
        rivales = [
            {'nombre':'Rival1','tipo':'Fuerte','nivel':1,'velocidad':random.randint(1,5),'puntos':0,'logros':[]},
            {'nombre':'Rival2','tipo':'Astuta','nivel':1,'velocidad':random.randint(1,5),'puntos':0,'logros':[]}
        ]

    participantes = [mona_jugador] + rivales
    meta = 30
    posiciones = {m['nombre']:0 for m in participantes}

    ganador = None
    while not ganador:
        limpiar_pantalla()
        for m in participantes:
            avance = random.randint(1, m['velocidad'])
            posiciones[m['nombre']] += avance
            if posiciones[m['nombre']] >= meta and not ganador:
                ganador = m
        
        for m in participantes:
            pos = min(posiciones[m['nombre']], meta)
            # nombre con padding hasta 20 caracteres + barra de pasos
            nombre_padding = m['nombre'].ljust(20)
            print(f"{nombre_padding}: " + "→"*pos)
        
        time.sleep(0.3)


    print(f"\n🏆 ¡Ganador: {ganador['nombre']}!")
    if ganador['nombre']==mona_jugador['nombre']:
        mona_jugador['puntos'] += 10
        if mona_jugador['velocidad']<velocidad_maxima:
            mona_jugador['velocidad'] += 1
        if "Primer Victoria" not in mona_jugador['logros']:
            mona_jugador['logros'].append("Primer Victoria")
        print("🎉 ¡Ganaste! Velocidad aumentada y puntos otorgados.")
    else:
        print("😢 Ganaste otro día. ¡Sigue intentando!")
    actualizar_mona(mona_jugador['nombre'], mona_jugador)
