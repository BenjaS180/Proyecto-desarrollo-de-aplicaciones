from tkinter import messagebox, ttk
from tkinter import *
from LN.bodegaClass import obtener_bodegas, guardar_bodega, actualizar_bodega, eliminar_bodega
from LN.productoClass import obtener_productos, guardar_producto, actualizar_producto, eliminar_producto
from LN.movimientodebodegaClass import obtener_colaborador, movimientobodega, obtener_historialmovimientos
from LN.colaboradorcredencialesClass import inicio_sesion, obtener_tipo_acceso, ingresar_credenciales
from LN.usuariosClass import selecusuario, obtener_id_usuario, ingresar_usuarios_data
from LN.colaboradoresClass import guardar_colaborador, obtener_colaborador1
from datetime import datetime


# Función para mostrar bodegas
def mostrar_bodega():
    # Función para actualizar los datos en la tabla
    def actualizar_tabla():
        # Borrar todos los registros de la tabla
        tabla.delete(*tabla.get_children())

        # Obtener los datos de las bodegas
        bodegas = obtener_bodegas()

        # Agregar los datos a la tabla
        for bodega in bodegas:
            tabla.insert("", "end", text="", values=(
                bodega.Idbodega,
                bodega.Nombre,
                bodega.Direccion,
                bodega.Jefeasignado,
                bodega.Capacidad,
                bodega.Niveldeocupacion,
                bodega.Correobodega,
                bodega.Numerofijo
            ))

            # Agrega aquí los datos adicionales de la bodega

    # Crear ventana secundaria para mostrar los datos de la bodega
    ventana_mostrar = Tk()
    ventana_mostrar.title("Bodegas")

    # Crear un widget Treeview para mostrar los datos en forma de tabla
    tabla = ttk.Treeview(ventana_mostrar)
    tabla.pack(expand=True, fill="both")

    # Configurar las columnas de la tabla
    tabla["columns"] = ("id", "nombre", "direccion", "jefe", "capacidad", "ocupacion", "correo", "numero")
    tabla.column("#0", width=0, stretch="NO")  # Columna invisible
    tabla.column("id", width=50, anchor="center")
    tabla.column("nombre", width=100)
    tabla.column("direccion", width=150)
    tabla.column("jefe", width=100)
    tabla.column("capacidad", width=80, anchor="center")
    tabla.column("ocupacion", width=120, anchor="center")
    tabla.column("correo", width=150)
    tabla.column("numero", width=100)

    # Configurar encabezados de las columnas
    tabla.heading("#0", text="")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("direccion", text="Dirección")
    tabla.heading("jefe", text="ID colaborador")
    tabla.heading("capacidad", text="Capacidad")
    tabla.heading("ocupacion", text="Nivel de ocupación")
    tabla.heading("correo", text="Correo Bodega")
    tabla.heading("numero", text="Número Fijo")

    # Obtener los datos de las bodegas
    bodegas = obtener_bodegas()

    # Agregar los datos a la tabla
    for bodega in bodegas:
        tabla.insert("", "end", text="", values=(
            bodega.Idbodega,
            bodega.Nombre,
            bodega.Direccion,
            bodega.Jefeasignado,
            bodega.Capacidad,
            bodega.Niveldeocupacion,
            bodega.Correobodega,
            bodega.Numerofijo
        ))

        # Agrega aquí los datos adicionales de la bodega

    # Crear un botón de actualización
    boton_actualizar = ttk.Button(ventana_mostrar, text="Actualizar", command=actualizar_tabla)
    boton_actualizar.pack()

    # Ejecutar ventana secundaria


