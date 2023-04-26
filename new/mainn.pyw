#Proyecto de Matematicas Discretas
#Participantes: Jose Humberto Venavente y Jose Gregorio Coronel
#Grupo 2
#Universidad del Istmo

from tkinter import *
import tkinter as tk
from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
from tkinter import messagebox
import convertBase
from itertools import product

#Colocamos las caracteristicas del window widget
window = Tk()  # creamos el  window widget
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.maxsize(610, 445)
window.minsize(590, 445)
window.geometry(f"{600}x{950}")




#Agregamos las paginas
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)

for frame in (page1, page2, page3, page4):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ============= Pagina 1 =========================================================================
#Fondo de la pagina inicial
page1.config(background='light cyan')



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
    label_result.config(text=f"El maximo comun divisor es: {resultado}", font=('Arial', 15, 'bold'))

#Se crea la ventana principal 

window.title("Proyecto de Matemática Discreta")



#los botones principales 

k = Label(page1, text='¡Bienvenidos!', font=('Arial', 23, 'bold'), bg='light cyan' )
k.place(x=205, y=85)

dd = Button(page1, text='Maximo Comun Divisor', font=('Arial', 15, 'bold'), command=lambda: show_frame(page2))
dd.place(x=180, y=200)

pp = Button(page1, text='Base Converter', font=('Arial', 15, 'bold'), command=lambda: show_frame(page3))
pp.place(x=210, y=250)

ppp_button3 = Button(page1, text='Mapa de Karnaugh', font=('Arial', 15, 'bold'), command=lambda: show_frame(page4))
ppp_button3.place(x=200, y=300)

k = Label(page1, text='Elige una opcion :]', font=('Corbel', 20), bg='light cyan' )
k.place(x=200, y=140)


# ======================= pagina 2 =====================================================================
# Maximo comun divisor

page2.config(background='light salmon')

pag_label = Label(page2, text='Maximo Comun Divisor', font=('Arial', 23, 'bold'), bg='light salmon')
pag_label.place(x=135, y=390)

#Se crea los widgets necesarios con informacion para el usuario
label_num1 = tk.Label(page2, text="Ingrese el primer numero:", font=('Arial', 16, 'bold'), bg='light salmon')
entry_num1 = tk.Entry(page2)

label_num2 = tk.Label(page2, text="Ingrese el segundo numero:", font=('Arial', 16, 'bold'), bg='light salmon')
entry_num2 = tk.Entry(page2)

button_calculate = tk.Button(page2, text="Calcular", font=('Arial', 14, 'bold'), command=calcularMCD)


label_result = tk.Label(page2, text="", bg='light salmon')




label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
button_calculate.grid(row=2, column=0, columnspan=2)
label_result.grid(row=3, column=0, columnspan=2)
#Coloca los widgets en la ventana


#Se hace el ciclo para iniciar la aplicacion



