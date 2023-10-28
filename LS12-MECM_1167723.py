#Introducción a programación - Sección:17
#27/10/2023
#Marvin Estuardo Cifuentes Majía
#Objetivo:Crear un programa que permita guardar contactos en una lista.
#Entrada: Contactos, nombre, telefono, numero, eliminarcontacto, posicion, copialistacontacto.
""" PROCESO
1. Inicializar una lista vacía para almacenar los contactos.
2. Solicitar al usuario la cantidad de contactos que desea agregar.
3. Solicitar nombre y número de teléfono para cada contacto y agregarlos a la lista.
4. Mostrar la lista de contactos completa.
5. Si el usuario decide eliminar un contacto, solicitar el índice del contacto a eliminar y realizar la eliminación.
6. Ordenar la lista de contactos alfabéticamente por nombre.
7. Mostrar la lista de contactos ordenada.
8. Pedir al usuario ingresar un nuevo contacto en una posición específica de la lista.
9. Mostrar la lista de contactos actualizada.
10. Crear una copia de la lista de contactos original.
11. Ordenar la copia en orden descendente alfabéticamente por nombre.
12. Mostrar la lista copia en orden descendente.
13. Mostrar la lista original sin cambios.
"""
""" SALIDA
1. Solicitar al usuario la cantidad de contactos a almacenar.
2. Solicitar los datos de cada contacto.
3. Mostrar la lista de contactos.
4. Solicitar al usuario eliminar uno de los contactos existentes.
5. Mostrar la lista de contactos actualizada.
6. Mostrar la lista de contactos ordenada alfabeticamente.
7. Solicitar al usuario un nuevo ingreso en una posicion especifica.
8. Mostrar la lista de contactos actualizada.
9. Mostrar una copia de la lista original, ordenada de forma descendente.
10. Mostrar la lista original.
"""

# Se crea una variable tipo lista para almacenar los contactos.
Contactos = []

# Solicitar al usuario la cantidad de contactos que desea ingresar.
Numero = int(input("Ingrese la cantidad de contactos que desea agregar: "))

# Solicitar nombre y número de teléfono para cada contacto
for i in range(Numero):
    Nombre = input("Ingrese el nombre del contacto: ")
    Telefono = input("Ingrese el número de teléfono del contacto: ")
    Contacto = (Nombre, Telefono)  # Crear una tupla (nombre, telefono)
    Contactos.append(Contacto)  # Agregar la tupla a la lista de contactos

# Mostrar la lista de contactos completa
print("\n\nLista de contactos completa:")
for i, Contacto in enumerate(Contactos, 1):
    Nombre, Telefono = Contacto
    print(f"{i}. nombre: {Nombre}, Teléfono: {Telefono}")

# Pedir al usuario eliminar un contacto existente
EliminarContacto = int(input("\n\nIngrese el número del contacto que desea eliminar: ")) - 1

# Verificar si el numero es válido
if 0 <= EliminarContacto < len(Contactos):
    # Eliminar el contacto usando "pop"
    ContactoEliminado = Contactos.pop(EliminarContacto)
    print(f"\nSe eliminó el contacto: {ContactoEliminado[0]}")
else:
    print("Numero inválido. No se eliminó ningún contacto.")

# Mostrar la lista de contactos actualizada
print("\n\nLista de contactos actualizada:")
for i, Contacto in enumerate(Contactos, 1):
    Nombre, Telefono = Contacto
    print(f"{i}. Nombre: {Nombre}, Teléfono: {Telefono}")

# Ordenar la lista de contactos alfabéticamente por Nombre
Contactos.sort(key=lambda x: x[0])

# Mostrar la lista de contactos ordenada
print("\n\nLista de contactos ordenada alfabéticamente:")
for i, Contacto in enumerate(Contactos, 1):
    Nombre, Telefono = Contacto
    print(f"{i}. Nombre: {Nombre}, Teléfono: {Telefono}")

# Pedir al usuario ingresar un nuevo contacto en una posición específica
Posicion = int(input("\n\nIngrese la posición en la que desea guardar el nuevo contacto: ")) - 1
NuevoContacto = input("Ingrese el Nombre del nuevo contacto: ")
NuevoTelefono = input("Ingrese el número de teléfono del nuevo contacto: ")

# Verificar si la posición es válida
nuevo_contacto = (NuevoContacto, NuevoTelefono)
Contactos.insert(Posicion, nuevo_contacto)  # Insertar el nuevo contacto en la posición deseada
print(f"\nSe agregó el nuevo contacto en la posición {Posicion + 1}.")

# Mostrar la lista de contactos actualizada
print("\n\nLista de contactos actualizada:")
for i, contacto in enumerate(Contactos, 1):
    Nombre, Telefono = contacto
    print(f"{i}. Nombre: {Nombre}, Teléfono: {Telefono}")

# Crear una copia de la lista de contactos original
CopiaListaContactos = list(Contactos)

# Ordenar la copia en orden descendente alfabéticamente por Nombre
CopiaListaContactos.sort(key=lambda x: x[0], reverse=True)

# Mostrar la lista copia en orden descendente
print("\n\nLista copia de contactos en orden descendente:")
for i, contacto in enumerate(CopiaListaContactos, 1):
    Nombre, Telefono = contacto
    print(f"{i}. Nombre: {Nombre}, Teléfono: {Telefono}")

# Mostrar la lista original sin cambios
print("\n\nLista original de contactos:")
for i, contacto in enumerate(Contactos, 1):
    Nombre, Telefono = contacto
    print(f"{i}. Nombre: {Nombre}, Teléfono: {Telefono}")