# Funcion para mostrar productos
def mostrar_producto():
    # Función para actualizar los datos en la tabla
    def actualizar_tabla():
        # Borrar todos los registros de la tabla
        tabla.delete(*tabla.get_children())

        # Obtener los datos de los productos
        productos = obtener_productos()

        # Agregar los datos a la tabla
        for producto in productos:
            tabla.insert("", "end", text="", values=(
                producto.Idproducto,
                producto.Fechaing,
                producto.Cantidades,
                producto.Tipoproducto
            ))

            # Agrega aquí los datos adicionales del producto

    # Crear ventana secundaria para mostrar los datos de los productos
    ventana_mostrar = Tk()
    ventana_mostrar.title("Productos")

    # Crear un widget Treeview para mostrar los datos en forma de tabla
    tabla = ttk.Treeview(ventana_mostrar)
    tabla.pack(expand=True, fill="both")

    # Configurar las columnas de la tabla
    tabla["columns"] = ("id", "fecha", "cantidades", "tipo")
    tabla.column("#0", width=0, stretch="NO")  # Columna invisible
    tabla.column("id", width=100, anchor="center")
    tabla.column("fecha", width=150)
    tabla.column("cantidades", width=100, anchor="center")
    tabla.column("tipo", width=150)

    # Configurar encabezados de las columnas
    tabla.heading("#0", text="")
    tabla.heading("id", text="ID Producto")
    tabla.heading("fecha", text="Fecha de ingreso")
    tabla.heading("cantidades", text="Cantidades")
    tabla.heading("tipo", text="Tipo de producto")

    # Obtener los datos de los productos
    productos = obtener_productos()

    # Agregar los datos a la tabla
    for producto in productos:
        tabla.insert("", "end", text="", values=(
            producto.Idproducto,
            producto.Fechaing,
            producto.Cantidades,
            producto.Tipoproducto
        ))

        # Agrega aquí los datos adicionales del producto

    # Crear un botón de actualización
    boton_actualizar = ttk.Button(ventana_mostrar, text="Actualizar", command=actualizar_tabla)
    boton_actualizar.pack()

    # Ejecutar ventana secundaria
    ventana_mostrar.mainloop()


# Función para mostrar el historial de movimientos
def mostrar_historialesm():
    # Función para actualizar los datos en la tabla
    def actualizar_tabla():
        # Borrar todos los registros de la tabla
        tabla.delete(*tabla.get_children())

        # Obtener los datos de los historiales de movimientos
        historiales = obtener_historialmovimientos()

        # Agregar los datos a la tabla
        for historial in historiales:
            tabla.insert("", "end", text="", values=(
                historial.Fecha,
                historial.N_bodega_origen,
                historial.N_bodega_destino,
                historial.Id_colaborador,
                historial.Id_producto
            ))

            # Agrega aquí los datos adicionales del historial

    # Crear ventana secundaria para mostrar los datos de los historiales de movimientos
    ventana_mostrar = Tk()
    ventana_mostrar.title("Historial de movimientos")

    # Crear un widget Treeview para mostrar los datos en forma de tabla
    tabla = ttk.Treeview(ventana_mostrar)
    tabla.pack(expand=True, fill="both")

    # Configurar las columnas de la tabla
    tabla["columns"] = ("fecha", "bodega_origen", "bodega_destino", "colaborador", "producto")
    tabla.column("#0", width=0, stretch="NO")  # Columna invisible
    tabla.column("fecha", width=150)
    tabla.column("bodega_origen", width=200)
    tabla.column("bodega_destino", width=200)
    tabla.column("colaborador", width=100, anchor="center")
    tabla.column("producto", width=100, anchor="center")

    # Configurar encabezados de las columnas
    tabla.heading("#0", text="")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("bodega_origen", text="Bodega de Origen")
    tabla.heading("bodega_destino", text="Bodega de Destino")
    tabla.heading("colaborador", text="ID Colaborador")
    tabla.heading("producto", text="ID Producto")

    # Obtener los datos de los historiales de movimientos
    historiales = obtener_historialmovimientos()

    # Agregar los datos a la tabla
    for historial in historiales:
        tabla.insert("", "end", text="", values=(
            historial.Fecha,
            historial.N_bodega_origen,
            historial.N_bodega_destino,
            historial.Id_colaborador,
            historial.Id_producto
        ))

        # Agrega aquí los datos adicionales del historial

    # Crear un botón de actualización
    boton_actualizar = ttk.Button(ventana_mostrar, text="Actualizar", command=actualizar_tabla)
    boton_actualizar.pack()

    # Ejecutar ventana secundaria
    ventana_mostrar.mainloop()

