"""
Atributos Clase
"""
class ClasePrueba:
    atributoCompartido= []

    def __init__(self, valor):
        self.atributo=valor

    @property
    def atributo (self):
        return self.__atributo
    @atributo.setter
    def atributo(self, valor):
        self.__atributo=valor
ob1=ClasePrueba(100)
ob2=ClasePrueba(200)
ob1.atributoCompartido.append("Primer objeto agregado")
ob2.atributoCompartido.append("Segundo objeto agregado")

print(ob2.atributo)
print(ob1.atributo)
print(ob1.atributoCompartido)