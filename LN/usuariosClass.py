from LD.conexion import DAO

dao = DAO()


class Usuarios:
    def __init__(self, rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c):
        self.__rut = rut
        self.__nombre = nombre
        self.__apellido_p = apellido_p
        self.__apellido_m = apellido_m
        self.__correo = correo
        self.__direccion = direccion
        self.__numero_c = numero_c

    def getrut(self):
        return self.__rut

    def setrut(self, rut):
        self.__rut = rut

    def delrut(self):
        del self.__rut

    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

    def delnombre(self):
        del self.__nombre

    def getapellido_p(self):
        return self.__apellido_p

    def setapellido_p(self, apellido_p):
        self.__apellido_p = apellido_p

    def delapellido_p(self):
        del self.__apellido_p

    def getapellido_m(self):
        return self.__apellido_m

    def setapellido_m(self, apellido_m):
        self.__apellido_m = apellido_m

    def delapellido_m(self):
        del self.__apellido_m

    def getcorreo(self):
        return self.__correo

    def setcorreo(self, correo):
        self.__correo = correo

    def delcorreo(self):
        del self.__correo

    def getdireccion(self):
        return self.__direccion

    def setdireccion(self, direccion):
        self.__direccion = direccion

    def deldireccion(self):
        del self.__direccion

    def getnumero_c(self):
        return self.__numero_c

    def setnumero_c(self, numero_c):
        self.__numero_c = numero_c

    def delnumero_c(self):
        del self.__numero_c

    Rut = property(fget=getrut,
                   fset=setrut,
                   fdel=delrut,
                   doc="Soy la propiedad Rut")
    Nombre = property(fget=getnombre,
                      fset=setnombre,
                      fdel=delnombre,
                      doc="Soy la propiedad Nombre")
    Apellido_P = property(fget=getapellido_p,
                          fset=setapellido_p,
                          fdel=delapellido_p,
                          doc="Soy la propiedad Apellido_P")
    Apellido_M = property(fget=getapellido_m,
                          fset=setapellido_m,
                          fdel=delapellido_m,
                          doc="Soy la propiedad Apellido_M")
    Correo = property(fget=getcorreo,
                      fset=setcorreo,
                      fdel=delcorreo,
                      doc="Soy la propiedad Correo")
    Direccion = property(fget=getdireccion,
                         fset=setdireccion,
                         fdel=deldireccion,
                         doc="Soy la propiedad Direccion")
    Numero_C = property(fget=getnumero_c,
                        fset=setnumero_c,
                        fdel=delnumero_c,
                        doc="Soy la propiedad Numero_C")


def selecusuario(rut):
    resultado = dao.Consulta_usuario(rut)  # Llama a la función de la capa de datos

    if resultado is not None:
        id_usuario = resultado[0]  # El resultado es una lista de tuplas, obtenemos el primer elemento de la primera tupla
        # Haz lo que necesites con el id_usuario
        print("El id_usuario correspondiente al rut {} es: {}".format(rut, id_usuario))
    else:
        print("No se encontró ningún usuario con el rut {}".format(rut))


def obtener_id_usuario(rut):
    resultado = dao.Consulta_usuario(rut)  # Llama a la función de la capa de datos

    if resultado is not None:
        id_usuario = resultado[0]  # El resultado es una tupla, obtenemos el primer elemento
        return id_usuario
    else:
        return None


def ingresar_usuarios_data(rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c):
    usuario = Usuarios(rut=rut,
                       nombre=nombre,
                       apellido_p=apellido_p,
                       apellido_m=apellido_m,
                       correo=correo,
                       direccion=direccion,
                       numero_c=numero_c
                       )
    usuario_data = [usuario.Rut, usuario.Nombre, usuario.Apellido_P, usuario.Apellido_M, usuario.Correo,
                    usuario.Direccion, usuario.Numero_C]

    dao.Registrar_usuario(*usuario_data)
