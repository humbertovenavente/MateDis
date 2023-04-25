import tkinter as tk
from itertools import product

# Mapas de Karnaugh: Esta opcion consta de dos partes, dada unafuncion Booleana de 2, 3 o 4 variables 
# (el usuario elige el numero devariables), implemente un programa que satisfaga los siguientesprocedimientos:
# ▪ Mostrar la tabla de verdad y el mapa de Karnaugh de la funcionBooleana.
# ▪ Aplicar la tecnica de los mapas de Karnaugh, para obtenertodas las formas de simplificar la funcion 
# (El programa debemostrar las agrupaciones de los rectangulos que fueronempleados)


#Se crea la clase booleana para las variables
class BooleanFunction:
    def __init__(self, variables, function):
        self.variables = variables
        self.function = function
        
    def evaluate(self, values):
        variables = dict(zip(self.variables, values))
        return eval(self.function, variables)

class Generador:
    def __init__(self, master):
        self.master = master
        master.title("Tabla de verdad y Mapa de Karnaugh")
        
        #Variables de entrada
        self.var_inputs = tk.StringVar()
        self.var_function = tk.StringVar()
        
        #Se crea y se pide al usuario que ingrese las variables de entrada
        tk.Label(master, text="Ingrese las variables de entrada").grid(row=0, column=0, sticky="w")
        self.entry_inputs = tk.Entry(master, textvariable=self.var_inputs)
        self.entry_inputs.grid(row=0, column=1)
        
        #Se crea y se pide al usuario que ingrese la funcion booleana
        tk.Label(master, text="Ingrese la funcion booleana").grid(row=1, column=0, sticky="w")
        self.entry_function = tk.Entry(master, textvariable=self.var_function)
        self.entry_function.grid(row=1, column=1)
        
        #Se crea el boton que genera la tabla y el mapa de karnaugh
        tk.Button(master, text="Crear tabla y mapa", command=self.generate_table_kmap).grid(row=2, column=1)
        
        #Label de la tabla de Verdad
        self.table = tk.LabelFrame(master, text="Tabla de verdad")
        self.table.grid(row=3, column=0, columnspan=2, pady=10)
        
        #Label del mapa de Karnaugh
        self.kmap = tk.LabelFrame(master, text="Mapa de Karnaugh")
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
    
root = tk.Tk()
app = Generador(root)
root.mainloop()
