import pandas as pd
import os
from tkinter import Tk, messagebox

def convertir_excel_a_csv():
    # Ruta del archivo Excel independiente de s. operativo.
    ruta_excel = os.path.join("assets", "archivos excel", "Tienda Electronica.xlsx") #3° modificable
    
    # Verifica si el archivo Excel existe
    if not os.path.exists(ruta_excel):
        print(f"El archivo {ruta_excel} no existe.")
        return
    
    # Lee archivo indicado lo se convierte en DataFrame(estructura tabular en pandas)
    datos = pd.read_excel(ruta_excel)
    
    # Ruta destino del archivo CSV
    ruta_csv = os.path.join("assets", "archivos csv", "Tienda_Electronica.csv") #3° modificable
    
    # Guardar datos en formato CSV
    datos.to_csv(ruta_csv, index=False, encoding='latin1') #opciones encoding: utf-8, ISO-8859-1
    
    # Eliminar filas completamente vacías y filas con espacios en blanco
    datos = datos.dropna(how='all')  # Elimina filas vacías. Por defecto 'axis=0'
    
    # Eliminar columnas completamente vacías
    datos = datos.dropna(axis=1, how='all')

    # Guardar como CSV
    datos.to_csv(ruta_csv, index=False, encoding='latin1')

    # Mostrar alerta de éxito
    mostrar_alerta_exito(ruta_csv)

def mostrar_alerta_exito(ruta_csv):
    # Crear ventana emergente usando tkinter
    ventana = Tk()
    ventana.withdraw()  # Oculta la ventana principal de tkinter
    mensaje = f"Conversión exitosa.\nArchivo guardado en:\n{ruta_csv}"
    messagebox.showinfo("Éxito", mensaje)
    ventana.destroy()  # Cierra la ventana emergente

# Llama a la función
convertir_excel_a_csv()
