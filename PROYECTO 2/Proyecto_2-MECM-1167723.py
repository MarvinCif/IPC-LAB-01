#Introducción a programación - Sección:17
#14/11/2023
#Marvin Estuardo Cifuentes Mejía - 1167723
#Objetivo: Crear un programa que simule el juego Batalla Naval.
#Entrada: filas, columnas, tablero, coordenadas, coordenada_disparo, nombre, jugador, barco, orientacion, turno, opcion.
"""ENTRADA
1. Solicitar la opción al usuario (1. Jugar, 2. Instrucciones, 3. Salir).
2. Ingresar la opción seleccionada.
3. Ingresar los nombres de los jugadores.
4. Iniciar el juego y mostrar el tablero vacío.
5. En cada turno de colocar barcos:
   a. Mostrar el tablero del jugador.
   b. Solicitar coordenadas para colocar barco.
   c. Validar las coordenadas y orientación.
   d. Colocar el barco en el tablero si es válido.
   e. Repetir hasta colocar todos los barcos.
6. En cada turno de disparo:
   a. Mostrar el tablero del jugador en turno.
   b. Mostrar el tablero de disparos.
   c. Solicitar coordenadas para disparar.
   d. Validar las coordenadas.
   e. Procesar el disparo (impacto o fallo).
   f. Cambiar de turno.
   g. Verificar si hay un ganador.
   h. Repetir hasta que haya un ganador.
"""
"""SALIDA
1. Mostrar un mensaje de error si se ingresa una opción no válida. (menu principal)
2. Mostrar el mensaje de bienvenida al juego de Batalla Naval. (menu principal)
3. Mostrar las instrucciones del juego. (opcion 2)
4. Limpiar la pantalla y mostrar el menú principal. (al finalizar un proceso)
5. Mostrar un mensaje indicando la opción seleccionada. (según la opcion)
6. Mostrar un mensaje indicando que se ha seleccionado jugar. (opcion 1)
7. Mostrar los nombres de los jugadores y solicitar que coloquen sus barcos. (opcion 1)
8. Mostrar el tablero actualizado con los barcos colocados. (opcion 1)
9. Mostrar el tablero actualizado después del disparo. (opcion 1)
10. Mostrar el resultado del disparo y si se hundió un barco. (opcion 1)
11. Indicar el cambio de turno y mostrar el tablero actualizado. (opcion 1)
12. Mostrar el resultado del disparo (¡Has fallado! o ¡Impacto en el barco!). (opcion 1)
13. Mostrar el tablero actualizado. (opcion 1)
14. Indicar que el jugador ha ganado el juego. (opcion 1)
15. Mostrar un mensaje de agradecimiento por jugar. (opcion 1)
"""

import os

