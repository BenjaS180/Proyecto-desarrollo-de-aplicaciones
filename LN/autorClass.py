class Autor:
    def __init__(self, id_autor, nombre, productoautor_id_productoautor):
        self.__id_autor = id_autor
        self.__nombre = nombre
        self.__productoautor_id_productoautor = productoautor_id_productoautor

    def get_id_autor(self):
        return self.__id_autor

    def set_id_autor(self, id_autor):
        self.__id_autor = id_autor

    def del_id_autor(self):
        del self.__id_autor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def del_nombre(self):
        del self.__nombre

    def get_productoautor_id_productoautor(self):
        return self.__productoautor_id_productoautor

    def set_productoautor_id_productoautor(self, productoautor_id_productoautor):
        self.__productoautor_id_productoautor = productoautor_id_productoautor

    def del_productoautor_id_productoautor(self):
        del self.__productoautor_id_productoautor

    id_autor = property(fget=get_id_autor,
                        fset=set_id_autor,
                        fdel=del_id_autor,
                        doc="Soy la propiedad id_autor")
    nombre = property(fget=get_nombre,
                      fset=set_nombre,
                      fdel=del_nombre,
                      doc="Soy la propiedad nombre")
    productoautor_id_productoautor = property(fget=get_productoautor_id_productoautor,
                                              fset=set_productoautor_id_productoautor,
                                              fdel=del_productoautor_id_productoautor,
                                              doc="Soy la propiedad productoautor_id_productoautor")