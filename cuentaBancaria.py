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