from Persona import Persona
class Alumno (Persona):
    def __init__(self, nombre, edad, boleta):
        self.boleta=boleta
    @property
    def boleta(self):
        return self.__boleta
    @boleta.setter
    def boleta(self, boleta):
        self.__boleta=boleta
    def imprimeInformacion(self):
        super().imprimeInformacion()
        print("Boleta : {}".format(self.boleta))

alumno=Alumno("Carlos ", 100, "741852963")
alumno.nombre="Alumno Creado"
alumno.edad=100
alumno.imprimeInformacion()