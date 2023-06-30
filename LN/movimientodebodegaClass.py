from LD.conexion import DAO

dao = DAO()


class Movimientodebodega:
    def __init__(self, fecha, n_bodega_origen, n_bodega_destino, id_colaborador, id_producto):
        self.__fecha = fecha
        self.__n_bodega_origen = n_bodega_origen
        self.__n_bodega_destino = n_bodega_destino
        self.__id_colaborador = id_colaborador
        self.__id_producto = id_producto

    def getfecha(self):
        return self.__fecha

    def getn_bodega_origen(self):
        return self.__n_bodega_origen

    def getn_bodega_destino(self):
        return self.__n_bodega_destino

    def getid_colaborador(self):
        return self.__id_colaborador

    def getid_producto(self):
        return self.__id_producto

    def setfecha(self, fecha):
        self.__fecha = fecha

    def setn_bodega_origen(self, n_bodega_origen):
        self.__n_bodega_origen = n_bodega_origen

    def setn_bodega_destino(self, n_bodega_destino):
        self.__n_bodega_destino = n_bodega_destino

    def setid_colaborador(self, id_colaborador):
        self.__id_colaborador = id_colaborador

    def setid_producto(self, id_producto):
        self.__id_producto = id_producto

    def delfecha(self):
        del self.__fecha

    def deln_bodega_origen(self):
        del self.__n_bodega_origen

    def deln_bodega_destino(self):
        del self.__n_bodega_destino

    def delid_colaborador(self):
        del self.__id_colaborador

    def delid_producto(self):
        del self.__id_producto

    Fecha = property(fget=getfecha,
                     fset=setfecha,
                     fdel=delfecha)
    N_bodega_origen = property(fget=getn_bodega_origen,
                               fset=setn_bodega_origen,
                               fdel=deln_bodega_origen)
    N_bodega_destino = property(fget=getn_bodega_destino,
                                fset=setn_bodega_destino,
                                fdel=deln_bodega_destino)
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


def movimientobodega(fecha, n_bodega_origen, n_bodega_destino, id_colaborador, id_producto):
    mobodega = Movimientodebodega(fecha=fecha,
                                  n_bodega_origen=n_bodega_origen,
                                  n_bodega_destino=n_bodega_destino,
                                  id_colaborador=id_colaborador,
                                  id_producto=id_producto)

    # Pasar los valores individuales en lugar de la lista
    dao.Registrar_mobodega(mobodega.Fecha, mobodega.N_bodega_origen, mobodega.N_bodega_destino,
                           mobodega.Id_colaborador, mobodega.Id_producto)


def obtener_historialmovimientos():
    resultados = dao.Listar_historialbodega()
    historiales = convertir_historial(resultados)
    return historiales


def convertir_historial(resultados):
    historiales = []

    for datos in resultados:
        historial = Movimientodebodega(
            fecha=datos[1],
            n_bodega_origen=datos[2],
            n_bodega_destino=datos[3],
            id_colaborador=datos[4],
            id_producto=datos[5]
        )
        historiales.append(historial)

    return historiales
