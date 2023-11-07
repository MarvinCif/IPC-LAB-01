#Introducción a programación - Sección:17
#07/11/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que permita el ingreso de datos de venta de un automovil.
#Entrada: modelo, precio, marca, disponibilidad, tipoCambioDolar, descuento.
""" PROCESO
1. Mostrar menu principal.
2. Solicitar datos de marca, modelo, precio, cambioDolar, descuento.
"""
""" SALIDA
1. Opcion para solicitar al usuario el ingreso de los datos. (marca, modelo, precio, cambioDolar, descuento)
2. Opcion para mostrar informacion.
3. Opcion para salir.
"""

import os

class Automovil:
    def __init__(self,unModelo = 0,unPrecio = 0,unMarca = 0,disponible = True,tipoCambioDolar = 0,descuentoAplicado = 0):
        self.modelo = unModelo
        self.precio = unPrecio
        self.marca = unMarca
        self.disponible = disponible
        self.tipoCambioDolar = tipoCambioDolar
        self.descuentoAplicado = descuentoAplicado
        
    def obtenerModelo(self):
        self.modelo = unModelo
    def obtenerPrecio(self):
        self.precio = unPrecio
    def obtenerMarca(self):
        self.marca = unMarca
    
    def MostrarInformacion(self):
        print(f"Marca: {unMarca}.\nModelo {unModelo}.\nPrecio de venta: Q{unPrecio:.2f}.\nPrecio en dolares: ${tipoCambioDolar:.2f}.\n{disponibilidad}.")

if __name__ == "__main__":
    while True:
        os.system('cls')
        print("LS14 - INTRODUCCIÓN AL PENSAMIENTO COMPUTACIONAL\n\n")
        print("1.Realizar un ingreso.")
        print("2.Mostrar informacion.")
        print("3.Salir.")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            os.system('cls')
            unMarca = str(input("Ingrese la marca del automovil: "))
            unModelo = int(input("Ingrese el año de modelo del automovil: "))
            unPrecio = float(input("Ingrese el precio del automovil: "))
            disponibilidad = input("¿Se encuentra disponible? (Si/No): ")
            if disponibilidad == "Si":
                disponible = True
                disponibilidad = "Disponible"
            elif disponibilidad == "No":
                disponible = False
                disponibilidad = "No disponible"
            CambioDolar = float(input("Ingrese el tipo de cambio: "))
            descuentoAplicado = float(input("Ingrese descuento: "))
            if not descuentoAplicado == 0:
                unPrecio = (descuentoAplicado/100) * unPrecio
            tipoCambioDolar = unPrecio/CambioDolar
        if opcion == "2":
            os.system('cls')
            Informacion = Automovil(unModelo,unPrecio,unMarca,tipoCambioDolar,descuentoAplicado)
            Informacion.MostrarInformacion()
            input("Presione una tecla para continuar....")
        if opcion == "3":
            break