from LD.conexion import DAO

dao = DAO()


class Usuarios:
    def __init__(self, id_usuarios, rut, nombre, apellido, correo, direccion, numeroc):
        self.__id_usuarios = id_usuarios
        self.__rut = rut
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__direccion = direccion
        self.__numeroc = numeroc

    def getid_usuarios(self):
        return self.__id_usuarios

    def getrut(self):
        return self.__rut

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido

    def getcorreo(self):
        return self.__correo

    def getdireccion(self):
        return self.__direccion

    def getnumeroc(self):
        return self.__numeroc

    def setid_usuarios(self, id_usuarios):
        self.__id_usuarios = id_usuarios

    def setrut(self, rut):
        self.__rut = rut

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setapellido(self, apellido):
        self.__apellido = apellido

    def setcorreo(self, correo):
        self.__correo = correo

    def setdireccion(self, direccion):
        self.__direccion = direccion

    def setnumeroc(self, numeroc):
        self.__numeroc = numeroc

    def delid_usuarios(self):
        del self.__id_usuarios

    def delrut(self):
        del self.__rut

    def delnombre(self):
        del self.__nombre

    def delapellido(self):
        del self.__apellido

    def delcorreo(self):
        del self.__correo

    def deldireccion(self):
        del self.__direccion

    def delnumeroc(self):
        del self.__numeroc

    Id_usuarios = property(fget=getid_usuarios,
                           fset=setid_usuarios,
                           fdel=delid_usuarios,
                           doc="Soy la propiedad id_usuarios")
    Rut = property(fget=getrut,
                   fset=setrut,
                   fdel=delrut,
                   doc="Soy la propiedad del rut")
    Nombre = property(fget=getnombre,
                      fset=setnombre,
                      fdel=delnombre, doc="Soy la propiedad del nombre")
    Apellido = property(fget=getapellido,
                        fset=setapellido,
                        fdel=delapellido,
                        doc="Soy la propiedad del apellido")
    Correo = property(fget=getcorreo,
                      fset=setcorreo,
                      fdel=delcorreo,
                      doc="Soy la propiedad del correo")
    Direccion = property(fget=getdireccion,
                         fset=setdireccion,
                         fdel=deldireccion,
                         doc="Soy la propiedad direccion")
    Numeroc = property(fget=getnumeroc,
                       fset=setnumeroc,
                       fdel=delnumeroc,
                       doc="Soy la propiedad del numeroc")
