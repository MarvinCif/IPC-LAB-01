#TS Introducción a programación - Sección:17
#21/09/2023
#Marvin Estuardo Cifuentes Mejía
#Objetivo:Solicitar al usuario un numero en el rango de 1 a 10 y devolver la tabla de multiplicar del numero.
#Entrada: Numero1.
""" PROCESO
1. Solicitar al usuario un numero 1-10
2. Mostrar de la tabla de multiplicar del numero del usuario.
3. Verificar si el dato ingresado es un numero o se encuentra dentro del rango.
"""
""" SALIDA
4. Tabla de multiplicar
[nx1,nx2,nx3,nx4,nx5,nx6,nx7,nx8,nx9,nx10]
5. Preguntar si quiere realizar otra operacion.
"""
import os
while True:
    os.system('cls')
    print("MARVIN ESTUARDO CIFUENTES MEJIA\nACTIVIDAD NO.5\nTABLA DE MULTIPLICAR\n")
    try:
        Numero1=int(input("Ingrese un numero del 1 al 10: "))
        if Numero1>=1 and Numero1<=10:
                print("TABLA DEL", Numero1)
                for i in [0,1,2,3,4,5,6,7,8,9,10]:
                    print(f"{i} X {Numero1} = {i*Numero1}")
        else:
            print("El valor ingresado no se encuentra dentro del rango")
    except ValueError:
        print("El valor ingresado no es un numero.")
    bucle=input("\n\nDesea realizar otra operacion? S/N:  ")
    if bucle.upper() != "S":
        break
SystemExit
