import tkinter as tk
from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
from tkinter import messagebox
#import Euclides

# Ejercicio 2: MCD: el usuario debe ingresar dos valores y utilizando el algoritmo deEuclides debe mostrar el maximo comun divisor entre ellos.

#Declaracion de la funcion Euclides para calcular el MCD con este algoritmo
def euclides(a, b):
   
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

#Declaracion de la funcion calcularMCD que hace el calculo de los valores ingresado por el usuario
def calcularMCD():
    
    # Obtiene los valores ingresados por el usuario
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    
    #Esta funcion revisa que los valores ingresados por el usuario en efecto sean numeros
    if not num1.isdigit() or not num2.isdigit():
        messagebox.showerror("Error", "Debe ingresar solo numeros.")
        return
    
    #Con esto convertimos los valores ingresados en enteros
    num1 = int(num1)
    num2 = int(num2)
    
    # Calcula el maximo comun divisor utilizando el algoritmo de Euclides
    resultado = euclides(num1, num2)
    
    #Muestra el resultado en la etiqueta correspondiente
    label_result.config(text=f"El maximo comun divisor es: {resultado}")

#Se crea la ventana principal 
window = tk.Tk()
window.title("Maximo Comun Divisor")

#Se crea los widgets necesarios con informacion para el usuario
label_num1 = tk.Label(window, text="Ingrese el primer numero:")
entry_num1 = tk.Entry(window)
label_num2 = tk.Label(window, text="Ingrese el segundo numero:")
entry_num2 = tk.Entry(window)
button_calculate = tk.Button(window, text="Calcular", command=calcularMCD)
label_result = tk.Label(window, text="")

#Coloca los widgets en la ventana
label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
button_calculate.grid(row=2, column=0, columnspan=2)
label_result.grid(row=3, column=0, columnspan=2)

#Se hace el ciclo para iniciar la aplicacion
window.mainloop()



