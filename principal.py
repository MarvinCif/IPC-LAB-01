#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Mejía
#Objetivo:Crear un programa que realice conversiones de una unidad de longitud en cm a otra.
#Entrada: Cantidad en centimetros a convertir.
""" PROCESO
1. Solicitar al usuario que ingrese una cantidad en cm a convertir.
2. Mostrar un menu de opciones de conversion y solicitar al usuario que seleccione una opcion.
"""
""" SALIDA
3. Resultado de la conversion a otra unidad de medida.
"""

# importar el código fuente del módulo indicado
import conversiones
import os #Libreria 'os' se utilizo solo para dar una mejor presentacion al programa.

while True:

    os.system('cls')
    
    # pedir al usuario la cantidad a convertir
    centimetros = float(input("Ingrese una cantidad en centímetros: "))

    # Mostrar un menú de opciones
    print("\nSeleccione la conversión que desea realizar:")
    print("1. Convertir a metros")
    print("2. Convertir a kilómetros")
    print("3. Convertir a pulgadas")
    print("4. Convertir a pies")
    print("5. Salir")
    opcion = int(input("\n\nIngrese el número de la opción deseada: "))

    # Realizar la conversión según la opción seleccionada
    if opcion == 1:
        metros = conversiones.centimetroAmetro(centimetros)
        print(f"{centimetros} cm equivale a {metros:.2f} m")
        input("Presione una tecla para continuar...")
    elif opcion == 2:
        kilometro = conversiones.centimetroAkilometro(centimetros)
        print(f"{centimetros} cm equivale a {kilometro} km")
        input("Presione una tecla para continuar...")
    elif opcion == 3:
        pulgadas = conversiones.centimetroApulgada(centimetros)
        print(f"{centimetros} cm equivale a {pulgadas:.2f} in")
        input("Presione una tecla para continuar...")
    elif opcion == 4:
        pies = conversiones.centimetroApie(centimetros)
        print(f"{centimetros} cm equivale a {pies:.2f} ft")
        input("Presione una tecla para continuar...")
    elif opcion == 5:
        print("\nGracias por utilizar el programa!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        input("Presione una tecla para continuar...")

