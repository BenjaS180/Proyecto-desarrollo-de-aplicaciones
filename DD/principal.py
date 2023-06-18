from mysql.connector import Error
from datetime import datetime
from LN.bodegaClass import obtener_bodegas, guardar_bodega,actualizar_bodega
from LN.productoClass import obtener_productos, guardar_producto,actualizar_producto


# FUNCIONES DE INGRESO DE DATOS A BODEGA
def ingresar_datos_bodega():
    id_bodega = input("Ingrese el ID de la bodega: ")
    nombre = input("Ingrese el nombre de la bodega: ")
    direccion = input("Ingrese la dirección de la bodega: ")
    jefe_asignado = input("Ingrese el jefe asignado de la bodega: ")
    capacidad = input("Ingrese la capacidad de la bodega: ")
    nivel_ocupacion = input("Ingrese el nivel de ocupación de la bodega: ")
    correo_bodega = input("Ingrese el correo de la bodega: ")
    numero_fijo = input("Ingrese el número fijo de la bodega: ")

    bodega = guardar_bodega(id_bodega, nombre, direccion, jefe_asignado, capacidad, nivel_ocupacion, correo_bodega,
                            numero_fijo)
    return bodega


def ingresar_datos_producto():
    id_producto = input('Ingrese el id del producto: ')
    id_editorial = input('Ingrese el id de la editorial: ')
    print('se agregara la fecha de ingreso automaticamente !')
    fechaing = datetime.now()
    cantidades = input('Ingrese la/s cantidad/es: ')
    tipoproducto = input('Ingrese el tipodeproducto: ')

    producto = guardar_producto(id_producto, id_editorial, fechaing, cantidades, tipoproducto)
    return producto


def solicitar_datos_actualizacion_bodega():
    # Solicitar el ID de la bodega a actualizar
    id_bodega = input("Ingrese el ID de la bodega a actualizar: ")

    # Solicitar el nombre del campo a actualizar
    campo_actualizar = input("Ingrese el nombre del campo a actualizar: ")

    # Solicitar el nuevo valor para el campo
    nuevo_valor = input("Ingrese el nuevo valor para el campo: ")

    Actualizar_bodega = actualizar_bodega(id_bodega, campo_actualizar, nuevo_valor)
    return Actualizar_bodega


def solicitar_datos_actualizacion_producto():
    # Solicitar el ID del producto a actualizar
    id_producto = input("Ingrese el ID del producto a actualizar: ")

    # Solicitar el nombre del campo a actualizar
    campo_actualizar = input("Ingrese el nombre del campo a actualizar: ")

    # Solicitar el nuevo valor para el campo
    nuevo_valor = input("Ingrese el nuevo valor para el campo: ")

    Actualizar_producto = actualizar_producto(id_producto, campo_actualizar, nuevo_valor)
    return Actualizar_producto


def menuPrincipal():
    while True:
        print('================MENU PRINCIPAL================')
        print('1.- Listar ')
        print('2.- Registrar')
        print('3.- Actualizar')
        print('4.- Eliminar')
        print('5.- Salir')
        print('==============================================')
        opcion = int(input('Seleccione una opcion: '))

        if opcion < 1 or opcion > 5:
            print("Opcion incorrecta, ingrese nuevamente...")
        else:
            if opcion == 1:
                opcion_listar_bodegas = int(input('Que informacion desea listar   1)Bodegas 2)Productos: '))
                if opcion_listar_bodegas == 1:
                    try:
                        bodegas = obtener_bodegas()
                        for bodega in bodegas:
                            print("ID: ", bodega.Idbodega)
                            print("Nombre: ", bodega.Nombre)
                            print("Dirección: ", bodega.Direccion)
                            print("Jefe Asignado: ", bodega.Jefeasignado)
                            print("Capacidad: ", bodega.Capacidad)
                            print("Nivel de Ocupación: ", bodega.Niveldeocupacion)
                            print("Correo Bodega: ", bodega.Correobodega)
                            print("Número Fijo: ", bodega.Numerofijo)
                            print("")

                        realizar_otra_opcion = input("¿Desea realizar otra opción? (S/N): ")
                        if realizar_otra_opcion.upper() != "S":
                            break
                    except Error as ex:
                        print("Ocurrio un error...")
                        print("Error capturado: {}".format(ex))

                elif opcion_listar_bodegas == 2:
                    try:
                        productos = obtener_productos()
                        for producto in productos:
                            print("ID Producto: ", producto.Idproducto)
                            print("ID Editorial: ", producto.Id_editorial)
                            print("Fechaing: ", producto.Fechaing)
                            print("Cantidades: ", producto.Cantidades)
                            print("Tipo de producto: ", producto.Tipoproducto)
                            print("")

                        realizar_otra_opcion = input("¿Desea realizar otra opción? (S/N): ")
                        if realizar_otra_opcion.upper() != "S":
                            break
                    except Error as ex:
                        print("Ocurrio un error...")
                        print("Error capturado: {}".format(ex))
            elif opcion == 2:
                opcion_crear = int(input("Donde desea ingresar la nueva lista de datos 1)Bodegas 2)Productos: "))
                if opcion_crear == 1:
                    ingresar_datos_bodega()
                else:
                    ingresar_datos_producto()

            elif opcion == 3:
                opcion_actualizar = int(input('Que lista desea actualizar: 1)Bodega 2)Producto'))
                if opcion_actualizar == 1:
                    print('Eligio actualizar un campo de la bodega')
                    solicitar_datos_actualizacion_bodega()
                else:
                    print('Eligio actualizar un campo de los productos')
                    solicitar_datos_actualizacion_producto()


            elif opcion == 4:
                pass
            else:
                print("Gracias por usar este sistema!!!")
                break


menuPrincipal()
