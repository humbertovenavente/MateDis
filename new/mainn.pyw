from tkinter import *
import tkinter as tk
from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
from tkinter import messagebox
import convertBase


window = Tk()  # create a window widget
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.maxsize(610, 445)
window.minsize(590, 445)
window.geometry(f"{600}x{950}")
 


page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)

for frame in (page1, page2, page3, page4):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ============= Page 1 =========

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

window.title("Proyecto de Informatica")

k = Label(page1, text='¡Bienvenidos!', font=('Arial', 23, 'bold'), bg='light cyan' )
k.place(x=205, y=85)

pp= Label(page1, text='Username', font=('Arial', 15, 'bold'), bg='light cyan')
pp.place(x=175, y=150)

pp_entry = Entry(page1)
pp_entry.place(x=295, y=155)

pp_label2 = Label(page1, text='Password', font=('Arial', 15, 'bold'), bg='light cyan')
pp_label2.place(x=175, y=200)

pp_entry2 = Entry(page1)
pp_entry2.place(x=295, y=205)

ppp_button3 = Button(page1, text='Ingresar', font=('Arial', 15, 'bold'), command=lambda: show_frame(page2))
ppp_button3.place(x=250, y=250)



#pagina 1

page2.config(background='antique white')

pag_label = Label(page2, text='Maximo Comun Divisor', font=('Arial', 23, 'bold'), bg='antique white')
pag_label.place(x=135, y=390)

#Se crea los widgets necesarios con informacion para el usuario
label_num1 = tk.Label(page2, text="Ingrese el primer numero:", font=('Arial', 16, 'bold'), bg='antique white')
entry_num1 = tk.Entry(page2)

label_num2 = tk.Label(page2, text="Ingrese el segundo numero:", font=('Arial', 16, 'bold'), bg='antique white')
entry_num2 = tk.Entry(page2)

button_calculate = tk.Button(page2, text="Calcular", font=('Arial', 14, 'bold'), command=calcularMCD)


label_result = tk.Label(page2, text="", bg='antique white')




label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
button_calculate.grid(row=2, column=0, columnspan=2)
label_result.grid(row=3, column=0, columnspan=2)
#Coloca los widgets en la ventana


#Se hace el ciclo para iniciar la aplicacion



pg1_button = Button(page2, text='Converter', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg1_button.place(x=20, y=400)

pg1_button3 = Button(page2, text='Mapa', font=('Arial', 13, 'bold'), command=lambda: show_frame(page4))
pg1_button3.place(x=510, y=400) 



# ======== Page 3 ===========


bases = [str(i) for i in (2,8,10,16)]
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

frame1 = Frame(page3)
frame1.pack(anchor = "center", pady = 10)
Label(frame1, text = "Enter number: ").pack(side = LEFT)
Entry(frame1, width = 30, font = "ms-sans 20", insertbackground = "white", bg = "black", fg = "yellow", textvariable = number).pack(side = RIGHT)

def limit(number):
    if len(number.get()) > 0:
        number.set(number.get()[:5])
        
number.trace("w", lambda *args: limit(number))

        

createDropBox(baseFrom, "Base From:")
createDropBox(baseTo, "Base To:     ")

pg2_button = Button(page3, text='Mapa', font=('Arial', 13, 'bold'), command=lambda: show_frame(page4), bg = "black", fg = "yellow")
pg2_button.place(x=510, y=400)
pg1_buttonz = Button(page3, text='MCD', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2), bg = "black", fg = "yellow")
pg1_buttonz.place(x=30, y=400)

CalculateButton = Button(page3, text = "calculate", bg = "black", fg = "yellow", font = "ms-sans 30", command = calculate)
CalculateButton.pack(fill = X, anchor = "center")

calculation = Label(page3, text = "", bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
calculation.pack(anchor = "center", fill = X)




pag2_label = Label(page3, text='Base Converter', font=('Arial', 30, 'bold'))
pag2_label.place(x=150, y=390)








# ======== Page 4 ===========
page4.config(background='gray')
pag3_label = Label(page4, text='Mapa de Karnaugh', font=('Arial', 30, 'bold'))
pag3_label.place(x=50, y=100)

pg3_button = Button(page4, text='Converter', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg3_button.place(x=170, y=200)

pg33button3 = Button(page4, text='MCD', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg33button3.place(x=300, y=200)


window.mainloop()