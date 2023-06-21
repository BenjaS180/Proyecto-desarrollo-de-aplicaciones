import tkinter as tk
from datetime import datetime
def mostrar_bodega():
    pass
    # Aquí iría tu implementación para mostrar los datos de la bodega en la interfaz

def mostrar_producto():
    pass
    # Aquí iría tu implementación para mostrar los datos del producto en la interfaz

def ingresar_datos_bodega():
    pass
    # Aquí iría tu implementación para ingresar datos de la bodega desde la interfaz

def ingresar_datos_producto():
    pass
    # Aquí iría tu implementación para ingresar datos del producto desde la interfaz

def solicitar_datos_actualizacion_bodega():
    pass
# Aquí iría tu implementación para solicitar datos de actualización de la bodega desde la interfaz

def solicitar_datos_actualizacion_producto():
    pass
    # Aquí iría tu implementación para solicitar datos de actualización del producto desde la interfaz

def eliminar_bodega():
    pass
    # Aquí iría tu implementación para eliminar una bodega desde la interfaz

def menuPrincipal():
    ventana = tk.Tk()
    ventana.title("Programa de Gestión")
    ventana.geometry("400x300")

    def listar_opcion():
        opcion_listar_bodegas = opcion_listar.get()
        if opcion_listar_bodegas == 1:
            mostrar_bodega()
        elif opcion_listar_bodegas == 2:
            mostrar_producto()

    def registrar_opcion():
        opcion_registrar = opcion_registrar.get()
        if opcion_registrar == 1:
            ingresar_datos_bodega()
        elif opcion_registrar == 2:
            ingresar_datos_producto()

    def actualizar_opcion():
        opcion_actualizar = opcion_actualizar.get()
        if opcion_actualizar == 1:
            solicitar_datos_actualizacion_bodega()
        elif opcion_actualizar == 2:
            solicitar_datos_actualizacion_producto()

    def eliminar_opcion():
        opcion_eliminar = opcion_eliminar.get()
        if opcion_eliminar == 1:
            eliminar_bodega()

    opcion_listar = tk.IntVar()
    opcion_registrar = tk.IntVar()
    opcion_actualizar = tk.IntVar()
    opcion_eliminar = tk.IntVar()

    label_menu = tk.Label(ventana, text="MENU PRINCIPAL", font=("Arial", 16))
    label_menu.pack(pady=10)

    # Opciones de listar
    label_listar = tk.Label(ventana, text="Listar:")
    label_listar.pack(anchor=tk.W)

    radio_bodegas = tk.Radiobutton(ventana, text="Bodegas", variable=opcion_listar, value=1)
    radio_bodegas.pack(anchor=tk.W)

    radio_productos = tk.Radiobutton(ventana, text="Productos", variable=opcion_listar, value=2)
    radio_productos.pack(anchor=tk.W)

    btn_listar = tk.Button(ventana, text="Mostrar", command=listar_opcion)
    btn_listar.pack(pady=5)

    # Opciones de registrar
    label_registrar = tk.Label(ventana, text="Registrar:")
    label_registrar.pack(anchor=tk.W)

    radio_bodegas_reg = tk.Radiobutton(ventana, text="Bodegas", variable=opcion_registrar, value=1)
    radio_bodegas_reg.pack(anchor=tk.W)

    radio_productos_reg = tk.Radiobutton(ventana, text="Productos", variable=opcion_registrar, value=2)
    radio_productos_reg.pack(anchor=tk.W)

    btn_registrar = tk.Button(ventana, text="Registrar", command=registrar_opcion)
    btn_registrar.pack(pady=5)

    # Opciones de actualizar
    label_actualizar = tk.Label(ventana, text="Actualizar:")
    label_actualizar.pack(anchor=tk.W)

    radio_bodegas_act = tk.Radiobutton(ventana, text="Bodegas", variable=opcion_actualizar, value=1)
    radio_bodegas_act.pack(anchor=tk.W)

    radio_productos_act = tk.Radiobutton(ventana, text="Productos", variable=opcion_actualizar, value=2)
    radio_productos_act.pack(anchor=tk.W)

    btn_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_opcion)
    btn_actualizar.pack(pady=5)

    # Opciones de eliminar
    label_eliminar = tk.Label(ventana, text="Eliminar:")
    label_eliminar.pack(anchor=tk.W)

    radio_bodegas_del = tk.Radiobutton(ventana, text="Bodegas", variable=opcion_eliminar, value=1)
    radio_bodegas_del.pack(anchor=tk.W)

    radio_productos_del = tk.Radiobutton(ventana, text="Productos", variable=opcion_eliminar, value=2)
    radio_productos_del.pack(anchor=tk.W)

    btn_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_opcion)
    btn_eliminar.pack(pady=5)

    ventana.mainloop()

menuPrincipal()
menuPrincipal()