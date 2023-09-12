#Introducción a programación - Sección:17
#12/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que solicite un numero entero y devuelva si es positivo, negativo o cero.
#Entrada: Numero1
""" PROCESO
1. Solicitar al usuario un numero entero según el día de la semana (1 al 7)
2. Determinar el día de la semana en que nos encontramos.
"""
""" SALIDA
Si no es un número devolver el mensaje "El valor ingresado no es un número".
Si no se encuentra en el rango devolver el mensaje "El numero no se encuentra en el rango solicitado.
Devolver el día de acuerdo al número ingresado 1-Lunes 2-Martes 3-Miercoles 4-Jueves 5-Viernes
"""

print("Ejercicio #2 \nDías de la semana\n")

try:
    Numero1=int(input("Ingrese el número de día de la semana (1 al 7): "))
    if(Numero1==1):
        print("El día de hoy es lunes")
    elif(Numero1==2):
        print("El día de hoy es martes")
    elif(Numero1==3):
        print("El día de hoy es miercoles")
    elif(Numero1==4):
        print("El día de hoy es jueves")
    elif(Numero1==5):
        print("El día de hoy es viernes")
    elif(Numero1==6):
        print("El día de hoy es sabado")
    elif(Numero1==7):
        print("El día de hoy es domingo")
    else:
        print("El valor ingresado no se encuentra en el rango solicitado.")
except ValueError:
    print("El valor ingresado no es un numero.")