# Pensamiento computacional 
# 19/09/23
# Mynor Adolfo Salazar Contreras
# Objetivo: 
# Entrada 
# Procesos 
# Salida

#Seleccione numeros 
print("operaciones aritmeticas")
numero1= int(input("seleccione un numero entero"))
numero2= int(input("seleccione un numero entero diferente al anterior "))
print("/n")

#Menu
menu=""
while menu != "7":
    print("Menu de opciones")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. Division")
    print("5. exponenciacion")
    print("6. Cociente")
    print("7. Salir")
    menu=input("seleccione una opcion")
    if menu=="1":
        print("Usted selecciono la 1")
        print(numero1,"+", numero2, "=", numero1 + numero2)
    elif menu=="2":
        print("usted selecciono la 2")
        print(numero1,"-", numero2, "=", numero1 - numero2)
    elif menu=="3":
        print("usted selecciono la 3")
        print(numero1,"*", numero2, "=", numero1 * numero2)
    elif menu=="4":
        print("usted selecciono la 4")
        print(numero1,"/", numero2, "=", numero1 / numero2)
    elif menu=="5":
        print("usted selecciono la 5")
        print(numero1,"**", numero2, "=", numero1 ** numero2)
    elif menu=="6":
        print("usted selecciono la 6")
        print(numero1,"//", numero2, "=", numero1 // numero2)
    elif menu=="7":
        print("Terminò")
    else:
        print("ERROR seleccione una opcio valida")








