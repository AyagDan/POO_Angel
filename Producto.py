class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self._descuento = 0.1

    def precio_final(self):
        return self.precio * (1 - self._descuento)

p1 = Producto("Laptop", 15000)
print(p1.precio_final())