class Tablero:
    def __init__(self):
        self.filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.columnas = ["   1  ","2  ","3  ","4  ","5  ","6  ","7  ","8  ","9  ","10"]
        self.tablero = [[' ' for i in range(10)] for i in range(10)]

    #Funcion para mostrar el tablero enconsola.
    def mostrar_tablero(self):
        print(" " + " ".join(map(str, self.columnas)))
        for fila, fila_tablero in zip(self.filas, self.tablero):
            print(fila + " | " + " | ".join(fila_tablero) + " | ")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero_jugador = Tablero()
        self.tablero_disparos = Tablero()  # Agregar un tablero para los disparos del jugador
        self.oponente = None  # Agregar una propiedad para almacenar la referencia al oponente


    #Funcion para colocar los barcos en el tablero.
    def colocar_barcos(self):
        print(f"{self.nombre}, coloca tus barcos:")
        barcos = {'barco pequeño': 3, 'barco grande': 2}

        for barco, cantidad in barcos.items():
            for i in range(cantidad):
                tamaño_barco = 3 if barco == 'barco pequeño' else 5
                print(f"Coloca {barco} ({tamaño_barco} casillas):")

                while True:
                    self.tablero_jugador.mostrar_tablero()
                    coordenadas = input(f"Ingresa las coordenadas (por ejemplo, A1) para el {barco}: ")

                    # Validar que las coordenadas sean válidas
                    if len(coordenadas) < 2 or coordenadas[0] not in self.tablero_jugador.filas or not coordenadas[1:].isdigit() or not (1 <= int(coordenadas[1:]) <= 10):
                        print("Coordenadas inválidas. Inténtalo de nuevo.")
                        continue

                    fila = coordenadas[0]
                    columna = int(coordenadas[1:]) - 1

                    orientacion = input(f"Ingresa la orientación (H para Horizontal, V para Vertical) para el {barco}: ")

                    if orientacion not in ['H', 'V']:
                        print("Orientación inválida. Inténtalo de nuevo.")
                        continue

                    if orientacion == 'H':
                        if columna + tamaño_barco <= 10 and all(self.tablero_jugador.tablero[self.tablero_jugador.filas.index(fila)][columna + j] == ' ' for j in range(tamaño_barco)):
                            for j in range(tamaño_barco):
                                self.tablero_jugador.tablero[self.tablero_jugador.filas.index(fila)][columna + j] = barco[0]
                            break
                        else:
                            print("Colocación fuera de los límites del tablero o casillas ocupadas. Inténtalo de nuevo.")
                    elif orientacion == 'V':
                        if self.tablero_jugador.filas.index(fila) + tamaño_barco <= 10 and all(self.tablero_jugador.tablero[self.tablero_jugador.filas.index(fila) + j][columna] == ' ' for j in range(tamaño_barco)):
                            for j in range(tamaño_barco):
                                self.tablero_jugador.tablero[self.tablero_jugador.filas.index(fila) + j][columna] = barco[0]
                            break
                        else:
                            print("Colocación fuera de los límites del tablero o casillas ocupadas. Inténtalo de nuevo.")
                    else:
                        print("Error inesperado al procesar la orientación. Inténtalo de nuevo.")
                        continue


    #Funcion para realizar los disparos.
    def disparar(self, oponente, coordenadas):
        while True:
            # Validar que las coordenadas ingresadas sean correctas y no estén vacías
            if not coordenadas or coordenadas[0] not in self.tablero_disparos.filas or not coordenadas[1:].isdigit() or not (1 <= int(coordenadas[1:]) <= 10):
                print("Coordenadas inválidas. Inténtalo de nuevo.")
                return False

            # Corregir la obtención de la fila restando 1 al índice
            fila = self.tablero_disparos.filas.index(coordenadas[0])
            columna = int(coordenadas[1:]) - 1

            # Verificar si ya se ha disparado a esta ubicación
            if self.tablero_disparos.tablero[fila][columna] != ' ':
                print("Ya has disparado a esta ubicación. Inténtalo de nuevo.")
                return False

            # Procesar el disparo
            if oponente.tablero_jugador.tablero[fila][columna] == ' ':
                oponente.tablero_jugador.tablero[fila][columna] = 'o'
                self.tablero_disparos.tablero[fila][columna] = 'o'  # Actualizar tablero de disparos
                print("¡Has fallado!")
            elif oponente.tablero_jugador.tablero[fila][columna] == 'b':
                oponente.tablero_jugador.tablero[fila][columna] = 'x'
                self.tablero_disparos.tablero[fila][columna] = 'x'  # Actualizar tablero de disparos
                print("¡Impacto en el barco!")

            return True

    def get_tablero(self):
        return self.tablero_jugador

class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.jugador1.oponente = jugador2  # Establecer la referencia al oponente para cada jugador
        self.jugador2.oponente = jugador1
        self.turno_jugador = jugador1  # Inicializar con el jugador1

    #Funcion para realizar los cambios de turno
    def cambiar_turno(self):
        self.turno_jugador = self.jugador2 if self.turno_jugador == self.jugador1 else self.jugador1
    
    #Funcion para verificar un ganador.
    def verificar_ganador(self):
        jugador = self.jugador1 if self.turno_jugador == self.jugador1 else self.jugador2
        oponente = self.jugador2 if self.turno_jugador == self.jugador1 else self.jugador1

        for fila in oponente.tablero_jugador.tablero:
            if 'b' in fila:
                return False  # Aún hay barcos sin hundir

        print(f"¡El jugador {jugador.nombre} ha ganado!")
        input("Presiona Enter para continuar...")
        return True  # No hay más barcos, un jugador ha ganado


    
