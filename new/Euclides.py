#Proyecto de Matematicas Discretas
#Participantes: Jose Humberto Venavente y Jose Gregorio Coronel
#Grupo 2
#Universidad del Istmo

def euclides(a, b):
    """
    Implementación del algoritmo de Euclides para encontrar el máximo común divisor
    entre dos números.
    """
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

# Pedir al usuario que ingrese dos valores
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

# Calcular el máximo común divisor utilizando el algoritmo de Euclides
mcd = euclides(a, b)

# Mostrar el resultado
print("El máximo común divisor de", a, "y", b, "es", mcd)