from LD.conexion import DAO

dao = DAO()


class Producto:
    # Creamos el constructor con parametros
    def __init__(self, id_producto, fechaing, cantidades, tipoproducto):
        self.__id_producto = id_producto
        self.__fechaing = fechaing
        self.__cantidades = cantidades
        self.__tipoproducto = tipoproducto

    # Creamos metodos selectores
    def getid_producto(self):
        return self.__id_producto

    def getfechaing(self):
        return self.__fechaing

    def getcantidades(self):
        return self.__cantidades

    def gettipoproducto(self):
        return self.__tipoproducto

    # Creamos metodos mutadores
    def setid_producto(self, id_producto):
        self.__id_producto = id_producto

    def setfechaing(self, fechaing):
        self.__fechaing = fechaing

    def setcantidades(self, cantidades):
        self.__cantidades = cantidades

    def settipoproducto(self, tipoproducto):
        self.__tipoproducto = tipoproducto

    # Creamos metodos eliminadores
    def delid_producto(self):
        del self.__id_producto

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
                            doc='Soy la propiedad del tipoproducto')

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
            fechaing=datos[1],
            cantidades=datos[2],
            tipoproducto=datos[3]
        )
        productos.append(producto)

    return productos


def guardar_producto(id_producto,fechaing, cantidades, tipoproducto):
    producto = Producto(id_producto=id_producto,
                        fechaing=fechaing,
                        cantidades=cantidades,
                        tipoproducto=tipoproducto)

    producto_data = [producto.Idproducto, producto.Fechaing, producto.Cantidades,
                     producto.Tipoproducto]

    dao.Registrar_producto(*producto_data)


def actualizar_producto(id_producto, campo_actualizar, nuevo_valor):
    nuevos_datos = dao.actualizar_campo_producto(id_producto, campo_actualizar, nuevo_valor)
    return nuevos_datos


def eliminar_producto(id_opcion_eliminar):
    opcion_eliminar = dao.Eliminar_producto(id_opcion_eliminar)
    return opcion_eliminar
