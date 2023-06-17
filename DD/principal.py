from LD.conexion import DAO
from mysql.connector import Error
from LN.bodegaClass import obtener_bodegas

dao = DAO()
listaProveedores = []

def menuPrincipal():
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
        menuPrincipal()
    else:
        if opcion == 1:
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


            except Error as ex:
                print("Ocurrio un error...")
                print("Error capturado: {}".format(ex))

            opcionlistar=int(input('Desea realizar otra opcion 1)SI 2)NO: '))
            if opcionlistar == 1:
                menuPrincipal()
            else:
                pass



        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        else:
            print("!Gracias por usar este sistema!")
            exit()


menuPrincipal()