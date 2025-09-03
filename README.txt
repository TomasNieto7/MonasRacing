-Monas con Carreras y Logros

Este proyecto es de monas chinas hecho en Python, que permite registrar personajes, hacerlos competir en carreras, ganar puntos y desbloquear logros.

-Características principales

    1.Gestión de Monas

    2.Agregar monas con validaciones de nombre, tipo, nivel, ataque y generación.

    3.Buscar monas por nombre.

    4.Listar todas las monas registradas.

    5.Actualizar atributos de una mona (nivel, ataque, tipo, generación).

    6.Eliminar monas de la base de datos.

    7.Mostrar estadísticas generales.

    8.Conseguir y mostrar logros

-Modo de juego: Carreras de Monas

    -Participan monas ya registradas en la base de datos.

    -Cada mona empieza con velocidad 1 y nivel 1 por defecto.

    -Compiten en una pista horizontal hasta llegar a la meta.

    -Los nombres ocupan siempre 20 caracteres (alineados con espacios), y los pasos (→) comienzan en la posición 21, para que nadie tenga ventaja.

    -Si tu mona gana, obtienes puntos para mejorar su velocidad.

-Sistema de logros desbloqueables

    -Primera Victoria: cuando ganas tu primera carrera.

    -Velocidad Maxima: cuando una mona alcanza velocidad maxima.

    -Ganador de 5 carreras: Ganar 5 carreras

-Base de datos persistente (JSON)
Toda la información de las monas (nivel, velocidad, logros) se guarda automáticamente.

-Instalación y uso

Asegúrate de tener Python 3.8+ instalado.

python --version


Ejecuta el programa principal:

python main.py

-Menú principal

Cuando ejecutes el programa verás este menú:

- Sistema de Gestión de Monas
============================================================
🏁 CARRERA DE MONAS CHINAS
============================================================
1. Agregar Mona
2. Eliminar Mona
3. Buscar Mona
4. Listar todas las Monas
5. Actualizar Mona
6. Ver tipos disponibles
7. Estadísticas
8. Jugar carrera
9. Ver logros
10. Salir
============================================================

-Tecnologías utilizadas

    -Python 3

    -JSON para la base de datos

Programación modular:

    -config.py → configuración general

    -database.py → base de datos

    -validaciones.py → validaciones de entrada

    -interfaz.py → menús e interacción

    -main.py → programa principal

    -test.py → prueba todas las validaciones de entrada