# Función para ingresar un colaborador y crear sus credenciales
def ingresarusuarioc():
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar nuevo perfil")

    label_rutu = Label(ventana_ingreso, text="Ingrese el rut del usuario")
    label_rutu.pack()
    entry_rutu = Entry(ventana_ingreso)
    entry_rutu.pack()

    def abrir_interfaz(rut_colaborador):
        ventana_ingreso.destroy()  # Cerrar la ventana de ingreso
        id_usuario = obtener_id_usuario(rut_colaborador)

        if id_usuario is not None:
            ventana_nueva = Tk()
            ventana_nueva.title("Ingresar colaborador")

            label_id_usuario = Label(ventana_nueva, text="ID de Usuario: {}".format(id_usuario))
            label_id_usuario.pack()

            label_cargo = Label(ventana_nueva, text="Ingrese el cargo:")
            label_cargo.pack()
            entry_cargo = Entry(ventana_nueva)
            entry_cargo.pack()

            def crear_co():
                cargo = entry_cargo.get()
                guardar_colaborador(cargo, id_usuario)
                ventana_nueva.destroy()
                messagebox.showinfo("Éxito", "Colaborador ingresado con éxito.")
                c_credencial(id_usuario)

            boton_ingreso = Button(ventana_nueva, text="Crear", command=crear_co)
            boton_ingreso.pack()

            ventana_nueva.mainloop()
        else:
            print("No se encontró ningún usuario con el rut {}".format(rut_colaborador))

    def c_credencial(id_usuario):
        id_colaborador = obtener_colaborador1(id_usuario)
        ventana_nueva = Toplevel()
        ventana_nueva.title("Crear credenciales")

        label_usuario1 = Label(ventana_nueva, text="Ingrese Usuario:")
        label_usuario1.pack()
        entry_usuario1 = Entry(ventana_nueva)
        entry_usuario1.pack()

        label_contrasena1 = Label(ventana_nueva, text="Ingresar Contrasena:")
        label_contrasena1.pack()
        entry_contrasena1 = Entry(ventana_nueva, show="*")
        entry_contrasena1.pack()

        label_accesos1 = Label(ventana_nueva, text="Ingresar Accesos:")
        label_accesos1.pack()
        entry_accesos1 = Entry(ventana_nueva)
        entry_accesos1.pack()

        def guardar():
            usuario1 = entry_usuario1.get()
            contrasena2 = entry_contrasena1.get()
            accesos1 = entry_accesos1.get()
            ingresar_credenciales(id_colaborador, usuario1, contrasena2, accesos1)
            ventana_nueva.destroy()
            messagebox.showinfo("Éxito", "Credenciales creadas con éxito.")

        boton_ingresar = Button(ventana_nueva, text="Guardar", command=guardar)
        boton_ingresar.pack()

        ventana_nueva.mainloop()

    def ingresousuarioc():
        rut_colaborador = entry_rutu.get()
        if rut_colaborador:
            rut_colaborador = int(rut_colaborador)
            selecusuario(rut_colaborador)
            abrir_interfaz(rut_colaborador)
        else:
            print("Por favor, ingrese un RUT válido.")

    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresousuarioc)
    boton_guardar.pack()

    ventana_ingreso.mainloop()


# Función para agregar una bodega
def ingresar_datos_bodega():
    # Crear ventana secundaria para ingresar datos
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Bodega")

    # Etiquetas y campos de entrada para los datos de la bodega
    label_id = Label(ventana_ingreso, text="ID de la Bodega:")
    label_id.pack()
    entry_id = Entry(ventana_ingreso)
    entry_id.pack()

    label_nombre = Label(ventana_ingreso, text="Nombre de la Bodega:")
    label_nombre.pack()
    entry_nombre = Entry(ventana_ingreso)
    entry_nombre.pack()

    label_direccion = Label(ventana_ingreso, text="Dirección de la Bodega:")
    label_direccion.pack()
    entry_direccion = Entry(ventana_ingreso)
    entry_direccion.pack()

    label_capacidad = Label(ventana_ingreso, text="Capacidad de la Bodega:")
    label_capacidad.pack()
    entry_capacidad = Entry(ventana_ingreso)
    entry_capacidad.pack()

    label_nivelocupacion = Label(ventana_ingreso, text="Nivel de ocupacion de la Bodega:")
    label_nivelocupacion.pack()
    entry_nivelocupacion = Entry(ventana_ingreso)
    entry_nivelocupacion.pack()

    label_correobodega = Label(ventana_ingreso, text="Correo de la bodega")
    label_correobodega.pack()
    entry_correobodega = Entry(ventana_ingreso)
    entry_correobodega.pack()

    label_numerofijo = Label(ventana_ingreso, text="Numero fijo de la bodega")
    label_numerofijo.pack()
    entry_numerofijo = Entry(ventana_ingreso)
    entry_numerofijo.pack()

    def ingresar_bodega():
        # Obtener los valores ingresados por el usuario
        id_bodega = int(entry_id.get())
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        id_colaborador = obtener_colaborador(usuario, contrasena)
        capacidad = int(entry_capacidad.get())
        nivelocupacion = int(entry_nivelocupacion.get())
        correobodega = entry_correobodega.get()
        numerofijo = entry_numerofijo.get()
        # Agrega aquí el código para obtener los demás valores ingresados por el usuario

        # Guardar la bodega
        guardar_bodega(id_bodega, nombre, direccion, id_colaborador, capacidad, nivelocupacion, correobodega,
                       numerofijo)

        # Cerrar la ventana de ingreso de datos
        ventana_ingreso.destroy()

    # Botón para guardar los datos ingresados
    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_bodega)
    boton_guardar.pack()

    # Ejecutar ventana secundaria
    ventana_ingreso.mainloop()


