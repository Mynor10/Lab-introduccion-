
# Clase para representar un barco
class Barco:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.ubicacion = []
        self.hundido = False

    def colocar_barco(self, fila, columna, orientacion):
        if orientacion == "horizontal":
            for i in range(self.tamano):
                self.ubicacion.append((fila, columna + i))
        else:
            for i in range(self.tamano):
                self.ubicacion.append((chr(ord(fila) + i), columna))

# Clase para representar el tablero de juego
class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(10)] for _ in range(10)]
        self.barcos = []
        self.disparos = []

    def imprimir_tablero(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        letras = "ABCDEFGHIJ"
        for i in range(10):
            fila = " ".join(self.tablero[i])
            print(f"{letras[i]} {fila}")

    def colocar_barco(self, barco):
        for fila, columna in barco.ubicacion:
            self.tablero[ord(fila) - ord("A")][columna - 1] = "O"

    def disparar(self, fila, columna, oponente):
        if (fila, columna) in self.disparos:
            print("Ya has disparado a esa casilla.")
            return

        self.disparos.append((fila, columna))
        if (fila, columna) in oponente.obtener_ubicacion_barcos():
            print("¡Impacto en un barco!")
            oponente.marcar_danio(fila, columna)
            if oponente.hundido_todos_barcos():
                print("¡Has hundido todos los barcos del oponente! ¡Ganaste!")
        else:
            print("Fallo en el disparo.")

    def obtener_ubicacion_barcos(self):
        ubicacion = []
        for barco in self.barcos:
            ubicacion.extend(barco.ubicacion)
        return ubicacion

    def hundido_todos_barcos(self):
        for barco in self.barcos:
            if not barco.hundido:
                return False
        return True

    def marcar_danio(self, fila, columna):
        for barco in self.barcos:
            if (fila, columna) in barco.ubicacion:
                barco.tamano -= 1
                if barco.tamano == 0:
                    print(f"¡Has hundido un barco {barco.nombre}!")
                    barco.hundido = True
                else:
                    print(f"¡Has impactado un barco {barco.nombre}!")

# Función para el juego principal
def jugar_batalla_naval():
    print("¡Bienvenido a Batalla Naval!")
    jugador1 = Tablero()
    jugador2 = Tablero()

    barcos_jugador1 = [Barco("Pequeño 1", 3), Barco("Pequeño 2", 3), Barco("Pequeño 3", 3), Barco("Grande 1", 5), Barco("Grande 2", 5)]
    barcos_jugador2 = [Barco("Pequeño 1", 3), Barco("Pequeño 2", 3), Barco("Pequeño 3", 3), Barco("Grande 1", 5), Barco("Grande 2", 5)]

    print("Jugador 1, coloca tus barcos:")
    for barco in barcos_jugador1:
        jugador1.barcos.append(barco)
        while True:
            jugador1.imprimir_tablero()
            print(f"Coloca el barco {barco.nombre} ({barco.tamano} casillas).")
            fila = input("Fila (A-J): ")
            columna = int(input("Columna (1-10): "))
            orientacion = input("Orientación (horizontal/vertical): ")
            fila = fila.upper()

            if fila not in "ABCDEFGHIJ" or columna < 1 or columna > 10 or orientacion not in ["horizontal", "vertical"]:
                print("Entrada no válida. Inténtalo de nuevo.")
                continue

            barco.colocar_barco(fila, columna, orientacion)
            jugador1.colocar_barco(barco)
            break

    print("Jugador 2, coloca tus barcos:")
    for barco in barcos_jugador2:
        jugador2.barcos.append(barco)
        while True:
            jugador2.imprimir_tablero()
            print(f"Coloca el barco {barco.nombre} ({barco.tamano} casillas).")
            fila = input("Fila (A-J): ")
            columna = int(input("Columna (1-10): "))
            orientacion = input("Orientación (horizontal/vertical): ")
            fila = fila.upper()

            if fila not in "ABCDEFGHIJ" or columna < 1 or columna > 10 or orientacion not in ["horizontal", "vertical"]:
                print("Entrada no válida. Inténtalo de nuevo.")
                continue

            barco.colocar_barco(fila, columna, orientacion)
            jugador2.colocar_barco(barco)
            break

    turno = 1
    while True:
        if turno == 1:
            print("Turno del Jugador 1:")
            jugador2.imprimir_tablero()
            fila = input("Fila a disparar (A-J): ")
            columna = int(input("Columna a disparar (1-10): "))
            fila = fila.upper()
            jugador1.disparar(fila, columna, jugador2)
            turno = 2
        else:
            print("Turno del Jugador 2:")
            jugador1.imprimir_tablero()
            fila = input("Fila a disparar (A-J): ")
            columna = int(input("Columna a disparar (1-10): "))
            fila = fila.upper()
            jugador2.disparar(fila, columna, jugador1)
            turno = 1

        if jugador1.hundido_todos_barcos():
            print("¡Jugador 2 gana!")
            break
        elif jugador2.hundido_todos_barcos():
            print("¡Jugador 1 gana!")
            break

# Iniciar el juego
jugar_batalla_naval()