#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que realice operaciones aritméticas.
#Entrada: Numero1, Numero2.
""" PROCESO
1. Solicitar al usuario tres numeros y realizar los cálculos de las expresiones
2. Mostrar los resultados.
"""
""" SALIDA
3. Resultado de operacion 1
4. Resultado de operacion 2
5. Resultado de operacion 3
6. Resultado de operacion 4
"""
print ("Ejercicio 3: Jerarquia de operaciones")
Numero1=int(input("Ingrese un numero: "))
Numero2=int(input("Ingrese un numero: "))
Numero3=int(input("Ingrese un numero: "))

print("\n", Numero1*Numero2+Numero3)
print("\n", Numero1*(Numero2+Numero3))
print("\n", (Numero1)/(Numero2*Numero3))
print("\n", (3*Numero1+2*Numero2)/(Numero3**2))

SystemExit