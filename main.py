from interfaz import *
import sys

def main():
    print("¡Bienvenido a la Carrera de Monas Chinas!")
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1-10): ").strip()
        if opcion=="1":
            menu_agregar_mona()
        elif opcion=="2":
            menu_eliminar_mona()
        elif opcion=="3":
            menu_buscar_mona()
        elif opcion=="4":
            menu_listar_monas()
        elif opcion=="5":
            menu_actualizar_mona()
        elif opcion=="6":
            mostrar_tipos_monas()
        elif opcion=="7":
            mostrar_estadisticas()
        elif opcion=="8":
            menu_jugar()
        elif opcion=="9":
            mostrar_logros()
        elif opcion=="10":
            print("👋 Gracias por jugar. ¡Nunca vuelva y vaya a apostar!")
            sys.exit()
        else:
            print("❌ Opción no válida")
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__=="__main__":
    main()
