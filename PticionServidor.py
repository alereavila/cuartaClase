#se debe de instalar
#cmd como administrador
#pip install requests
import requests
class LocalidadClima:
    def __init__(self, nombre, pais, temperatura, t_minima,
                 t_maxima, humedad, presion, latitud, longitud):
        self.nombre = nombre
        self.pais = pais
        self.temperatura = temperatura
        self.t_minima = t_minima
        self.t_maxima = t_maxima
        self.humedad = humedad
        self.presion = presion
        self.longitud = longitud
        self.latitud = latitud

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        self._temperatura = temperatura

    @property
    def t_minima(self):
        return self._t_minima

    @t_minima.setter
    def t_minima(self, t_minima):
        self._t_minima = t_minima

    @property
    def t_maxima(self):
        return self._t_maxima

    @t_maxima.setter
    def t_maxima(self, t_maxima):
        self._t_maxima = t_maxima

    @property
    def humedad(self):
        return self._humedad

    @humedad.setter
    def humedad(self, humedad):
        self._humedad = humedad

    @property
    def presion(self):
        return self._presion

    @presion.setter
    def presion(self, presion):
        self._presion = presion

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, longitud):
        self._longitud = longitud

    @property
    def latitud(self):
        return self._latitud

    @latitud.setter
    def latitud(self, latitud):
        self._latitud = latitud

    def imprimeInformacion(self):
        print('Datos climatológicos Generales para {}'.format(self.nombre))
        print('País : {} '.format(self.pais))
        print('Temperatura actual : {}'.format(LocalidadClima.cambiaCentigrados(self.temperatura)))
        print('Temperatura mínima : {}'.format(LocalidadClima.cambiaCentigrados(self.t_minima)))
        print('Temperatura máxima : {}'.format(LocalidadClima.cambiaCentigrados(self.t_maxima)))
        print('Humedad relativa : {}'.format(self.humedad))
        print('presión atmosférica : {}'.format(self.presion))
        print('coordenadas de la muestra : ({},{})'.format(self.latitud, self.longitud))

    @staticmethod
    def cambiaCentigrados(g_kelvin):
        return g_kelvin - 273.15


class GestorClima:
    api_key = 'c751c6d8002c04b266d0b8706c8b2f72'
    url_base = 'http://api.openweathermap.org/data/2.5/weather?'

    def __init__(self):
        self.url_completa = self.url_base + 'lat={}&lon={}&appid=' + self.api_key

    @property
    def url_completa(self):
        return self._url_completa

    @url_completa.setter
    def url_completa(self, url_completa):
        self._url_completa = url_completa

    def consultaCoordenadas(self, latitud=21.16072, longitud=-86.84906):
        url_formato= self.url_completa.format(latitud,longitud)
        respuesta=requests.get(url_formato)
        dicResponse=respuesta.json()
        if dicResponse['cod']==200:
            nombreCiudad=dicResponse["name"]
            nombrePais=""
            dicPrincipal=dicResponse["main"]
            tempActual=dicPrincipal["temp"]
            tempMin = dicPrincipal["temp_min"]
            tempMax = dicPrincipal["temp_max"]
            presion = dicPrincipal["pressure"]
            humedad= dicPrincipal["humidity"]
            clima=dicResponse["weather"]
            descripcion=clima[0]["description"]
            sysDoc=dicResponse["sys"]
            if "country" in sysDoc:
                nombrePais=sysDoc["country"]
            coordenadas=dicResponse["coord"]
            lon=coordenadas["lon"]
            lat=coordenadas["lat"]
                                             #nombre, pais  , temperatura, t_minima, t_maxima, humedad, presion, latitud, longitud)
            localidad= LocalidadClima(nombreCiudad, nombrePais, tempActual, tempMin,tempMax, humedad, presion, lat, lon)
            return localidad
        else:
            return None
def main():
    present = '''
    ================================================
    == Programa que presenta datos climatológicos ==
    == Generales para una ubicación geográfica    ==
    == definida por latitud y longitud            ==
    ================================================    
    '''
    print(present)
    latitud = float(input('Proporcione la latitud : '))
    longitud = float(input('Proporcione la longitud : '))

    gestor = GestorClima()
    localidad = gestor.consultaCoordenadas(latitud, longitud)
    if localidad != None:
        localidad.imprimeInformacion()


if __name__ == '__main__':
    main()
