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

    # Funciones para listar
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

    def Listar_historialbodega(self):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from movimiento_bodega ;")
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
                    """INSERT INTO bodega(ID_bodega, nombre, direccion, ID_colaborador, capacidad, nivel_ocupacion, correo_bodegas, numero_fijo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_bodega, nombre, direccion, jefe_asignado, capacidad, nivelocupacion, correobodega, numerofijo))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_producto(self, id_producto, fechaing, cantidades, tipoproducto):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO productos(ID_producto, fecha_ing, cantidades, tipo_producto) VALUES (%s, %s, %s, %s)""",
                    (id_producto, fechaing, cantidades, tipoproducto))
                print('Campo ingresado con exito')
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_mobodega(self, fecha, n_bodega_origen, n_bodega_destino, id_colaborador, id_producto):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO movimiento_bodega(fecha, n_bodega_origen, n_bodega_destino, ID_colaborador,ID_producto) VALUES (%s, %s, %s, %s,%s)""",
                    (fecha, n_bodega_origen, n_bodega_destino, id_colaborador, id_producto))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_colaborador(self, cargo, id_usuario):
        if self.conexion.is_connected():

            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO colaborador(cargo, ID_usuarios) VALUES (%s, %s)""",
                    (cargo, id_usuario))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_credenciales(self,id_colaborador,usuario,contrasena,accesos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO colaborador_credenciales(ID_colaborador,usuario,contrasena,accesos) VALUES (%s, %s, %s, %s)""",
                    (id_colaborador,usuario,contrasena,accesos))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))

    def Registrar_usuario(self,rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """INSERT INTO usuarios(rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c) VALUES (%s, %s, %s, %s,%s, %s, %s)""",
                    (rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c))
                self.conexion.commit()

            except  Error as ex:

                print("Error al intentar la conexion: {}".format(ex))



    def actualizar_campo_bodega(self, id_bodega, campo_actualizar, nuevo_valor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE bodega SET {} = %s WHERE ID_bodega = %s".format(campo_actualizar)
                cursor.execute(query, (nuevo_valor, id_bodega))
                self.conexion.commit()
                print("Campo actualizado exitosamente en la tabla 'bodega'.")
            except Error as ex:
                print("Error al intentar actualizar campo en la tabla 'bodega': {}".format(ex))

    def actualizar_campo_producto(self, id_producto, campo_actualizar, nuevo_valor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE productos SET {} = %s WHERE ID_producto = %s".format(campo_actualizar)
                cursor.execute(query, (nuevo_valor, id_producto))
                self.conexion.commit()
                print("Campo actualizado exitosamente en la tabla 'productos'.")
            except Error as ex:
                print("Error al intentar actualizar campo en la tabla 'productos': {}".format(ex))

    def Eliminar_bodega(self, id_opcion_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('DELETE FROM bodega WHERE ID_bodega = %s', (id_opcion_eliminar,))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexion: {}".format(ex))

    def Eliminar_producto(self, id_opcion_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('DELETE FROM productos WHERE ID_producto = %s', (id_opcion_eliminar,))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexion: {}".format(ex))

    def Iniciar_sesion(self, usuario, contrasena):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """SELECT accesos,ID_colaborador FROM colaborador_credenciales WHERE usuario = %s AND contrasena = %s""",
                    (usuario, contrasena)
                )

                # Obtener el resultado de la consulta
                resultados = cursor.fetchone()
                return resultados

            except Error as ex:
                print("Error al intentar la conexión: {}".format(ex))
        else:
            print("No se pudo establecer una conexión a la base de datos.")

    # Consulta de datos varios:
    def Consulta_usuario(self,rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """SELECT ID_usuarios FROM usuarios WHERE rut = %s""",
                    (rut,)
                )

                # Obtener el resultado de la consulta
                resultados = cursor.fetchone()
                return resultados

            except Error as ex:
                print("Error al intentar la conexión: {}".format(ex))
        else:
            print("No se pudo establecer una conexión a la base de datos.")

    def Consulta_colaborador(self,id_usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """SELECT id_colaborador FROM colaborador WHERE ID_usuarios = %s""",
                    (id_usuario,)
                )

                # Obtener el resultado de la consulta
                resultados = cursor.fetchone()
                return resultados

            except Error as ex:
                print("Error al intentar la conexión: {}".format(ex))
        else:
            print("No se pudo establecer una conexión a la base de datos.")