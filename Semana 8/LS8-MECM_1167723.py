#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que realice factoriales y secuencia de fibonacci.
#Entrada: Numero1, Numero2
""" PROCESO
1. Inicio del conjunto de instrucciones
2. Desplagar un menu de opciones para el usuario. (1- Factorial,2- Secuencia de Fibonacci,3- Salir)
3. Solicitar al usuario el numero de opcion que quiere ejecutar.
4. 
    Opción 1: Pedir al usuario que ingrese un numero
    Opción 2: Pedir al usuario que ingrese un numero
"""
""" SALIDA
5. 
    Opción 1: Mostrar la secuencia y cálculo del factorial del numero.
    Opción 2: Mostrar la secuencia de Fibonacci del numero ingresado.
6. Volver al inicio del conjunto de instrucciones
"""
import math
import os
while True:
    try:
        os.system('cls')
        print ("LS 8 - FACTORIAL Y SECUENCIA DE FIBONACCI\n")
        print("1- Factorial\n2- Secuencia de Fibonacci\n3- Salir")
        Numero1=int(input("Seleccione una opción: "))
        try:
            if (Numero1 == 1):
                os.system('cls')
                print("OPCION FACTORIAL")
                try:
                    Numero2=int(input("Ingrese un numero: "))
                    if Numero2 < 0:
                        print("NO EXISTEN LOS FACTORIALES NEGATIVOS\n\n")
                        os.system('PAUSE')
                    else:
                        contador = 1
                        while contador <= Numero2:
                            print(f"{contador}",end='')
                            contador = contador + 1
                            if (contador<=Numero2):
                                print(" X ", end='')
                            else:
                                print(" = ", math.factorial(Numero2), "\n\n")
                                os.system('PAUSE')
                        else:
                            print(math.factorial(Numero2))
                except ValueError:
                    print("El valor ingresado no es un numero\n\n")
                    os.system('PAUSE')
            elif(Numero1 == 2):
                os.system('cls')
                def fibonacci(n):
                    fibseq = list([])
                    a, b = 0, 1
                    for _ in range(n):
                        fibseq.append(a)
                        a, b = b, a + b
                    print(fibseq) 
                try:
                    n = int(input("Ingrese un numero para la secuencia de Fibonacci: "))
                    if n<0:
                        print("Ingrese un numero mayor a 0")
                    else:
                        secuencia = fibonacci(n)
                except ValueError:
                    print("El valor ingresado no es un numero")
                print("\n\n")
                os.system('PAUSE')
            elif(Numero1 ==3):
                os.system('cls')
                print("GRACIAS POR USAR EL PROGRAMA")
                break
            else:
                print("\nEl numero ingresado no se encuentra dentro del rango.\n\n")
                os.system('PAUSE')
        except ValueError:
            print("El valor ingresado no es un numero.")
    except ValueError:
        os.system('cls')
        print("El valor ingresado no es un numero.\n\n")
        os.system('PAUSE')
