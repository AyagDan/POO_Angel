class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, nombre, tel):
        self.contactos.append((nombre, tel))

    def buscar(self, nombre):
        for c in self.contactos:
            if c[0] == nombre:
                return c
        return "No encontrado"

    def mostrar(self):
        for c in self.contactos:
            print(c)

agenda = Agenda()
agenda.agregar("Ana", "1111")
agenda.mostrar()
