class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

p1 = Persona("Ana", 20)
p1.saludar()

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: división entre cero"
        return a / b

calc = Calculadora()
print(calc.sumar(5, 3))

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r1 = Rectangulo(5, 3)
print(r1.area(), r1.perimetro())

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= monto

    def mostrar_saldo(self):
        print(self.saldo)

cuenta = CuentaBancaria("Carlos", 1000)
cuenta.depositar(500)
cuenta.mostrar_saldo()

class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

al = Alumno("Ana", [9, 8, 10])
print(al.promedio())

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio**2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

figuras = [Circulo(5), Cuadrado(4)]
for f in figuras:
    print(f.area())

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self._descuento = 0.1

    def precio_final(self):
        return self.precio * (1 - self._descuento)

p1 = Producto("Laptop", 15000)
print(p1.precio_final())

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
