from LD.conexion import DAO

dao = DAO()


class Colaborador_credenciales:
    def __init__(self, ID, ID_colaborador, usuario, contrasena, accesos):
        self.__ID = ID
        self.__ID_colaborador = ID_colaborador
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__accesos = accesos

    def getID(self):
        return self.__ID

    def setID(self, ID):
        self.__ID = ID

    def delID(self):
        del self.__ID

    def getID_colaborador(self):
        return self.__ID_colaborador

    def setID_colaborador(self, ID_colaborador):
        self.__ID_colaborador = ID_colaborador

    def delID_colaborador(self):
        del self.__ID_colaborador

    def getusuario(self):
        return self.__usuario

    def setusuario(self, usuario):
        self.__usuario = usuario

    def delusuario(self):
        del self.__usuario

    def getcontrasena(self):
        return self.__contrasena

    def setcontrasena(self, contrasena):
        self.__contrasena = contrasena

    def delcontrasena(self):
        del self.__contrasena

    def getaccesos(self):
        return self.__accesos

    def setaccesos(self, accesos):
        self.__accesos = accesos

    def delaccesos(self):
        del self.__accesos

    ID = property(fget=getID,
                  fset=setID,
                  fdel=delID,
                  doc="Soy la propiedad ID")
    ID_colaborador = property(fget=getID_colaborador,
                              fset=setID_colaborador,
                              fdel=delID_colaborador,
                              doc="Soy la propiedad ID_colaborador")
    Usuario = property(fget=getusuario,
                       fset=setusuario,
                       fdel=delusuario,
                       doc="Soy la propiedad usuario")
    Contrasena = property(fget=getcontrasena,
                          fset=setcontrasena,
                          fdel=delcontrasena,
                          doc="Soy la propiedad contrasena")

    Accesos = property(fget=getaccesos,
                       fset=setaccesos,
                       fdel=delaccesos,
                       doc="Soy la propiedad del acceso")


def inicio_sesion(usuario, contrasena):
    credenciales = dao.Iniciar_sesion(usuario, contrasena)
    return credenciales

def obtener_tipo_acceso(usuario, contrasena):
    accesos = dao.Iniciar_sesion(usuario, contrasena)

    if accesos is not None:
        tipo_acceso = Colaborador_credenciales.Accesos = accesos[0]  # Obtener el valor del tipo de acceso desde los resultados de la consulta
        return tipo_acceso
    else:
        return None