#Contructor y rama principal del programa (Menu de opciones)
if __name__ == "__main__":
    while True:
        os.system('cls')
        print("""
 ____    __  _________ _________ ___             _____  _   __  _  ______
| __ )  / \  |___  __| |___  __| |  |      ___  |  __| | |__| || ||  __  |
|  _ \ / _ \    | |       | |    |  |     / _ ] |__  | | ___  || ||  ____|
| |_) / ___ \   | |       | |    |  |____|  __/ ___| | | |  | || ||  |
|____/_/   \_\  |_|       |_|    |______| \___| |___ | |_|  |_||_||__|
    
Autor: Marvin Cifuentes
PROYECTO NO.2
            """)

        print("SELECCIONE UNA OPCIÓN")
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            os.system('cls')
            print("HAS SELECCIONADO JUGAR\n")
            nombre_jugador1 = input("Nombre del Jugador 1: ")
            nombre_jugador2 = input("Nombre del Jugador 2: ")
            jugador1 = Jugador(nombre_jugador1)
            jugador2 = Jugador(nombre_jugador2)
            juego = Juego(jugador1, jugador2)

            jugador1.colocar_barcos()
            input(f"{nombre_jugador1}, has colocado tus barcos. Presiona Enter para continuar.")

            jugador2.colocar_barcos()
            input(f"{nombre_jugador2}, has colocado tus barcos. Presiona Enter para continuar.")
            
            turno_jugador = 1
            
            while True:
                os.system('cls')
                print(f"Es el turno de {juego.turno_jugador.nombre}")
                print("Tu tablero: ")
                juego.turno_jugador.tablero_jugador.mostrar_tablero()
                print("\nTablero de disparos:")
                juego.turno_jugador.tablero_disparos.mostrar_tablero()  # Mostrar tablero de disparos

                coordenadas = input("Ingresa las coordenadas para disparar (por ejemplo, A1): ")

                if juego.turno_jugador.disparar(juego.turno_jugador.oponente, coordenadas):
                    if juego.verificar_ganador():
                        break

                    input("Presiona Enter para continuar...")
                    juego.cambiar_turno()

                else:
                    input("Presiona Enter para intentar de nuevo...")

            print("¡Gracias por jugar!")

        elif opcion == 2:
            os.system('cls')
            print("¡Bienvenido al juego de Batalla Naval!\n\n")
            print("INSTRUCCIONES")
            print("""
1. Inicio del Juego:
    Al iniciar el juego, se le pedirá a los jugadores que ingresen sus nombres.

2. Colocación de Barcos:
    - Cada jugador debe colocar sus barcos en el tablero por turnos.
    - Existen dos tipos de barcos:
        - Barco Pequeño: Ocupa 3 casillas.
        - Barco Grande: Ocupa 2 casillas.
    - Para colocar un barco, se debe:
        - Elegir una coordenada inicial (por ejemplo, A1).
        - Elegir una orientación para el barco: Horizontal (H) o Vertical (V).
    - Si el barco no cabe en el tablero o si se superpone con otro barco ya colocado, se pedirá que se vuelva a intentar.

3. Turnos para Disparar:
    - Los jugadores dispararán por turnos.
    - En cada turno, se mostrará el tablero del oponente.
    - El jugador en turno debe elegir una coordenada para disparar (por ejemplo, A1).
    - El tablero se actualizará mostrando el resultado del disparo:
        - Si acierta a un barco, la casilla mostrará 'x'.
        - Si falla, la casilla mostrará 'o'.

4. Final del Juego:
    - El juego termina cuando todos los barcos de un jugador han sido hundidos.
    - El jugador opuesto será declarado ganador.

                """)
            input("\nPresione Enter para continuar...")
            continue
            
        elif opcion == 3:
            print("¡Gracias por jugar!")
            break
            
        else:
            os.system('cls')
            print("El valor ingresado no se encuentra dentro del rango.")
            input("Presione Enter para continuar...")
            continue