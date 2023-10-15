#Introducción a programación - Sección:17
#05/10/2023
#Marvin Estuardo Cifuentes Mejía - 1167723
#Objetivo: Programa que realiza el cálculo y análisis de la eficiencia de líneas de producción en un aserradero.
"""ENTRADA
- Linea (int): Número de línea (1-4)
- Precio (int): Precio de venta por m²
- Metros (int): Metros cuadrados vendidos
- Empleados (int): Número de empleados (1-20)
- CostoPorHora (list): Lista de costos por hora de empleados
- HorasTrabajadas (list): Lista de horas trabajadas por empleados
- NumLineas (int): Cantidad de líneas a comparar (2-4)
- ComparacionLinea (list): Lista de números de líneas a comparar
- BuscarLinea (int): Número de línea a buscar
- GuardarLinea (list): Lista de tuplas con datos guardados (NoLinea, GananciaTotal, CostoTotal, GananciaNeta, Eficiencia)
"""
""" PROCESO
1. Se capturan los valores ingresados por el usuario para Linea, Precio, Metros y Empleados.
2. Se aplican restricciones verificando que Linea esté en el rango (1-4) y Empleados en el rango (1-20).
3. Se inicializan las listas CostoPorHora y HorasTrabajadas.
4. Se solicita el costo por hora y las horas trabajadas para cada empleado y se validan los datos.
5. Se calcula el CostoTotal como la suma de los pagos individuales de empleados.
6. Se calcula GananciaTotal como el producto de Metros y Precio.
7. Se calcula GananciaNeta restando CostoTotal a GananciaTotal.
8. Se calcula Eficiencia como GananciaNeta dividida por Empleados.
9. Se guardan los datos calculados en GuardarLinea.
10. Se muestra un mensaje de resultados en una ventana emergente.
"""
""" SALIDA
1. Mensajes de resultados en ventanas emergentes con los cálculos realizados.
2. Mensajes de datos guardados o error en caso de no encontrar datos en MostrarDatos.
3. Mensajes de comparación de datos en Comparacion.
4. Mensajes de mayor eficiencia o mensaje de error en caso contrario.
5. Cierre de la ventana principal del programa.
"""

# Función para calcular la ganancia, costo total, ganancia neta e índice de eficiencia
def CalcularProduccion():
    while True:
        try:
            NoLinea = int(input("\n\nNúmero de línea (1-4): "))
            if not (1 <= NoLinea <= 4):
                print("\nEl número de línea debe estar en el rango de 1 a 4.")
                input("Presione Enter para continuar...\n\n")
                continue
            M2Venta = int(input("Precio de venta por m²: "))
            M2VentaMes = int(input("Metros cuadrados vendidos: "))
            NoEmpleados = int(input("Número de empleados (1-20): "))
            if NoEmpleados > 20:
                print("\nEl número máximo de empleados es 20.")
                input("Presione Enter para continuar...\n\n")
                continue
        except ValueError:
            print("\nPor favor ingrese un número válido.")
            input("Presione Enter para continuar...\n\n")
            continue

        CostoPorHora = []
        HorasTrabajadas = []

        for empleado in range(NoEmpleados):
            try:
                CostoHora = int(input(f"\tCosto por hora del Empleado {empleado + 1}: "))
                Horas = int(input(f"\tHoras trabajadas por el Empleado {empleado + 1}: "))
            except ValueError:
                print("\nDebe ingresar un valor válido.")
                input("Presione Enter para continuar...\n\n")
                return

            CostoPorHora.append(CostoHora)
            HorasTrabajadas.append(Horas)

        CostoTotal = sum([costo * horas for costo, horas in zip(CostoPorHora, HorasTrabajadas)])
        GananciaTotal = M2VentaMes * M2Venta
        GananciaNeta = GananciaTotal - CostoTotal
        Eficiencia = GananciaNeta / NoEmpleados

        GuardarDatos(NoLinea, GananciaTotal, CostoTotal, GananciaNeta, Eficiencia)

        print(f"\n\nResultados para Línea {NoLinea}:\n")
        print(f"Ganancia Total: Q{GananciaTotal:.2f}")
        print(f"Costo Total: Q{CostoTotal:.2f}")
        print(f"Ganancia Neta: Q{GananciaNeta:.2f}")
        print(f"Índice de Eficiencia: {Eficiencia:.0f}.00")
        input("Presione Enter para continuar...\n\n")
        return

