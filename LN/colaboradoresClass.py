from LD.conexion import DAO

dao = DAO()


class Colaborador:
    def __init__(self, cargo, id_usuario):
        self.__cargo = cargo
        self.__id_usuario = id_usuario

    def getcargo(self):
        return self.__cargo

    def getid_usuario(self):
        return self.__id_usuario

    def setcargo(self, cargo):
        self.__cargo = cargo

    def setid_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def delcargo(self):
        del self.__cargo

    def delid_usuario(self):
        del self.__id_usuario

    Cargo = property(fget=getcargo,
                     fset=setcargo,
                     fdel=delcargo)
    Id_usuario = property(fget=getid_usuario,
                          fset=setid_usuario,
                          fdel=delid_usuario)


def guardar_colaborador(cargo,id_usuario):
    colaborador = Colaborador(cargo=cargo,
                              id_usuario=id_usuario)

    # Hay que convertir la Bodega objeto a un dato que la estructura sea compatible con la funcion que existe en dao
    colaborador_data = [colaborador.Cargo, colaborador.Id_usuario]

    dao.Registrar_colaborador(*colaborador_data)



def obtener_colaborador1(id_usuario):
    resultado = dao.Consulta_colaborador(id_usuario)  # Llama a la función de la capa de datos

    if resultado is not None:
        id_colaborador = resultado[0]  # El resultado es una tupla, obtenemos el primer elemento
        return id_colaborador
    else:
        return None