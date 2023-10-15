#Introducción a programación - Sección:17
#19/09/2023
#Marvin Estuardo Cifuentes Mejía
#Objetivo:Crear funciones para convertir de cm a otra unidad de medida de longitud.
#Entrada: Cantidad en centimetros a convertir.
""" PROCESO
1. Solicitar al usuario que ingrese una cantidad en cm a convertir.
2. Mostrar un menu de opciones de conversion y solicitar al usuario que seleccione una opcion.
"""
""" SALIDA
3. Resultado de la conversion a otra unidad de medida.
"""

#Conversión cm a m
def centimetroAmetro(centimetros):
    total=centimetros/100
    return total

#Conversión cm a km
def centimetroAkilometro(centimetros):
    total=centimetros/100000
    return total

#Conversión cm a in
def centimetroApulgada(centimetros):
    total=centimetros/2.54
    return total

#Conversión cm a ft
def centimetroApie(centimetros):
    total=centimetros/30.48
    return total