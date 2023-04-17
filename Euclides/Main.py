import tkinter as tk
from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
#import Euclides


# Funcion que realiza el calculo con los dos numeros ingresados

def euclides(a, b):
   
    if b == 0:
        return a
    else:
        return euclides(b, a % b)


# Funcion que se ejecuta cuando el boton "Calcular" es presionado
def calcularMCD():
    # Obtener los valores ingresados por el usuario
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Llamar a la funcion para calcular el resultado
    resultado = euclides(num1, num2)

    # Actualizar la etiqueta con el resultado del colculo
    label_resultado.config(text=f"El resultado es: {resultado}")

# Crear la ventana de la interfaz grafica
ventana = tk.Tk()
ventana.title("Calculadora de Maximo Comun Divisor")

# Crear las etiquetas y campos de entrada para los numeros
label1 = tk.Label(ventana, text="Ingrese el primer numero:")
label1.pack()
entry1 = tk.Entry(ventana)
entry1.pack()

label2 = tk.Label(ventana, text="Ingrese el segundo numero:")
label2.pack()
entry2 = tk.Entry(ventana)
entry2.pack()

# Crear el boton para calcular la suma
boton_calcular = tk.Button(ventana, text="Calcular MCD", command=calcularMCD)
boton_calcular.pack()

# Crear la etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Ejecutar el loop principal de la interfaz grafica
ventana.mainloop()