# Función para ingresar datos de movimientos de bodega
def ingresar_datos_movimiento_bodega():
    # Crear ventana secundaria para ingresar datos
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Movimiento de Bodega")

    label_n_bodega_origen = Label(ventana_ingreso, text="Nombre de la Bodega Origen:")
    label_n_bodega_origen.pack()
    entry_n_bodega_origen = Entry(ventana_ingreso)
    entry_n_bodega_origen.pack()

    label_n_bodega_destino = Label(ventana_ingreso, text="ID de Bodega Destino:")
    label_n_bodega_destino.pack()
    entry_n_bodega_destino = Entry(ventana_ingreso)
    entry_n_bodega_destino.pack()

    label_id_producto = Label(ventana_ingreso, text="ID de producto:")
    label_id_producto.pack()
    entry_id_producto = Entry(ventana_ingreso)
    entry_id_producto.pack()

    def ingresar_movimiento_bodega():
        # Obtener los valores ingresados por el usuario

        fecha = datetime.now()
        n_bodega_origen = entry_n_bodega_origen.get()
        n_bodega_destino = entry_n_bodega_destino.get()
        id_colaborador = obtener_colaborador(usuario, contrasena)
        id_producto = entry_id_producto.get()

        # Guardar el movimiento de bodega
        movimientobodega(fecha, n_bodega_origen, n_bodega_destino, id_colaborador, id_producto)

        # Cerrar la ventana de ingreso de datos
        ventana_ingreso.destroy()

    # Botón para guardar los datos ingresados
    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_movimiento_bodega)
    boton_guardar.pack()

    # Ejecutar ventana secundaria
    ventana_ingreso.mainloop()


def ingresar_usuarios():
    # Crear ventana secundaria para ingresar datos
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Usuario")

    # Etiquetas y campos de entrada para los datos del usuario
    label_rut = Label(ventana_ingreso, text="RUT:")
    label_rut.pack()
    entry_rut = Entry(ventana_ingreso)
    entry_rut.pack()

    label_nombre = Label(ventana_ingreso, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(ventana_ingreso)
    entry_nombre.pack()

    label_apellido_p = Label(ventana_ingreso, text="Apellido Paterno:")
    label_apellido_p.pack()
    entry_apellido_p = Entry(ventana_ingreso)
    entry_apellido_p.pack()

    label_apellido_m = Label(ventana_ingreso, text="Apellido Materno:")
    label_apellido_m.pack()
    entry_apellido_m = Entry(ventana_ingreso)
    entry_apellido_m.pack()

    label_correo = Label(ventana_ingreso, text="Correo:")
    label_correo.pack()
    entry_correo = Entry(ventana_ingreso)
    entry_correo.pack()

    label_direccion = Label(ventana_ingreso, text="Dirección:")
    label_direccion.pack()
    entry_direccion = Entry(ventana_ingreso)
    entry_direccion.pack()

    label_numero_c = Label(ventana_ingreso, text="Número de Contacto:")
    label_numero_c.pack()
    entry_numero_c = Entry(ventana_ingreso)
    entry_numero_c.pack()

    def ingresar_usuario_data():
        # Obtener los valores ingresados por el usuario
        rut = entry_rut.get()
        nombre = entry_nombre.get()
        apellido_p = entry_apellido_p.get()
        apellido_m = entry_apellido_m.get()
        correo = entry_correo.get()
        direccion = entry_direccion.get()
        numero_c = entry_numero_c.get()

        # Guardar el usuario
        ingresar_usuarios_data(rut, nombre, apellido_p, apellido_m, correo, direccion, numero_c)

        # Cerrar la ventana de ingreso de datos
        ventana_ingreso.destroy()

    # Botón para guardar los datos ingresados
    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_usuario_data)
    boton_guardar.pack()

    # Ejecutar ventana secundaria
    ventana_ingreso.mainloop()