# Función para mostrar los datos de una línea específica
def MostrarDatos():
    while True:
        try:

            BuscarLinea = int(input("Número de línea a buscar: "))
            if not (1 <= BuscarLinea <= 4):
                print("\nPor favor ingrese un número de línea válido.")
                input("Presione Enter para continuar...\n\n")
                continue
            if not guardar_linea:
                print("\nNo se ha guardado ningún dato en esa línea")
                input("Presione Enter para continuar...\n\n")
                return

            mensaje = (f"\nDatos calculados para Línea {BuscarLinea}:")
            encontrada = False

            for linea in guardar_linea:
                if linea[0] == BuscarLinea:
                    mensaje = mensaje + (f"\nGanancia Total: Q{linea[1]:.2f}")
                    mensaje = mensaje + (f"\nCosto Total: Q{linea[2]:.2f}")
                    mensaje = mensaje + (f"\nGanancia Neta: Q{linea[3]:.2f}")
                    mensaje = mensaje + (f"\nÍndice de Eficiencia: {linea[4]:.0f}.00")
                    encontrada = True
                    break

            if not encontrada:
                mensaje = (f"\nNo se han calculado datos para la Línea {BuscarLinea}.")

            print(mensaje)
            input("Presione Enter para continuar...\n\n")
            return
        except ValueError:
            print("\nPor favor ingrese un número válido.")
            input("Presione Enter para continuar...\n\n")
            continue  # Vuelve a pedir todos los datos si hay un error

# Función para mostrar los datos comparados de dos líneas.
def comparacion():
    while True:
        try:

            NumLineas = int(input("Ingrese la cantidad de líneas a comparar (2-4): "))
            if not (2 <= NumLineas <= 4):
                print("\nPor favor, ingrese una cantidad válida (2-4).")
                input("Presione Enter para continuar...\n\n")
                continue

            ComparacionLinea = []

            for i in range(NumLineas):
                NumeroLinea = int(input(f"Ingrese el número de linea a comparar: "))
                if not NumeroLinea:
                    print("\nPor favor, ingrese un valor")
                    input("Presione Enter para continuar...\n\n")
                    continue
                if NumeroLinea > 4:
                    print("\nPor favor, ingrese números de línea válidos (1-4).")
                    input("Presione Enter para continuar...\n\n")
                    continue
                ComparacionLinea.append(NumeroLinea)

            mensaje = ("\nComparación de Datos:")

            for NumeroLinea in ComparacionLinea:
                encontrada = False
                for linea in guardar_linea:
                    if linea[0] == NumeroLinea:
                        mensaje = mensaje + (f"\n\nLínea {NumeroLinea}:")
                        mensaje = mensaje + (f"\nGanancia Total: Q{linea[1]:.2f}")
                        mensaje = mensaje + (f"\nCosto Total: Q{linea[2]:.2f}")
                        mensaje = mensaje + (f"\nGanancia Neta: Q{linea[3]:.2f}")
                        mensaje = mensaje + (f"\nÍndice de Eficiencia: {linea[4]:.0f}.00")
                        encontrada = True
                        break

            if not encontrada:
                mensaje += f"\n\nNo se han calculado datos para la Línea {NumeroLinea}."

            print(mensaje)
            input("Presione Enter para continuar...\n\n")
            return
        except ValueError:
            print("\nDebe ingresar un valor válido.")
            input("Presione Enter para continuar...\n\n")
            continue

# Función para encontrar la línea con mayor eficiencia
def MayorProduccion(ComparacionLinea):
    MayorEficiencia = None
    LineaMayorEficiencia = None

    for NumeroLinea in ComparacionLinea:
        for linea in guardar_linea:
            if linea[0] == NumeroLinea:
                Eficiencia = linea[4]
                if MayorEficiencia is None or Eficiencia > MayorEficiencia:
                    MayorEficiencia = Eficiencia
                    LineaMayorEficiencia = NumeroLinea

    if LineaMayorEficiencia is not None:
        print(f"La línea con mayor eficiencia es la Línea {LineaMayorEficiencia} con un total de {MayorEficiencia:.0f}.00")
        input("Presione Enter para continuar...\n\n")
    else:
        print("No se han calculado datos para las líneas comparadas.")
        input("Presione Enter para continuar...\n\n")

# Función para guardar los datos ingresados
def GuardarDatos(NoLinea, GananciaTotal, CostoTotal, GananciaNeta, Eficiencia):
    guardar_linea.append((NoLinea, GananciaTotal, CostoTotal, GananciaNeta, Eficiencia))

if __name__ == "__main__":
    guardar_linea = []

    while True:
        print("PROYECTO DE CURSO - INTRODUCCION A PROGRAMACION\n")
        print("OPCIONES")
        print("1. Calcular Producción")
        print("2. Mostrar Datos")
        print("3. Comparación")
        print("4. Salir")

        opcion = input("\nIngrese el número de la opción deseada: ")

        if opcion == "1":
            CalcularProduccion()
        elif opcion == "2":
            MostrarDatos()
        elif opcion == "3":
            comparacion()
        elif opcion == "4":
            break
        else:
            print("\nPor favor, seleccione una opción válida.")
            input("Presione Enter para continuar...\n\n")
