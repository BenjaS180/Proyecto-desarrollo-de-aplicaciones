class Editoriales:
    def __init__(self, id_editorial, nombre, cantidad):
        self.__id_editorial = id_editorial
        self.__nombre = nombre
        self.__cantidad = cantidad

    def get_id_editorial(self):
        return self.__id_editorial

    def set_id_editorial(self, id_editorial):
        self.__id_editorial = id_editorial

    def del_id_editorial(self):
        del self.__id_editorial

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def del_nombre(self):
        del self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def del_cantidad(self):
        del self.__cantidad

    id_editorial = property(fget=get_id_editorial,
                            fset=set_id_editorial,
                            fdel=del_id_editorial,
                            doc="Soy la propiedad id_editorial")
    nombre = property(fget=get_nombre,
                      fset=set_nombre,
                      fdel=del_nombre,
                      doc="Soy la propiedad nombre")
    cantidad = property(fget=get_cantidad,
                        fset=set_cantidad,
                        fdel=del_cantidad,
                        doc="Soy la propiedad cantidad")