# Función para ingresar datos a producto
def ingresar_datos_producto():
    # Agrega aquí el código para ingresar los datos del producto
    ventana_ingreso = Tk()
    ventana_ingreso.title("Ingresar Producto")

    # Etiquegas y campos de entrada para los datos de producto
    label_idproducto = Label(ventana_ingreso, text="ID del Producto")
    label_idproducto.pack()
    entry_idproducto = Entry(ventana_ingreso)
    entry_idproducto.pack()

    label_cantidades = Label(ventana_ingreso, text="Cantidades de los productos")
    label_cantidades.pack()
    entry_cantidades = Entry(ventana_ingreso)
    entry_cantidades.pack()

    label_tipoproducto = Label(ventana_ingreso, text="Tipo de producto")
    label_tipoproducto.pack()
    entry_tipoproducto = Entry(ventana_ingreso)
    entry_tipoproducto.pack()

    def ingresar_producto():
        id_producto = int(entry_idproducto.get())
        fechaing = datetime.now()
        cantidades = int(entry_cantidades.get())
        tipoproducto = str(entry_tipoproducto.get())

        guardar_producto(id_producto, fechaing, cantidades, tipoproducto)

        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Guardar", command=ingresar_producto)
    boton_guardar.pack()


# Función para actualizar datos de bodegas
def solicitar_datos_actualizacion_bodega():
    ventana_ingreso = Tk()
    ventana_ingreso.title("Actualizar Bodega")

    label_idbodega = Label(ventana_ingreso, text="ID de la bodega")
    label_idbodega.pack()
    entry_idbodega = Entry(ventana_ingreso)
    entry_idbodega.pack()

    campos_posibles = ["nombre", "direccion", "ID_colaborador", "capacidad", "niveldeocupacion",
                       "correobodegas", "numerofijo"]

    label_campoactualizar = Label(ventana_ingreso, text="Campo que desea actualizar")
    label_campoactualizar.pack()

    campoactualizar = StringVar(ventana_ingreso)  # Crear instancia de StringVar
    campoactualizar.set(campos_posibles[0])

    opciones_campoactualizar = OptionMenu(ventana_ingreso, campoactualizar, *campos_posibles)
    opciones_campoactualizar.pack()

    label_campo_seleccionado = Label(ventana_ingreso, text="Campo seleccionado: " + campoactualizar.get())
    label_campo_seleccionado.pack()

    label_nuevovalor = Label(ventana_ingreso, text="Nuevo valor")
    label_nuevovalor.pack()
    entry_nuevovalor = Entry(ventana_ingreso)
    entry_nuevovalor.pack()

    def actualizar_campo_seleccionado(*args):
        label_campo_seleccionado.config(text="Campo seleccionado: " + campoactualizar.get())

    campoactualizar.trace("w", actualizar_campo_seleccionado)  # Actualizar el campo seleccionado al cambiar la opción

    def actualizacion_bodega():
        id_bodega = int(entry_idbodega.get())
        nuevovalor = str(entry_nuevovalor.get())

        campo_seleccionado = campoactualizar.get()
        actualizar_bodega(id_bodega, campo_seleccionado, nuevovalor)
        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Actualizar", command=actualizacion_bodega)
    boton_guardar.pack()


