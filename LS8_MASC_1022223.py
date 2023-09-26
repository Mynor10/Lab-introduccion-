# Pensamiento computacional 
# 26/09/23
# Mynor Adolfo Salazar Contreras
# Objetivo: 
# Entrada 
# Procesos 
# Salida


#seleccion de numero
print("bienvenido")
#Menu
import math

menu=""
contador=1
num1= 0
num2 =1
numero_siguiente = num2
while menu != "3":
    print("Menu de opciones")
    print("1. Factorial")
    print("2. Secuencia de fibonacci")
    print("3. Salir")
    menu=input("seleccione una opcion")
    #Factorial
    if menu=="1":
        print("Usted selecciono factorial")
        n1 =int(input("ingrese un numero"))
        print("La factorial de", n1)
        while contador <= n1:
            print(n1,"*", (contador), "=", n1*contador) 
            contador = contador +1 
    elif menu=="2":
        print("usted selecciono sucesiòn de fibonacci")
        num2 =int(input("ingrese un numero"))
        print("la sucesion de numero de",num1)
        numero_siguiente = num2
        while contador <=1:
            print(numero_siguiente, ends="")
            contador = contador+1
            num1,num2 = num2, numero_siguiente
            numero_siguiente = num1+ num2
            print()

    elif menu=="3":
        print("Finalizar calculo")
    else:
        print("ERROR seleccione una opcio valida")