#TS Introduccion a programacion - Sección:17
#28/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que realice secuencias numericas.
#Entrada: Numero, Numeros, Resultado, i, opcion.
""" PROCESO
1. Realizar un bucle for que muestre una secuencia numérica de 1 a 25 con incremento en 1.
2. Realizar un bucle while que muestre una secuencia numérica de 1 a 25 con incremento en 1.
3. Realizar un bucle for que muestre una secuencia numérica de 1 a 50 con incremento en 5.
4. Realizar un bucle while que muestre una secuencia numérica de 1 a 50 con incremento en 5.
5. Realizar un bucle for que muestre una secuencia numérica de 20 a 0 con decremento en 2.
6. Realizar un bucle for que muestre una secuencia numérica de 20 a 0 con decremento en 2.
"""
""" SALIDA
7. Pantalla de opciones TKinter
    Resultado de la secuencia numerica 1 a 25 con for.
    Resultado de la secuencia numerica 1 a 25 con while.
    Resultado de la secuencia numerica 1 a 50 con for.
    Resultado de la secuencia numerica 1 a 50 con while.
    Resultado de la secuencia numerica 20 a 0 con for.
    Resultado de la secuencia numerica 20 a 0 con while.
"""

import tkinter as tk
from tkinter import *

#Se define una funcion para realizar una secuencia de incremento en 1 con el ciclo for
def Num1_25for():
        Numero = []
        for i in range(1, 26):
            Numero.append(i)
        Resultado.config(text=f"Números del 1 al 25 con incremento de 1:\n {Numero}")
        
#Se define una funcion para realizar una secuencia de incremento en 1 con el ciclo while
def Num1_25while():
    Numero = 0
    numeros = []
    while Numero < 25:
        Numero = Numero+1
        numeros.append(Numero)
    Resultado.config(text=f"Números del 1 al 25 con incremento de 1:\n{numeros}")

#Se define una funcion para realizar una secuencia de incremento en 5 con el ciclo for
def Num5_50for():
    Numero = []
    for i in range(5,51,5):
        Numero.append(i)
    Resultado.config(text=f"Números del 5 al 50 con incremento de 5:\n {Numero}")

#Se define una funcion para realizar una secuencia de incremento en 5 con el ciclo while
def Num5_50while():
    Numero = 0
    numeros = []
    while Numero < 50:
        Numero = Numero+5
        numeros.append(Numero)
        Resultado.config(text=f"Numeros del 5 al 50 con incremento de 5:\n  {numeros}")

#Se define una funcion para realizar una secuencia de decremento en 2 con el ciclo for
def Num20_0for():
    Numero = []
    for i in range(20,-1,-2):
        Numero.append(i)
    Resultado.config(text=f"Números del 20 al 0 con decremento en 2: {Numero}")

#Se define una funcion para realizar una secuencia de decremento en 2 con el ciclo while
def Num20_0while():
    Numero = 22
    numeros = []
    while Numero > 0:
        Numero = Numero-2
        numeros.append(Numero)
        Resultado.config(text=f"Numeros del 20 al 0 con decremento en 2:  {numeros}")

#Se define una funcion para realizar la terminacion del programa
def salida():
    opcion.destroy()

#Se definen las funciones del programa con TKinter

#Se declara una variable que da inicio a TKinter con el tamaño, letra y separacion de los titulos.
opcion = tk.Tk()
opcion.title("TS8 - SECUENCIAS DE NUMEROS")
opcion.geometry("800x400")

Titulo = tk.Label(opcion, text="TS8 - SECUENCIAS DE NUMEROS", font=("Arial", 14))
Titulo.pack()

Opciones = tk.Label(opcion, text="\nSeleccione una opción:\n", font=("Arial", 11))
Opciones.pack()

BotonSecuencia1 = tk.Button(opcion, text="SECUENCIA 1-25 FOR", command=Num1_25for, font=("Arial", 11))
BotonSecuencia1.pack(pady=4)

BotonSecuencia2 = tk.Button(opcion, text="SECUENCIA 1-25 WHILE", command=Num1_25while, font=("Arial", 11))
BotonSecuencia2.pack(pady=4)

BotonSecuencia3 = tk.Button(opcion, text="SECUENCIA 1-50 FOR", command=Num5_50for, font=("Arial", 11))
BotonSecuencia3.pack(pady=4)

BotonSecuencia4 = tk.Button(opcion, text="SECUENCIA 1-50 WHILE", command=Num5_50while, font=("Arial", 11))
BotonSecuencia4.pack(pady=4)

BotonSecuencia5 = tk.Button(opcion, text="SECUENCIA 20-0 FOR", command=Num20_0for, font=("Arial", 11))
BotonSecuencia5.pack(pady=4)

BotonSecuencia6 = tk.Button(opcion, text="SECUENCIA 20-0 WHILE", command=Num20_0while, font=("Arial", 11))
BotonSecuencia6.pack(pady=4)

BotonSalir = tk.Button(opcion, text="Salir", command=salida, font=("Arial", 11))
BotonSalir.pack(pady=4)


Resultado = tk.Label(opcion, text="", font=("Arial", 11))
Resultado.pack(pady=5)

opcion.mainloop()
