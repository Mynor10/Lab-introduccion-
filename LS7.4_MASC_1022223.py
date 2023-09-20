# Pensamiento computacional 
# 19/09/23
# Mynor Adolfo Salazar Contreras
# Objetivo: uso del string e input
# Entrada valores en jerarquia 
# Procesos pedir numeros enteros y realizar las operaciones
# Salida resultado es 

# Seleccion de numero 
import math
print("ejercicio 3 jerarquia de operaciones")
a= int(input("seleccione un numero entero"))
b= int(input("seleccione un numero entero"))
c= int(input("seleccione un numero entero"))

# Menu
menu=""
while menu != "6":
    print("Menu de opciones")
    print("1. a * b + c ")
    print("2. a * (b + c) ")
    print("3. a/(b*c) ")
    print("4. 3a + 2b/ c**2")
    print("5. cuadratica")
    print("6. salir")

    menu=input("seleccione una opcion")
    if menu=="1":
        print("Usted selecciono la 1")
        print(a, "x", b, "+", c, "=", (a * b) + c)
    elif menu=="2":
        print("usted selecciono la 2")
        print(a, "x (", b, "+", c, ") =", a * (b + c))
    elif menu=="3":
        print("usted selecciono la 3")
        print(a, "/", b, "x", c, "=", a / (b * c))
    elif menu=="4":
        print("usted selecciono la 4")
        print("3(", a, ") + 2(", b, ")/", c, "^2 =" , ((a * 3) + (b * 2)) / (c ** 2) )
    elif menu=="5":
        if a != 0 and ((b**2) - (4 * a * b)) >= 0:
            print( "el resultado es:", (-b + math.sqrt((b**2)-(4*a*c)))/(2*a) )
            print( "el resultado es:", (-b - math.sqrt((b**2)-(4*a*c)))/(2*a) )
    elif menu== "6":
        print("salio del programa")
    else:
        print("ERROR seleccione un valor dentro del rango")