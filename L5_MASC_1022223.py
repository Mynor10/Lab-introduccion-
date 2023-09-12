# Pensamiento computacional 
# 5/09/23
# Mynor Adolfo Salazar Contreras
# Objetivo: realizar un programa que relacione numeros con los dias de la semana 
# Entrada 
# Procesos 
# Salida

print ("ejercicio en clase 2")

Dia= int(input("seleccione un numero del 1 al 7"))


if Dia==1:
    print ("Usted selecciono lunes") 

if Dia==2:
    print ("Usted selecciono Martes") 

if Dia==3:
    print ("Usted selecciono Miercoles") 

if Dia==4:
    print ("Usted selecciono Jueves") 

if Dia==5:
    print ("Usted selecciono viernes")

if Dia==6:
    print ("Usted selecciono Sabado")

if Dia==7:
    print ("Usted selecciono Domingo")  

elif Dia<1 or Dia>7:
    print("ERROR")
