import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="elloco",
            )

        except Error as ex:
            print("Error al intentar la conexion: {}".format(ex))

    # Funciones para listar bodega
    def listar_bodegas(self):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from bodega;")
                resultados = cursor.fetchall()
                return resultados

            except  Error as ex:
                print("Error al intentar la conexion: {}".format(ex))

    def listar_productos(self):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from productos;")
                resultados = cursor.fetchall()
                return resultados

            except  Error as ex:
                print("Error al intentar la conexion: {}".format(ex))

    # Funciones para ingresar datos
    def Registrar_bodega(self, id_bodega, nombre, direccion, jefe_asignado, capacidad, nivelocupacion, correobodega,
                         numerofijo):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO bodega(id_bodega, nombre, direccion, jefe_asignado, capacidad, niveldeocupacion, correobodegas, numerofijo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_bodega, nombre, direccion, jefe_asignado, capacidad, nivelocupacion, correobodega, numerofijo))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_producto(self, id_producto, id_editorial, fechaing, cantidades, tipoproducto):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO productos(id_producto, id_editorial, fechaing, cantidades, tipoproducto) VALUES (%s, %s, %s, %s, %s)""",
                    (id_producto, id_editorial, fechaing, cantidades, tipoproducto))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))