pg1_button = Button(page2, text='Menu', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
pg1_button.place(x=20, y=400)





# ======== Page 3 ===========================================================================================
# Convertidor de Base

#Se importo CovertBase y procedemos con unas crefinicions de un driopbox y del boton calcular 

bases = [str(i) for i in (2,8,10,16)] #Definimos que las bases solo acepten 2,8,10 y 16
ttk.Style().configure("style1.TCombobox", foreground="blue", background="black")

def createDropBox(textVariable, textToDisplay):
    frame2 = Frame(page3)
    frame2.pack(anchor = "center", pady = 10)
    Label(frame2, text = textToDisplay).pack(side = LEFT)
    baseFrom = ttk.Combobox(frame2,  width = 40, height = 20, textvariable = textVariable, values = bases, style = "style1.TCombobox", font = "ms-sans 15")
    baseFrom.pack(side = RIGHT)
        

def calculate():
    global calculation
    converted = convertBase.convert(number.get(), baseFrom.get(), baseTo.get())
    try:calculation.pack_forget()
    except Exception:pass
    calculation = Label(page3, text = converted, bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
    calculation.pack(anchor = "center", fill = X)
    

baseFrom = StringVar();baseTo = StringVar();number = StringVar()

#Empezamos a crear los espacios para que ingrese el numero

frame1 = Frame(page3)
frame1.pack(anchor = "center", pady = 10)
Label(frame1, text = "Enter number: ").pack(side = LEFT)
Entry(frame1, width = 30, font = "ms-sans 20", insertbackground = "white", bg = "black", fg = "yellow", textvariable = number).pack(side = RIGHT)

def limit(number):
    if len(number.get()) > 0:
        number.set(number.get()[:5])
        
number.trace("w", lambda *args: limit(number))

        
#Labels
createDropBox(baseFrom, "Base From:")
createDropBox(baseTo, "Base To:     ")

#Botones para que pueda irse a otra pagina

pg1_buttonz = Button(page3, text='Menu', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1), bg = "black", fg = "yellow")
pg1_buttonz.place(x=20, y=400)

#Calcular boton con su comando calculate
CalculateButton = Button(page3, text = "calcular", bg = "black", fg = "yellow", font = "ms-sans 30", command = calculate)
CalculateButton.pack(fill = X, anchor = "center")


#Creamos el resultado
calculation = Label(page3, text = "", bg = "royal blue", fg = "white", pady = 57, font = "ms-sans 20")
calculation.pack(anchor = "center", fill = X)



#El titulo
pag2_label = Label(page3, text='Base Converter', font=('Arial', 30, 'bold'))
pag2_label.place(x=150, y=390)








# ========================================= Page 4 =========================================================
# Mapas de Karnaugh

#Solamente agregamos los botones

page4.config(background='light salmon')
pag3_label = Label(page4, text='Mapa de Karnaugh ', font=('Arial', 30, 'bold'), bg= 'light salmon')
pag3_label.place(x=125, y=380)

pg3_button = Button(page4, text='Menu', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
pg3_button.place(x=20, y=400)



# Mapas de Karnaugh: Esta opcion consta de dos partes, dada unafuncion Booleana de 2, 3 o 4 variables 
# (el usuario elige el numero devariables), implemente un programa que satisfaga los siguientesprocedimientos:
# ▪ Mostrar la tabla de verdad y el mapa de Karnaugh de la funcionBooleana.
# ▪ Aplicar la tecnica de los mapas de Karnaugh, para obtenertodas las formas de simplificar la funcion 
# (El programa debemostrar las agrupaciones de los rectangulos que fueronempleados) gggg


#Se crea la clase booleana para las variables
class BooleanFunction:
    def __init__(self, variables, function):
        self.variables = variables
        self.function = function
        
    def evaluate(self, values):
        variables = dict(zip(self.variables, values))
        return eval(self.function, variables)

class Generador:
    def __init__(self, page4):
        self.master = page4
       
        
        #Variables de entrada
        self.var_inputs = tk.StringVar()
        self.var_function = tk.StringVar()
        
        #Se crea y se pide al usuario que ingrese las variables de entrada
        tk.Label(page4, text="Ingrese las variables de entrada").grid(row=0, column=0, sticky="w")
        self.entry_inputs = tk.Entry(page4, textvariable=self.var_inputs)
        self.entry_inputs.grid(row=0, column=1)
        
        #Se crea y se pide al usuario que ingrese la funcion booleana
        tk.Label(page4, text="Ingrese la funcion booleana").grid(row=1, column=0, sticky="w")
        self.entry_function = tk.Entry(page4, textvariable=self.var_function)
        self.entry_function.grid(row=1, column=1)
        
        #Se crea el boton que genera la tabla y el mapa de karnaugh
        tk.Button(page4, text="Crear tabla y mapa", command=self.generate_table_kmap).grid(row=2, column=1)
        
        #Label de la tabla de Verdad
        self.table = tk.LabelFrame(page4, text="Tabla de verdad")
        self.table.grid(row=3, column=0, columnspan=2, pady=10)
        
        #Label del mapa de Karnaugh
        self.kmap = tk.LabelFrame(page4, text="Mapa de Karnaugh")
        self.kmap.grid(row=4, column=0, columnspan=2, pady=10)
        

        #Se define la funcion para generar la tabla de verdad
    def generate_table_kmap(self):

        #Se obtienen las variables booleanas
        inputs = [v.strip() for v in self.var_inputs.get().split(",")]
        function = self.var_function.get()
        
        #Se crea la funcion booleana
        bf = BooleanFunction(inputs, function)
        
        #Se crea la tabla de verdad
        header = [" ".join(inputs) + "  Resultado"]
        table_data = [header]
        for values in product([1, 0], repeat=len(inputs)):
            row_data = ["    ".join(str(v) for v in values)]
            row_data.append(int(bf.evaluate(values)))
            table_data.append(row_data)
        
        #Despliega la tabla de verdad
        for i, row_data in enumerate(table_data):
            for j, cell_data in enumerate(row_data):
                tk.Label(self.table, text=cell_data).grid(row=i, column=j)
        

        #Se crea el mapa de Karnaugh
        kmap_data = {}
        for values in product([1, 0], repeat=len(inputs)):
            index = "".join(str(int(v)) for v in values)
            kmap_data[index] = int(bf.evaluate(values))
        
        #Se despliega el mapa de Karnaugh
        kmap_table = tk.LabelFrame(self.kmap)
        kmap_table.pack()
        for i, row in enumerate(values):
            tk.Label(kmap_table, text=row).grid(row=i+1, column=0, padx=5)
        
        for i, column in enumerate(values):
            tk.Label(kmap_table, text=column).grid(row=0, column=i+1, pady=5)
            for j, value in enumerate([1, 0]):
                index1 = " ".join(str(int(v)) for v in self._get_combination(inputs[0][i], value, inputs))
                index2 = " ".join(str(int(v)) for v in self._get_combination(inputs[0][i], not value, inputs))
                if kmap_data[index1] == 1 or kmap_data[index2] == 1 or kmap_data[index2] == 0 or kmap_data[index2] == 0:
                    text = "1"
                else:
                    text = "0"
                tk.Label(kmap_table, text=text, width=2, height=1, borderwidth=1, relief="solid").grid(row=j+1, column=i+1)
    
    def _get_combination(self, variable, value, inputs):
        combination = []
        for input_var in inputs:
            if input_var == variable:
                combination.append(value)
            else:
                combination.append(None)
        return combination
    
#hacemos que lo muestre el generador en la pagina 4
app = Generador(page4)


window.mainloop()


