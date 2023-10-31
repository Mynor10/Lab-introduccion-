class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = ""

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} {self.apellido_casada}"
        return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            año = 2023  
            año_nacimiento = int(self.fecha_nacimiento[-4:])
            edad = año - año_nacimiento
            return edad
        else:
            return "ERROR en fecha de nacimiento"

# ingrese los datos
persona = Persona()
persona.insertar_nombres(input("Ingresa el nombre: "))
persona.insertar_apellidos(input("Ingresa el apellido: "))
casada = input("¿Tiene apellido de casada?: ")
if casada.lower() == "sí" or casada.lower() == "si":
    persona.insertar_apellido_casada(input("Ingresa el apellido de casada: "))
persona.insertar_fecha_nacimiento(input("Ingresa la fecha de nacimiento: "))

# Imprimir la información de la persona
print("Nombre completo:", persona.obtener_nombre_completo())
print("Fecha de nacimiento:", persona.obtener_fecha_nacimiento())
print("Edad:", persona.obtener_edad())
