# Pensamiento computacion 
# 21/09/23
# Mynor Adolfo Salazar Contreras
# Objetivo: Crear un rango del 1 al 10
# Entrada: Nombre, edad, carreraq, carné
# Procesos principales: pedir variable para realizar operaciones 
# Salida: 

# seleccion de numero
while True:

    numero1= int(input("seleccione un numero dentro del 1 al 10"))
    if numero1<=0:
        print("ERROR")
    if numero1 >=10:
        print("ERROR")
    else:

    #rango
        for i in range(1,11):
            print(numero1, "x",i, "=", i*numero1)

    numero2= str(input("Desea continuar? ingrese si o no "))
    if numero2== "no":
        break