# Función para actualizar producto
def solicitar_datos_actualizacion_producto():
    ventana_ingreso = Tk()
    ventana_ingreso.title("Actualizar producto")

    label_idproducto = Label(ventana_ingreso, text="ID del Producto")
    label_idproducto.pack()
    entry_idproducto = Entry(ventana_ingreso)
    entry_idproducto.pack()

    campos_posibles = [ "cantidades", "tipo de producto"]

    label_campoactualizar = Label(ventana_ingreso, text="Campo que desea actualizar")
    label_campoactualizar.pack()

    campoactualizar = StringVar(ventana_ingreso)  # Crear instancia de StringVar
    campoactualizar.set(campos_posibles[0])

    opciones_campoactualizar = OptionMenu(ventana_ingreso, campoactualizar, *campos_posibles)
    opciones_campoactualizar.pack()

    label_campo_seleccionado = Label(ventana_ingreso, text="Campo seleccionado: " + campoactualizar.get())
    label_campo_seleccionado.pack()
    label_campo_seleccionado.pack()

    label_nuevovalor = Label(ventana_ingreso, text="Nuevo valor")
    label_nuevovalor.pack()
    entry_nuevovalor = Entry(ventana_ingreso)
    entry_nuevovalor.pack()

    def actualizar_campo_seleccionado(*args):
        label_campo_seleccionado.config(text="Campo seleccionado: " + campoactualizar.get())

        campoactualizar.trace("w", actualizar_campo_seleccionado)

    def actualizacion_producto():
        id_producto = int(entry_idproducto.get())
        nuevovalor = str(entry_nuevovalor.get())

        campo_seleccionado = campoactualizar.get()
        actualizar_producto(id_producto, campo_seleccionado, nuevovalor)
        ventana_ingreso.destroy()

    boton_guardar = Button(ventana_ingreso, text="Actualizar", command=actualizacion_producto)
    boton_guardar.pack()


# Función para eliminar bodega
def dato_eliminar_bodega():
    def abrir_ventana_eliminar_bodega():
        ventana_eliminar_bodega = Toplevel()
        ventana_eliminar_bodega.title("Eliminar Bodega")

        def eliminar_bodega_ventana():
            id_bodega = entry_id.get()
            eliminar_bodega(id_bodega)
            messagebox.showinfo("Eliminación exitosa", f"Bodega con ID {id_bodega} eliminada.")
            ventana_eliminar_bodega.destroy()

        label_id = Label(ventana_eliminar_bodega, text="ID de la Bodega:")
        label_id.pack()
        entry_id = Entry(ventana_eliminar_bodega)
        entry_id.pack()

        boton_eliminar = Button(ventana_eliminar_bodega, text="Eliminar", command=eliminar_bodega_ventana)
        boton_eliminar.pack()

    abrir_ventana_eliminar_bodega()


# Función para eliminar un producto
def dato_eliminar_producto():
    def abrir_ventana_eliminar_producto():
        ventana_eliminar_producto = Toplevel()
        ventana_eliminar_producto.title("Eliminar Producto")

        def eliminar_producto_ventana():
            id_producto = entry_id.get()
            eliminar_producto(id_producto)
            messagebox.showinfo("Eliminación exitosa", f"Producto con ID {id_producto} eliminado.")
            ventana_eliminar_producto.destroy()

        label_id = Label(ventana_eliminar_producto, text="ID del Producto:")
        label_id.pack()
        entry_id = Entry(ventana_eliminar_producto)
        entry_id.pack()

        boton_eliminar = Button(ventana_eliminar_producto, text="Eliminar", command=eliminar_producto_ventana)
        boton_eliminar.pack()

    abrir_ventana_eliminar_producto()


# Funciónes de interfaces, segun el usuario (1)JEFE DE BODEGA
def mostrar_interfaz_principal():
    # Crear ventana principal
    ventana = Tk()
    ventana.title("Programa de El loco")
    ventana.geometry("1125x250")

    marco_botones = Frame(ventana)
    marco_botones.pack(pady=10)

    # Etiqueta de título
    titulo = Label(ventana, text="Bienvenido jefe de bodega", font=("Arial", 20))
    titulo.pack(pady=10)

    # Botones
    boton_mostrar_bodega = Button(ventana, text="Mostrar Bodega", command=mostrar_bodega)
    boton_mostrar_bodega.pack(side="left", padx=10)

    boton_mostrar_producto = Button(ventana, text="Mostrar Producto", command=mostrar_producto)
    boton_mostrar_producto.pack(side="left", padx=10)

    boton_ingresar_bodega = Button(ventana, text="Ingresar Bodega", command=ingresar_datos_bodega)
    boton_ingresar_bodega.pack(side="left", padx=10)

    boton_ingresar_producto = Button(ventana, text="Ingresar Producto", command=ingresar_datos_producto)
    boton_ingresar_producto.pack(side="left", padx=10)

    boton_ingresar_movimiento = Button(ventana, text="Ingresar Movimiento", command=ingresar_datos_movimiento_bodega)
    boton_ingresar_movimiento.pack(side="left", padx=10)

    boton_actualizar_bodega = Button(ventana, text="Actualizar Bodega", command=solicitar_datos_actualizacion_bodega)
    boton_actualizar_bodega.pack(side="left", padx=10)

    boton_actualizar_producto = Button(ventana, text="Actualizar Producto",
                                       command=solicitar_datos_actualizacion_producto)
    boton_actualizar_producto.pack(side="left", padx=10)

    boton_eliminar_bodega = Button(ventana, text="Eliminar Bodega", command=dato_eliminar_bodega)
    boton_eliminar_bodega.pack(side="left", padx=10)

    boton_eliminar_producto = Button(ventana, text="Eliminar Producto", command=dato_eliminar_producto)
    boton_eliminar_producto.pack(side="left", padx=10)

    # Ejecutar ventana
    ventana.mainloop()


