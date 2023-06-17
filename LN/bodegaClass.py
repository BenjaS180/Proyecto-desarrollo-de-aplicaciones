from LD.conexion import DAO

dao = DAO()

class Bodega:
    # Creamos el constructor con parametros
    def __init__(self, id_bodega, nombre, direccion, jefe_asignado, capacidad, niveldeocupacion, correobodega,
                 numerofijo):
        self.__id_bodega = id_bodega
        self.__nombre = nombre
        self.__direccion = direccion
        self.__jefe_asignado = jefe_asignado
        self.__capacidad = capacidad
        self.__niveldeocupacion = niveldeocupacion
        self.__correobodega = correobodega
        self.__numerofijo = numerofijo

    # Creamos metodos selectores
    def getid_bodega(self):
        return self.__id_bodega

    def getnombre(self):
        return self.__nombre

    def getdireccion(self):
        return self.__direccion

    def getjefe_asignado(self):
        return self.__jefe_asignado

    def getcapacidad(self):
        return self.__capacidad

    def getniveldeocupacion(self):
        return self.__niveldeocupacion

    def getcorreobodega(self):
        return self.__correobodega

    def getnumerofijo(self):
        return self.__numerofijo

    # Creamos metodos mutadores
    def setid_bodega(self, id_bodega):
        self.__id_bodega = id_bodega

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setdireccion(self, direccion):
        self.__direccion = direccion

    def setjefe_asignado(self, jefe_asignado):
        self.__jefe_asignado = jefe_asignado

    def setcapacidad(self, capacidad):
        self.__capacidad = capacidad

    def setniveldeocupacion(self, niveldeocupacion):
        self.__niveldeocupacion = niveldeocupacion

    def setcorreobodega(self, correobodega):
        self.__correobodega = correobodega

    def setnumerofijo(self, numerofijo):
        self.__numerofijo = numerofijo

    # Creamos metodos eliminadores
    def delid_bodega(self):
        del self.__id_bodega

    def delnombre(self):
        del self.__nombre

    def deldireccion(self):
        del self.__direccion

    def deljefe_asignado(self):
        del self.__jefe_asignado

    def delcapacidad(self):
        del self.__capacidad

    def delniveldeocupacion(self):
        del self.__niveldeocupacion

    def delcorreobodega(self):
        del self.__correobodega

    def delnumerofijo(self):
        del self.__numerofijo

    # Creamos propiedades de atributos

    Idbodega = property(fget=getid_bodega,
                        fset=setid_bodega,
                        fdel=delid_bodega,
                        doc="Soy la propiedad de la bodega")

    Nombre = property(fget=getnombre,
                      fset=setnombre,
                      fdel=delnombre,
                      doc="Soy la propiedad del nombre")

    Direccion = property(fget=getdireccion,
                         fset=setdireccion,
                         fdel=deldireccion,
                         doc='Soy la propiedad de la direccion')

    Jefeasignado = property(fget=getjefe_asignado,
                            fset=setjefe_asignado,
                            fdel=deljefe_asignado,
                            doc='Soy la propiedad del contacto')

    Capacidad = property(fget=getcapacidad,
                         fset=setcapacidad,
                         fdel=delcapacidad,
                         doc='Soy la propiedad de la Capacidad')

    Niveldeocupacion = property(fget=getniveldeocupacion,
                                fset=setniveldeocupacion,
                                fdel=delniveldeocupacion,
                                doc='Soy la propiedad del niveldeocupacion')

    Correobodega = property(fget=getcorreobodega,
                            fset=setcorreobodega,
                            fdel=delcorreobodega,
                            doc='Soy la propiedad del Email')

    Numerofijo = property(fget=getnumerofijo,
                          fset=setnumerofijo,
                          fdel=delnumerofijo,
                          doc='Soy la propiedad del numerofijo')

    # Creamos las operaciones del objeto.


def obtener_bodegas():
    resultados = dao.listar_bodegas()
    bodegas = convertir_a_bodegas(resultados)
    return bodegas


def convertir_a_bodegas(resultados):
    bodegas = []

    for datos in resultados:
        bodega = Bodega(
            id_bodega=datos[0],
            nombre=datos[1],
            direccion=datos[2],
            jefe_asignado=datos[3],
            capacidad=datos[4],
            niveldeocupacion=datos[5],
            correobodega=datos[6],
            numerofijo=datos[7]
        )
        bodegas.append(bodega)

    return bodegas
