from LD.conexion import DAO

dao = DAO()


class Producto:
    # Creamos el constructor con parametros
    def __init__(self, id_producto, id_editorial, fechaing, cantidades, tipoproducto):
        self.__id_producto = id_producto
        self.__id_editorial = id_editorial
        self.__fechaing = fechaing
        self.__cantidades = cantidades
        self.__tipoproducto = tipoproducto

    # Creamos metodos selectores
    def getid_producto(self):
        return self.__id_producto

    def getid_editorial(self):
        return self.__id_editorial

    def getfechaing(self):
        return self.__fechaing

    def getcantidades(self):
        return self.__cantidades

    def gettipoproducto(self):
        return self.__tipoproducto

    # Creamos metodos mutadores
    def setid_producto(self, id_producto):
        self.__id_producto = id_producto

    def setid_editorial(self, id_editorial):
        self.__id_editorial = id_editorial

    def setfechaing(self, fechaing):
        self.__fechaing = fechaing

    def setcantidades(self, cantidades):
        self.__cantidades = cantidades
    def settipoproducto(self, tipoproducto):
        self.__tipoproducto = tipoproducto

    # Creamos metodos eliminadores
    def delid_producto(self):
        del self.__id_producto

    def delid_editorial(self):
        del self.__id_editorial

    def delfechaing(self):
        del self.__fechaing

    def delcantidades(self):
        del self.__cantidades

    def deltipoproducto(self):
        del self.__tipoproducto


    # Creamos propiedades de atributos

    Idproducto = property(fget=getid_producto,
                          fset=setid_producto,
                          fdel=delid_producto,
                          doc="Soy la propiedad de la bodega")

    Id_editorial = property(fget=getid_editorial,
                            fset=setid_editorial,
                            fdel=delid_editorial,
                            doc="Soy la propiedad del id_editorial")

    Fechaing = property(fget=getfechaing,
                        fset=setfechaing,
                        fdel=delfechaing,
                        doc='Soy la propiedad de la direccion')

    Cantidades = property(fget=getcantidades,
                          fset=setcantidades,
                          fdel=delcantidades,
                          doc='Soy la propiedad del contacto')

    Tipoproducto = property(fget=gettipoproducto,
                         fset=settipoproducto,
                         fdel=deltipoproducto,
                         doc='Soy la propiedad de la Capacidad')

    # Creamos las operaciones del objeto.


def obtener_productos():
    resultados = dao.listar_productos()
    productos = convertir_a_productos(resultados)
    return productos


def convertir_a_productos(resultados):
    productos = []

    for datos in resultados:
        producto = Producto(
            id_producto=datos[0],
            id_editorial=datos[1],
            fechaing=datos[2],
            cantidades=datos[3],
            tipoproducto=datos[4]
        )
        productos.append(producto)

    return productos

