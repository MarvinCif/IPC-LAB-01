#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que realice operaciones aritméticas.
#Entrada: Numero1, Numero2, Numero3.
""" PROCESO
1. Solicitar al usuario tres numeros.
2. Desplagar un menu de opciones para el usuario.
"""
""" SALIDA
3. Resultado de operacion 1
4. Resultado de operacion 2
5. Resultado de operacion 3
6. Resultado de operacion 4
7. Resultado de formula cuadratica.
8. Salir.
"""
import math
import os
while True:
    os.system('cls')
    print ("Ejercicio 3: Jerarquia de operaciones")
    Numero1=int(input("Ingrese un numero (A): "))
    Numero2=int(input("Ingrese un numero (B): "))
    Numero3=int(input("Ingrese un numero (C): "))

    menu=int(input("\nELIJA UNA OPCION DEL MENU\n\n1- a*b+c\n2- a*(b+c)\n3- a/(b*c)\n4- (3a + 2b)/c^2\n5- Formula cuadratica (Encontrar soluciones)\n6- Salir -6\n\nOpcion: "))
    try:
        if(menu==1):
            print("Operacion 1: ", Numero1*Numero2+Numero3)
        elif(menu==2):
            print("Operacion 2: ", Numero1*(Numero2+Numero3))
        elif(menu==3):
            print("Operacion 3: ", (Numero1)/(Numero2*Numero3))
        elif(menu==4):
            try:
                print("Operacion 4: ", (3*Numero1+2*Numero2)/(Numero3**2))
            except ZeroDivisionError:
                print("No se puede dividir entre cero")
        elif(menu==5):
            try:
                print("FORMULA CUADRATICA")
                discriminante =  Numero1**2 - 4 * Numero1 * Numero3
                if discriminante < 0:
                    print('La ecuación no tiene solución en el campo de los numeros reales.')
                else:    
                    sol1 = (-Numero1 + math.sqrt(discriminante)) / (2 * Numero1)
                    if(discriminante != 0):
                        sol2 = (-Numero1 - math.sqrt(discriminante)) / (2 * Numero1)
                        print("\nSolucion 1: ", sol1)
                        print("Solucion 2: ", sol2)
                    else:
                        print("\nSolucion unica: ", sol1)
            except ZeroDivisionError:
                print("No se puede dividir entre cero.")
        elif(menu==6):
            break
        else:
            print("El valor ingresado no se encuentra dentro del rango.")
    except ValueError:
        print("El valor ingresado no es un numero.")
    bucle=input("\n\nDesea realizar otra operacion? S/N:  ")
    if bucle.upper() != "S":
        exit()
