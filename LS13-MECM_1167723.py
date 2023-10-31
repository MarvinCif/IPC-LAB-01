import os
import datetime

class Valores:
    def __init__(self,Nombre,Apellido,ApellidoCasada,dia,mes,año):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.ApellidoCasada = ApellidoCasada
        self.dia = dia
        self.mes = mes
        self.año = int(año)
    
    def ObtenerNombre(self):
        return self.Nombre
    def ObtenerApellido(self):
        return self.Apellido
    def ObtenerApellidoCasada(self):
        return self.ApellidoCasada
    def Obtenerdia(self):
        return self.dia
    def Obtenerdia(self):
        return self.mes
    def Obtenerdia(self):
        return self.año
    
    def MostrarValores(self):
        print(f"Persona: {Nombre} {Apellido} {ApellidoCasada}")
        print(f"Fecha de nacimiento: {dia}/{mes}/{año}")
        print(f"Edad: {Edad}")

while True:
    os.system('cls')
    print("LS13 - INTRODUCCIÓN AL PENSAMIENTO COMPUTACIONAL\n\n")
    print("1.Realizar un ingreso.")
    print("2.Obtener ingreso.")
    print("3.Salir.")
    Hoy = datetime.date.today()
    Opcion = input("Seleccione una opcion: ")
    if Opcion == "1":
        os.system('cls')
        Nombre = input("Ingrese el nombre: ")
        Apellido = input("Ingrese el apellido: ")
        ApellidoCasada = input("Ingrese el apellido de casada (Si no hay, presionar Enter): ")
        input("Presione una tecla para continuar...")
        os.system('cls')
        print("Ingrese la fecha de nacimiento: ")
        dia = input("Ingrese dia de su fecha de nacimiento: ")
        mes = input("Ingrese el mes de su fecha de nacimiento: ")
        año = int(input("Ingrese el año de su fecha de nacimiento: "))
        Edad = Hoy.year - año
    elif Opcion == "2":
        os.system('cls')
        Guardar = Valores(Nombre,Apellido,ApellidoCasada,dia,mes,año)
        Guardar.MostrarValores()
        input("Presione una tecla para continuar...")
    elif Opcion == "3":
        break
    else:
        print("El valor ingresado no se encuentra entre las opciones.")