import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Función para conectar a la base de datos MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="260768",  
        database="logistica"
    )

# Función para agregar un nuevo envío
def agregar_envio():
    numero = entrada_numero.get()
    origen = entrada_origen.get()
    destino = entrada_destino.get()
    fecha = entrada_fecha.get()
    estado = entrada_estado.get()

    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Envios (NumeroSeguimiento, Origen, Destino, FechaEntregaPrevista, Estado) VALUES (%s, %s, %s, %s, %s)",
                   (numero, origen, destino, fecha, estado))
    conexion.commit()
    conexion.close()

    messagebox.showinfo("Éxito", "Envío agregado correctamente.")
    mostrar_envios()

# Función para mostrar los envíos en la tabla
def mostrar_envios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Envios")
    registros = cursor.fetchall()
    conexion.close()

    for row in tabla.get_children():
        tabla.delete(row)
    
    for envio in registros:
        tabla.insert("", "end", values=envio)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Envíos")

# Campos de entrada
tk.Label(ventana, text="Número de Seguimiento").grid(row=0, column=0)
entrada_numero = tk.Entry(ventana)
entrada_numero.grid(row=0, column=1)

tk.Label(ventana, text="Origen").grid(row=1, column=0)
entrada_origen = tk.Entry(ventana)
entrada_origen.grid(row=1, column=1)

tk.Label(ventana, text="Destino").grid(row=2, column=0)
entrada_destino = tk.Entry(ventana)
entrada_destino.grid(row=2, column=1)

tk.Label(ventana, text="Fecha de Entrega Prevista").grid(row=3, column=0)
entrada_fecha = tk.Entry(ventana)
entrada_fecha.grid(row=3, column=1)

tk.Label(ventana, text="Estado").grid(row=4, column=0)
entrada_estado = tk.Entry(ventana)
entrada_estado.grid(row=4, column=1)

# Botón para agregar envío
tk.Button(ventana, text="Agregar Envío", command=agregar_envio).grid(row=5, column=0, columnspan=2)

# Crear la tabla para mostrar los envíos
tabla = ttk.Treeview(ventana, columns=("ID", "NumeroSeguimiento", "Origen", "Destino", "FechaEntregaPrevista", "Estado"), show="headings")
tabla.grid(row=6, column=0, columnspan=2)

# Definir los encabezados de la tabla
tabla.heading("ID", text="ID")
tabla.heading("NumeroSeguimiento", text="Número de Seguimiento")
tabla.heading("Origen", text="Origen")
tabla.heading("Destino", text="Destino")
tabla.heading("FechaEntregaPrevista", text="Fecha de Entrega Prevista")
tabla.heading("Estado", text="Estado")

# Mostrar los envíos al iniciar la aplicación
mostrar_envios()

# Ejecutar la aplicación
ventana.mainloop()
