# Pensamiento computacional 
# 10/10/23
# Mynor Adolfo Salazar Contreras
# Objetivo: invocar al modulo para convertir una moneda a otra
# Entrada:
# Procesos pedir datos y realizar las conversiones
# Salida:

import conversioneslab10

#Pedir al usuario la cantidad a convertir
pepito=float(input("Ingrese el valor que desea convertir en centimetros"))

#Menu
menu=""
while menu != "5":
    print("Menu de opciones")
    print("1. Metros")
    print("2.Kilometros")
    print("3. Pulgadas")
    print("4. Pies")
    print("5. salir")

    #menu
    menu=input("Seleccione una opcion")
    #Conversiones de centimetros a metros 
    if menu=="1":
        print("usted selecciono cm a m")
        metros=conversioneslab10.centrimetrosAmetros(pepito)
        print(pepito,"Centimetros equivale a",metros,"metros")
        
    #Conversion de centimetros a kilometros
    elif menu=="2":
        print("usted selecciono cm a km")
        kilometros=conversioneslab10.centimetrosAkilometros(pepito)
        print(pepito,"Centimetros equivale a",kilometros,"kilometros")

    #Conversion de centimetros a pulgadas
    elif menu=="3":
        print("usted selecciono cm a plg")
        pulgadas=conversioneslab10.centimetrosApulgadas(pepito)
        print(pepito,"Centimetros equivale a",pulgadas,"pulgadas")

    #Conversion de centimetros a pies
    elif menu=="4":
        print("usted selecciono cm a pies")
        pies=conversioneslab10.centimetrosApies(pepito)
        print(pepito,"Centimetros equivale a",pies,"pies")
    elif menu=="6":
        print("selecciono salir")
    else:
        print("ERROR, seleccione un valor dentro del rango del 1 al 6")