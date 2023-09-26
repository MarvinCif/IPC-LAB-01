#Introducción a programación - Sección:17
#12/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que solicite un numero entero y devuelva si es positivo, negativo o cero.
#Entrada: Numero1
""" PROCESO
1. Solicitar al usuario un numero entero
2. Determinar si el dato es positivo, negativo o cero.
"""
""" SALIDA
3. Si no es un número devolver el mensaje "El valor ingresado no es un número".
3. Devolver el número ingresado, seguido de "Numero" positivo, negativo o cero.
"""

try:
    print("Ejercicio #1 \nDeterminar el tipo de dato (Positivo, negativo o cero)\n")
    Numero1=int(input("Ingrese un numero entero: "))

    if(Numero1 < 0):
            print(Numero1," es un numero negativo")
    elif(Numero1 == 0):
            print(Numero1," es el numero cero")
    else:
            print(Numero1," es un numero positivo")

except ValueError:
        print("El valor ingresado no es un numero.")
        

SystemExit
