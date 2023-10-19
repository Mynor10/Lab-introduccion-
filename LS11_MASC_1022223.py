# Introducción a la programacion s11
# 19/10/2023
# Mynor salazar 1022223
# Objetivo: 
# Entrada: 
# procesos: 
# Salida: 

#Solicitud de la palabra 
palabra=input("Ingrese una palabra ")

tres_letras=palabra[:3]
print("las primeras dos letras de la palabra son",tres_letras)

#cadena
nueva_cadena = tres_letras
segunda_palabra=input("ingrese una nueva palabr")

#remplazar las vocales 
segunda_palabra_modificada=segunda_palabra.replace("o","x")

print("El nuevo texto es", segunda_palabra_modificada)

