import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                db="elloco",
            )

        except Error as ex:
            print("Error al intentar la conexion: {}".format(ex))


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

