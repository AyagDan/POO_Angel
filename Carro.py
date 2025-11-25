class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad = max(0, self.velocidad - cantidad)

    def mostrar_velocidad(self):
        print(self.velocidad)

carro = Carro("Nissan", "Versa")
carro.acelerar(20)
carro.mostrar_velocidad()
