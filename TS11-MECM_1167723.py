#TS Introducción a programación - Sección:17
#19/10/2023
#Marvin Estuardo Cifuentes Mejía
#Objetivo:Crear un programa pida ingresar una palabra y muestre sus primeras tres letras. Luego, pida otra palabra y cambie las letras "o" por "x"
"""PROCESO
Paso 1: 
    - Solicitar al usuario una palabra y mostrar las primeras tres letras una a una
    - Se recorren y muestran en pantalla las primeras tres letras de la palabra ingresada.
    - Guardar las primeras tres letras en una nueva variable
    - Las primeras tres letras se almacenan en una variable llamada 'LeerLetras'.

Paso 2: Solicitar al usuario un nuevo texto y reemplazar las vocales "o" por "x"
    - Se solicita al usuario ingresar un nuevo texto.
    - Se recorre cada letra del texto ingresado y se reemplazan las vocales "o" por "x".
"""
"""SALIDA
    - Se muestra en pantalla las primeras tres letras ingresadas por el usuario.
    - Se muestra en pantalla el nuevo texto con las vocales "o" reemplazadas por "x".
"""


import os

# Paso 1: Solicitar al usuario una palabra y mostrar las primeras tres letras una a una
palabra = input("Ingrese una palabra: ")
LeerLetras = ""

# Recorrer las primeras tres letras de la palabra ingresada
for i in range(3):
    if i < len(palabra):
        letra = palabra[i]
        print(f"Letra {i + 1}: {letra}")
        LeerLetras += letra

# Paso 2: Guardar las primeras tres letras en una nueva variable
print("Las primeras tres letras de su palabra son:", LeerLetras)
input("Presione Enter para continuar...")

# Paso 3: Solicitar al usuario un nuevo texto y reemplazar las vocales "o" por "x"
os.system('cls')
palabra2 = input("Ingrese una palabra: ")
TextoModificado = ""

# Recorrer cada letra del texto ingresado
for letra in palabra2:
    if letra == "o":
        TextoModificado += "x"
    else:
        TextoModificado += letra

# Mostrar el nuevo texto con las modificaciones
print("Texto modificado:", TextoModificado)

"""SITUACIONES EN LAS QUE ES UTIL ESTE TIPO DE FUNCION
1. Validar la entrada del usuario al momento de ingresar en algún tipo de formulario.
2. Procesar y corregir un texto. (Ejemplo: Cuando Word lee algún error gramatical)
3. Sustituir palabras en un texto por otras.
"""