import os

# Creamos el tablero
filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
columnas = ["   1  ","2  ","3  ","4  ","5  ","6  ","7  ","8  ","9  ","10"]

# Función para mostrar el tablero
def MostrarTablero(tablero):
    print(" " + " ".join(map(str, columnas)))
    for fila, fila_tablero in zip(filas, tablero):
        print(fila + " | " + " | ".join(fila_tablero) + " | ")

def MostrarTableroEnemigo(tablero):
    tablero_enemigo = [[' ' for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if tablero[i][j] == 'x' or tablero[i][j] == 'o':
                tablero_enemigo[i][j] = tablero[i][j]
    
    print(" " + " ".join(map(str, columnas)))
    for fila, fila_tablero in zip(filas, tablero_enemigo):
        print(fila + " | " + " | ".join(fila_tablero) + " | ")


# Función para que el jugador coloque sus barcos
def colocar_barcos(jugador):
    try:
        os.system('cls')
        print(f"Jugador {jugador}, coloca tus barcos:")
        barcos = {'barco pequeño': 3, 'barco grande': 2}
        orientacion = {'H': 'Horizontal', 'V': 'Vertical'}
        tablerojugador = []

        for i in range(10):
            tablerojugador.append([' ']*10)

        for barco, cantidad in barcos.items():
            for _ in range(cantidad):
                if barco == 'barco pequeño':
                    tamañobarco = 3
                else:
                    tamañobarco = 5
                print(f"Coloca {barco} ({tamañobarco} casillas):")
                for i in range(10):
                    MostrarTablero(tablerojugador)
                    coordenadas = input(f"Ingresa las coordenadas (por ejemplo, A1) para el {barco}: ")
                    fila = coordenadas[0]
                    columna = int(coordenadas[1:]) - 1
                    orientacion = input(f"Ingresa la orientación (H para Horizontal, V para Vertical) para el {barco}: ")

                    if orientacion not in orientacion:
                        print("Orientación inválida. Inténtalo de nuevo.")
                        input("Presiona Enter para continuar...")
                        continue

                    if orientacion == 'H':
                        if columna + tamañobarco <= 10:
                            valido = True
                            for j in range(tamañobarco):
                                if tablerojugador[filas.index(fila)][columna + j] != ' ':
                                    valido = False
                                    print("Ubicación ocupada. Inténtalo de nuevo.")
                                    break
                            if valido:
                                for j in range(tamañobarco):
                                    tablerojugador[filas.index(fila)][columna + j] = barco[0]
                                break
                        else:
                            print("Colocación fuera de los límites del tablero. Inténtalo de nuevo.")
                    elif orientacion == 'V':
                        if filas.index(fila) + tamañobarco <= 10:
                            valido = True
                            for j in range(tamañobarco):
                                if tablerojugador[filas.index(fila) + j][columna] != ' ':
                                    valido = False
                                    print("Ubicación ocupada. Inténtalo de nuevo.")
                                    break
                            if valido:
                                for j in range(tamañobarco):
                                    tablerojugador[filas.index(fila) + j][columna] = barco[0]
                                break
                        else:
                            print("Colocación fuera de los límites del tablero. Inténtalo de nuevo.")

        return tablerojugador
    except ValueError:
        print("Por favor, ingrese un valor válido")
        return

# Lógica para que un jugador dispare
def disparar(tablero, fila, columna):
    if tablero[fila][columna] == 'b':
        tablero[fila][columna] = 'x'
        print("¡Impacto en el barco!")
        input("Presiona Enter para continuar...")
    else:
        tablero[fila][columna] = 'o'
        print("¡Has fallado!")
        input("Presiona Enter para continuar...")

# Función para verificar al ganador
def VerificarGanador(tablero):
    for fila in tablero:
        if 'b' in fila:
            return None  # El juego aún no ha terminado
    return True  # No hay más barcos, un jugador ha ganado


# Agregamos estas líneas para ejecutar la rama principal si el módulo se ejecuta directamente
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
        
        op = int(input("\nSeleccione una opción: "))
        
        if op == 1:
            os.system('cls')
            print("HAS SELECCIONADO JUGAR\n")
            jugador1 = input("Nombre del Jugador 1: ")
            jugador2 = input("Nombre del Jugador 2: ")
            input("Presiona Enter para continuar...")

            tablerojugador1 = colocar_barcos(jugador1)
            input(f"{jugador1}, has colocado tus barcos. Presiona Enter para continuar.")

            tablerojugador2 = colocar_barcos(jugador2)
            input(f"{jugador2}, has colocado tus barcos. Presiona Enter para continuar.")
            
            # Variable para controlar el turno del jugador
            turno_jugador = 1
            
            while True:
                if turno_jugador == 1:
                    os.system('cls')
                    print("Tu tablero: ")
                    MostrarTablero(tablerojugador1)
                    print("\nTablero de disparos:")
                    MostrarTableroEnemigo(tablerojugador2) 
                    coordenadas = input(f"{jugador1}, es tu turno. Ingresa las coordenadas para disparar (por ejemplo, A1): ")
                    fila = filas.index(coordenadas[0])
                    columna = int(coordenadas[1:]) - 1
                    disparar(tablerojugador2, fila, columna)
                    turno_jugador = 2
                else:
                    os.system('cls')
                    print("Tu tablero:")
                    MostrarTablero(tablerojugador2)
                    print("\nTablero de disparos:")
                    MostrarTableroEnemigo(tablerojugador1)
                    coordenadas = input(f"{jugador2}, es tu turno. Ingresa las coordenadas para disparar (por ejemplo, A1): ")
                    fila = filas.index(coordenadas[0])
                    columna = int(coordenadas[1:]) - 1
                    disparar(tablerojugador1, fila, columna)
                    turno_jugador = 1
                    
                    
                ganador = VerificarGanador(tablerojugador1)
                if ganador:
                    os.system('cls')
                    print(f"¡El jugador {jugador2} ha ganado!")
                    break

                ganador = VerificarGanador(tablerojugador2)
                if ganador:
                    os.system('cls')
                    print(f"\n\n¡El jugador {jugador1} ha ganado!")
                    input("Presiona Enter para continuar")
                    break
        
        elif op == 2:
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
            
        elif op == 3:
            print("¡Gracias por jugar!")
            break
            
        else:
            os.system('cls')
            print("El valor ingresado no se encuentra dentro del rango.")
            input("Presione Enter para continuar...")
            continue