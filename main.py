"""
PROGRAMA PRINCIPAL - CARRERA DE MONAS CHINAS
"""
from interfaz import *

def main():
    """Función principal del programa"""
    print("¡Bienvenido al Sistema de Gestión de Monas Chinas!")
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("\nSeleccione una opción (1-8): ").strip()
            
            if opcion == "1":
                menu_agregar_mona()
            elif opcion == "2":
                menu_eliminar_mona()
            elif opcion == "3":
                menu_buscar_mona()
            elif opcion == "4":
                menu_listar_monas()
            elif opcion == "5":
                menu_actualizar_mona()
            elif opcion == "6":
                mostrar_tipos_monas()
            elif opcion == "7":
                mostrar_estadisticas()
            elif opcion == "8":
                print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida. Por favor, elija 1-8.")
            
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Programa interrumpido por el usuario! ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

if __name__ == "__main__":
    main()
