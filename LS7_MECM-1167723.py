#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que realice operaciones aritméticas.
#Entrada: Numero1, Numero2.
""" PROCESO
1. Solicitar al usuario dos numeros enteros y realizar los cálculos (Suma, resta, multiplicacion y division)
2. Mostrar los resultados.
"""
""" SALIDA
3. Resultado de suma
4. Resultado de resta
5. Resultado de multiplicacion
6. Resultado de division
7. Volver a realizar otra operación
"""
print ("Ejercicio 1: Operaciones aritmeticas")
Numero1=int(input("Ingrese un numero: "))
Numero2=int(input("Ingrese un numero: "))
while True:
    User=int(input("\nSuma-1\nResta-2\nMultiplicacion-3\nDivision-4\nExponenciacion-5\nCociente-6\nSalir-7\n\nSeleccione una opcion del menu: "))
    try:
        if(User==1):
            print(Numero1,"+", Numero2,"=", Numero1+Numero2)
        elif(User==2):
            print(Numero1,"-", Numero2,"=", Numero1-Numero2)
        elif(User==3):
            print(Numero1,"*", Numero2,"=", Numero1*Numero2)
        elif(User==4):
            print(Numero1,"/", Numero2,"=", Numero1/Numero2)
        elif(User==5):
            print(Numero1,"^", Numero2,"=", Numero1**Numero2)
        elif(User==6):
            print(Numero1,"//", Numero2,"=", Numero1//Numero2)
        elif(User==7):
            break
        else:
            print("El valor asignado no se encuentra dentro del rango")

    except ValueError:
        print("Debe ingresar una opcion valida.")
    accion=(input("Desea realizar otra operacion? S/N:  "))
    if accion.upper() != "S":
        break
SystemExit