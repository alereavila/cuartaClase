class Persona:
    #rutina de inicializacion
    #definicion al propio objeto init es como el constructor
    def __init__(self, nombre="",edad=0):
        #con __ lo declara como privado
        self.nombre=nombre
        self.edad=edad
#estos se llaman decorators
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        if isinstance(nombre,str) and len(nombre)>5:
            self.__nombre=nombre
        else:
            #para lanzar una escepción
            raise TypeError("Se espera una cadena")
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        if not isinstance(edad, int) :
            raise TypeError("Se espera una edad verdadera la 'e' se crea aca como TypeError")
        elif edad>=0:
            self.__edad = edad
        else:
            raise ValueError("Se espera una edad verdadera la 'e' se crea aca como ValueError")
    def getNombre (self):
        return self.nombre

    def getEdad (self):
        return self.edad
    def setNombre (self, nombre):
        self.nombre = nombre

    def setEdad (self, edad):
        self.edad = edad


    def imprimeInformacion(self):
        print("\nNombre: {} tiene una edad {}".format(self.__nombre,self.__edad))

    #metodo especial
    def __repr__(self):
        return "Representacion en consila es una Persona con dos atributos"
    def __str__(self):
        return "Persona({}, {})".format(self.nombre, self.edad)



print("Prueba de clase Persona ")
"""""
persona1=Persona()
per2=Persona()
listaPersonas=[persona1,per2]

print(type(persona1))
"""""
#for persona in listaPersonas:
    #print("Nombre ",persona.__nombre)
    #print("Edad ",persona.__edad)

lista2Personas = []
for x in range(20):
    nombre= "se llama --> "+str(x)
    """""
    Se crea un error
    """""
    if x==11:
        x="11"
    if x==15:
        x=-15
    edad=x
    try:
        #Bloque que puede lanzar una escepcion
        lista2Personas.append(Persona(nombre,edad))
    except TypeError as te:
        #Si hay un erro
        print("No se creo la persona  -->{} {} ".format(x, te))
    except ValueError as ve:
        #Si hay un erro
        print("No se creo la persona  -->{} {} ".format(x, ve))
    except Exception as e:
        #Si hay un erro
        print("No se creo la persona  -->{} {} ".format(x, e))
    else:
        #se ejecuta si tode fue correcto
        print("Se creo la persona -->{}".format(x))
    finally:
        #Se ejecuta al final del try
        print("Todo bien en {}".format(x))

print(lista2Personas)
for persona in lista2Personas:
    #print("Nombre ", persona.nombre)
    #print("Edad ", persona.edad)
    persona.imprimeInformacion()
    print(persona)
"""""
objeto =    Persona("Ale",45)
objeto.setEdad(20)
objeto.imprimeInformacion()
"""""