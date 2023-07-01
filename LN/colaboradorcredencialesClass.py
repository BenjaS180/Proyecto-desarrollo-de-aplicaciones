from LD.conexion import DAO

dao = DAO()


class Colaborador_credenciales:
    def __init__(self, id_colaborador, usuario, contrasena, accesos):
        self.__id_colaborador = id_colaborador
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__accesos = accesos

    def getid_colaborador(self):
        return self.__id_colaborador

    def setid_colaborador(self, id_colaborador):
        self.__id_colaborador = id_colaborador

    def delid_colaborador(self):
        del self.__id_colaborador

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

    ID_colaborador = property(fget=getid_colaborador,
                              fset=setid_colaborador,
                              fdel=delid_colaborador,
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
                       fdel=delaccesos)


def inicio_sesion(usuario, contrasena):
    credenciales = dao.Iniciar_sesion(usuario, contrasena)
    return credenciales


def ingresar_credenciales(id_colaborador, usuario, contrasena, accesos):
    colaborador = Colaborador_credenciales(
        id_colaborador=id_colaborador,
        usuario=usuario,
        contrasena=contrasena,
        accesos=accesos
    )

    colaborador_data = [
        colaborador.ID_colaborador,
        colaborador.Usuario,
        colaborador.Contrasena,
        colaborador.Accesos
    ]

    dao.Registrar_credenciales(*colaborador_data)


def obtener_tipo_acceso(usuario, contrasena):
    accesos = dao.Iniciar_sesion(usuario, contrasena)

    if accesos is not None:
        tipo_acceso = accesos[0]  # Obtener el valor del tipo de acceso desde los resultados de la consulta
        return tipo_acceso
    else:
        return None
