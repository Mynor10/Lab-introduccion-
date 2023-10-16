def linea_de_produccion(numero_linea):
    MEVL = float(input(f"Precio de venta por metro cuadrado por Línea {numero_linea}: "))
    CVEN = float(input(f"Metros cuadrados vendidos por Línea {numero_linea}: "))
    NOEMPL = int(input(f"Empleados por Línea {numero_linea} (Entre 2 y 20): "))

    costo_total = 0
    COSEM = []

    if NOEMPL < 1 or NOEMPL > 20:
        print("Número de empleados no válido. Debe ser entre 1 y 20.")
    else:
        for i in range(NOEMPL):
            horas_chambeadas = float(input(f"Cantidad de horas chambeadas por empleado {i + 1} (2-20): "))
            costo_por_chambear = float(input(f"Costo por chambeo del empleado {i + 1} (25-100): "))
            if horas_chambeadas < 2 or horas_chambeadas > 20 or costo_por_chambear < 25 or costo_por_chambear > 100:
                print("Datos de empleado no válidos. Revise las restricciones.")
                break
            costo_total += horas_chambeadas * costo_por_chambear
            COSEM.append([horas_chambeadas, costo_por_chambear])

    return MEVL, CVEN, NOEMPL, costo_total, COSEM

def ganancia_neta(MELV, CVEN, COSEM):
    ganancia_total = MELV * CVEN
    costo_total = sum(horas * costo for horas, costo in COSEM)
    ganancia_neta = ganancia_total - costo_total
    return ganancia_neta

def eficiencia(ganancia_neta, NOEMPL):
    return round(ganancia_neta / NOEMPL, 0)

#Producción 1 y 2
print("Datos para la Línea de Producción 1:")
MELV1, CVEN1, NOEMPL1, CONCH1, COSEM1 = linea_de_produccion(1)
print("Datos para la Línea de Producción 2:")
MELV2, CVEN2, NOEMPL2, CONCH2, COSEM2 = linea_de_produccion(2)

# Calcular ganancia neta 
GNET1 = ganancia_neta(MELV1, CVEN1, COSEM1)
GNET2 = ganancia_neta(MELV2, CVEN2, COSEM2)

# Calcular efi
EFI1 = eficiencia(GNET1, NOEMPL1)
EFI2 = eficiencia(GNET2, NOEMPL2)

if EFI1 > EFI2:
    LCE = 1
else:
    LCE = 2

# Resultado en consola
print("Resultados:")
print("Ganancia neta de linea 1: ", GNET1)
print("Costo Total linea 1: ", CONCH1)
print("Eficiencia Llinea 1", EFI1)
print("Ganancia Neta linea 2: ", GNET2)
print("Costo total linea 2: ", CONCH2)
print("Eficiencia linea de 2", EFI2)
print("Línea de Mayor eficiencia: ", LCE)