#TS Introducción a programación - Sección:17
#05/09/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa pida al usuario su información.
#Entrada: sNombre, sEdad, sCarrera, sCarne
""" PROCESO
1. Mostrar en pantalla nombre, edad, carrera y carne.
2. Solicitar al usuario que ingrese sus datos en el nombre, edad, carrera y carne
"""
""" SALIDA
3. Mostrar en pantalla el nombre
4. Mostrar en pantalla el edad
5. Mostrar en pantalla el carrera
6. Mostrar en pantalla el carne
"""

print ("Mi segundo programa")
print("Datos de usuario\n")
sNombre=str(input("Ingrese su nombre: "))
sEdad=str(input("Ingrese su edad: "))
sCarrera=str(input("Ingrese su carrera: "))
sCarne=str(input("Ingrese su carne: "))
print("\n\nNombre: ", sNombre)
print("Edad: ", sEdad)
print("Carrera: ", sCarrera)
print("Carne: ", sCarne)
print("\nSoy ",sNombre, " tengo ",sEdad, " años y estudio la carrera de ",sCarrera,"\nMi número de carné es; ", sCarne)