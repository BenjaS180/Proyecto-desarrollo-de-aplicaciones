from LD.conexion import DAO

dao = DAO()

class Colaborador:
    def __init__(self, id_colaborador, id_usuario, cargo):
        self.__id_colaborador = id_colaborador
        self.__id_usuario = id_usuario
        self.__cargo = cargo

    def getid_colaborador(self):
        return self.__id_colaborador

    def getid_usuario(self):
        return self.__id_usuario

    def getcargo(self):
        return self.__cargo

    def setid_colaborador(self, id_colaborador):
        self.__id_colaborador = id_colaborador

    def setid_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def setcargo(self, cargo):
        self.__cargo = cargo


    def delid_colaborador(self):
        del self.__id_colaborador

    def delid_usuario(self):
        del self.__id_usuario

    def delcargo(self):
        del self.__cargo


    id_colaborador = property(fget=getid_colaborador,
                              fset=setid_colaborador,
                              fdel=delid_colaborador)
    id_usuario = property(fget=getid_usuario,
                          fset=setid_usuario,
                          fdel=delid_usuario)
    cargo = property(fget=getcargo,
                     fset=setcargo,
                     fdel=delcargo)
