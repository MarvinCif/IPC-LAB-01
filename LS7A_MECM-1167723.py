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

print(Numero1,"+", Numero2,"=", Numero1+Numero2)
print(Numero1,"-", Numero2,"=", Numero1-Numero2)
print(Numero1,"*", Numero2,"=", Numero1*Numero2)
print(Numero1,"/", Numero2,"=", Numero1/Numero2)
print(Numero1,"^", Numero2,"=", Numero1**Numero2)
print(Numero1,"//", Numero2,"=", Numero1//Numero2)

SystemExit