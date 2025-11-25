class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

al = Alumno("Ana", [9, 8, 10])
print(al.promedio())