# Función de interfaces, segun el usuario (2)BODEGUERO
def mostrar_interfaz_secundario():
    # Crear ventana principal
    ventana = Tk()
    ventana.title("Programa de bodegas")
    ventana.geometry("650x200")

    marco_botones = Frame(ventana)
    marco_botones.pack(pady=10)

    # Etiqueta de título
    titulo = Label(ventana, text="Bienvenido Bodeguero", font=("Arial", 20))
    titulo.pack(pady=10)

    boton_mostrar_bodega = Button(ventana, text="Mostrar Bodega", command=mostrar_bodega)
    boton_mostrar_bodega.pack(side="left", padx=15)

    boton_mostrar_producto = Button(ventana, text="Mostrar Producto", command=mostrar_producto)
    boton_mostrar_producto.pack(side="left", padx=15)

    boton_ingresar_movimiento = Button(ventana, text="Ingresar Movimiento", command=ingresar_datos_movimiento_bodega)
    boton_ingresar_movimiento.pack(side="left", padx=15)

    boton_mostrar_historial = Button(ventana, text="Listar historial de movimientos", command=mostrar_historialesm)
    boton_mostrar_historial.pack(side="left", padx=15)


# Función de interfaces, segun el usuario (3)Administrador
def mostrar_interfaz_terciario():
    ventana = Tk()
    ventana.title("Programa de El loco")
    ventana.geometry("320x500")

    marco_botones = Frame(ventana)
    marco_botones.pack(pady=10)

    # Etiqueta de título
    titulo = Label(ventana, text="Bienvenido Administrador", font=("Arial", 20))
    titulo.pack(pady=10)

    boton_rut_usuario = Button(ventana, text="Ingresar usuario", command=ingresar_usuarios)
    boton_rut_usuario.pack(side="left", padx=15)

    boton_rut_usuario = Button(ventana, text="Crear nuevo colaborador", command=ingresarusuarioc)
    boton_rut_usuario.pack(side="left", padx=15)


# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales():
    global usuario
    global contrasena
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Verificar las credenciales llamando a la función inicio_sesion(usuario, contrasena)
    credenciales = inicio_sesion(usuario, contrasena)

    # Verificar si las credenciales son válidas
    if credenciales is not None:
        # Obtener el tipo de acceso
        tipo_acceso = obtener_tipo_acceso(usuario, contrasena)

        # Obtener el colaborador
        colaborador = obtener_colaborador(usuario, contrasena)

        if tipo_acceso is not None and colaborador is not None:
            # Mostrar un mensaje de éxito y continuar con la aplicación
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            ventana.title("Inicio de Sesión")
            ventana.destroy()  # Cerrar la ventana de inicio de sesión

            # Verificar el tipo de acceso y mostrar la interfaz correspondiente
            if tipo_acceso == 1:
                mostrar_interfaz_principal()
            elif tipo_acceso == 2:
                mostrar_interfaz_secundario()
            elif tipo_acceso == 3:
                mostrar_interfaz_terciario()
        else:
            # Mostrar un mensaje de error en caso de tipo de acceso inválido o colaborador no encontrado
            messagebox.showerror("Inicio de Sesión", "Tipo de acceso inválido o colaborador no encontrado")
    else:
        # Mostrar un mensaje de error en caso de credenciales incorrectas
        messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas")


ventana = Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x150")

# Etiqueta y campo de entrada para el usuario
label_usuario = Label(ventana, text="Usuario:")
label_usuario.pack()
entry_usuario = Entry(ventana)
entry_usuario.pack()

# Etiqueta y campo de entrada para la contraseña
label_contrasena = Label(ventana, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = Entry(ventana, show="*")
entry_contrasena.pack()

# Botón para verificar las credenciales
boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack()

# Ejecutar ventana de inicio de sesión
ventana.mainloop()
