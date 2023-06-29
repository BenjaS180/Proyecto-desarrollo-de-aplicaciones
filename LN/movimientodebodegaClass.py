from LD.conexion import DAO

dao = DAO()


class Movimientodebodega:
    def __init__(self, fecha, id_bodega_origen, id_bodega_destino, id_colaborador,id_producto):
        self.__fecha = fecha
        self.__id_bodega_origen = id_bodega_origen
        self.__id_bodega_destino = id_bodega_destino
        self.__id_colaborador = id_colaborador
        self.__id_producto = id_producto


    def getfecha(self):
        return self.__fecha

    def getid_bodega_origen(self):
        return self.__id_bodega_origen

    def getid_bodega_destino(self):
        return self.__id_bodega_destino

    def getid_colaborador(self):
        return self.__id_colaborador

    def getid_producto(self):
        return self.__id_producto

    def setfecha(self, fecha):
        self.__fecha = fecha

    def setid_bodega_origen(self, id_bodega_origen):
        self.__id_bodega_origen = id_bodega_origen

    def setid_bodega_destino(self, id_bodega_destino):
        self.__id_bodega_destino = id_bodega_destino

    def setid_colaborador(self, id_colaborador):
        self.__id_colaborador = id_colaborador

    def setid_producto(self,id_producto):
        self.__id_producto = id_producto

    def delfecha(self):
        del self.__fecha

    def delid_bodega_origen(self):
        del self.__id_bodega_origen

    def delid_bodega_destino(self):
        del self.__id_bodega_destino

    def delid_colaborador(self):
        del self.__id_colaborador

    def delid_producto(self):
        del self.__id_producto

    Fecha = property(fget=getfecha,
                     fset=setfecha,
                     fdel=delfecha)
    Id_bodega_origen = property(fget=getid_bodega_origen,
                                fset=setid_bodega_origen,
                                fdel=delid_bodega_origen)
    Id_bodega_destino = property(fget=getid_bodega_destino,
                                 fset=setid_bodega_destino,
                                 fdel=delid_bodega_destino)
    Id_colaborador = property(fget=getid_colaborador,
                              fset=setid_colaborador,
                              fdel=delid_colaborador)
    Id_producto = property(fget=getid_producto,
                           fset=setid_producto,
                           fdel=delid_producto)


def obtener_colaborador(usuario, contrasena):
    resultados = dao.Iniciar_sesion(usuario, contrasena)

    if resultados is not None:
        id_colaborador = resultados[1]  # Obtener el valor de id_colaborador desde los resultados de la consulta
        return id_colaborador
    else:
        return None





def movimientobodega(fecha, id_bodega_origen, id_bodega_destino, id_colaborador,id_producto):
    mobodega = Movimientodebodega(fecha=fecha,
                                  id_bodega_origen=id_bodega_origen,
                                  id_bodega_destino=id_bodega_destino,
                                  id_colaborador=id_colaborador,
                                  id_producto=id_producto)

    # Pasar los valores individuales en lugar de la lista
    dao.Registrar_mobodega(mobodega.Fecha, mobodega.Id_bodega_origen, mobodega.Id_bodega_destino, mobodega.Id_colaborador,mobodega.Id_producto)