#  Created by PyCharm
#
#  User: zOmArRD
#  Date: 30/7/2023
#
#  Copyright (c) 2023. zOmArRD <dev@zomarrd.me>

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El coche se ha encendido.")
        else:
            print("El coche ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print("El coche se ha apagado.")
        else:
            print("El coche ya estaba apagado.")

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += velocidad
            print("El coche ha acelerado a {} km/h.".format(self.velocidad))
        else:
            print("El coche no está encendido.")

    def frenar(self, velocidad):
        if self.encendido:
            self.velocidad -= velocidad
            print("El coche ha frenado a {} km/h.".format(self.velocidad))
        else:
            print("El coche no está encendido.")


# Creamos un objeto de la clase Coche
coche = Coche("Audi", "A4", "Rojo")

# Encendemos el coche
coche.encender()

# Aceleramos el coche
coche.acelerar(50)

# Frenamos el coche
coche.frenar(20)

# Apagamos el coche
coche.apagar()
