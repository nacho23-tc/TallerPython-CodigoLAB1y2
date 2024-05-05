import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = []
        for palo in ["Corazones", "Diamantes", "Tréboles", "Picas"]:
            for valor in range(1, 14):
                self.cartas.append(Carta(palo, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def tomar_carta(self, carta):
        self.mano.append(carta)

    def valor_mano(self):
        valor = 0
        for carta in self.mano:
            if carta.valor == 1:
                if valor + 11 <= 21:
                    valor += 11
                else:
                    valor += 1
            elif carta.valor >= 10:
                valor += 10
            else:
                valor += carta.valor
        return valor

mazo = Mazo()
mazo.barajar()

jugador = Jugador("Jugador")
dealer = Jugador("Dealer")

# Repartir cartas iniciales
jugador.tomar_carta(mazo.sacar_carta())
dealer.tomar_carta(mazo.sacar_carta())
jugador.tomar_carta(mazo.sacar_carta())
dealer.tomar_carta(mazo.sacar_carta())

# Mostrar cartas del jugador y una del dealer
print("Cartas del jugador:")
for carta in jugador.mano:
    print(carta)
print("Valor total de la mano del jugador:", jugador.valor_mano())
print("\nUna carta del dealer:")
print(dealer.mano[0])

# Juego del jugador
while True:
    accion = input("¿Desea 'pedir' o 'plantarse'?: ").lower()
    if accion == "pedir":
        jugador.tomar_carta(mazo.sacar_carta())
        print("Carta recibida:", jugador.mano[-1])
        print("Valor total de la mano del jugador:", jugador.valor_mano())
        if jugador.valor_mano() > 21:
            print("¡Te has pasado de 21! Has perdido.")
            break
    elif accion == "plantarse":
        break
    else:
        print("Por favor, elija 'pedir' o 'plantarse'.")

# Juego del dealer
print("\nTurno del dealer...")
print("Cartas del dealer:")
for carta in dealer.mano:
    print(carta)
print("Valor total de la mano del dealer:", dealer.valor_mano())

while dealer.valor_mano() < 17:
    dealer.tomar_carta(mazo.sacar_carta())
    print("El dealer ha tomado una carta:", dealer.mano[-1])
    print("Valor total de la mano del dealer:", dealer.valor_mano())

# Determinar ganador
if jugador.valor_mano() <= 21:
    if dealer.valor_mano() > 21 or jugador.valor_mano() > dealer.valor_mano():
        print("¡Felicidades! Has ganado.")
    elif jugador.valor_mano() < dealer.valor_mano():
        print("El dealer gana.")
    else:
        print("Empate.")
else:
    print("¡Te has pasado de 21! Has perdido.")

