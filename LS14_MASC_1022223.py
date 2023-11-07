class Automovil:
    def __init__(self):
        self.modelo = 0  
        self.precio = 0.0  
        self.marca = ""  
        self.disponible = True  
        self.tipoCambioDolar = 1.0  
        self.descuentoAplicado = 0.0  

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def AplicarDescuento(self, descuento):
        self.descuentoAplicado = descuento

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible



auto = Automovil()


auto.DefinirModelo(int(input("Ingrese el modelo del automóvil: ")))
auto.DefinirPrecio(float(input("Ingrese el precio del automóvil: ")))
auto.DefinirMarca(input("Ingrese la marca del automóvil: "))
auto.DefinirTipoCambio(float(input("Ingrese el tipo de cambio: ")))

# descuento
descuento = float(input("Ingrese el descuento a aplicar (en valor porcentual"))
auto.AplicarDescuento(descuento)

auto.CambiarDisponibilidad()

# Imprimir los valores
print("Modelo:", auto.modelo)
print("Precio:", auto.precio)
print("Marca:", auto.marca)
print("Disponible:", auto.disponible)
print("Tipo de cambio:", auto.tipoCambioDolar)
print("Descuento aplicado:", auto.descuentoAplicado, "%")
