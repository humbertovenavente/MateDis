#Proyecto de Matematicas Discretas
#Participantes: Jose Humberto Venavente y Jose Gregorio Coronel
#Grupo 2
#Universidad del Istmo

#CONVERTIMOS QUE SOLO ACEPTE DIGITOS DEL 0 AL 9 Y A AL F
correspondenceString = r"""0123456789ABCDEFabcdef/-"""

#pRIMERA DEFINICI´NO DE PASAR LAS BASES
def convert(number = '10', baseFrom = 10, baseTo = 10):
    check = checks(number, baseFrom, baseTo)
    if not check.accepted:return check.message
    convertedToBase10 = convertToBase10(number, baseFrom)
    return convertToBase(convertedToBase10, baseTo)

#cODIGO QUE AYUO A PASAR A BASE 10
#la funcion tiene como parametros number que el valor por defecto es 10, y cualuqier numero en string representa el numero que se uqiera convertir en base 10
#el chartonumc... mapea el correspndenceString

#el converterdBase10 se inicializa en cero y se utiliza para ir acumujlando el valor de la conversión a base 10
def convertToBase10(number = "10", baseFrom = 10, correspondenceString = correspondenceString):
    baseFrom = int(baseFrom)
    charToNumCorrespondence = {j:i for i, j in enumerate(correspondenceString)}
    convertedBase10 = 0

    for num, char in enumerate(reversed(str(number))):
        convertedBase10 += int(charToNumCorrespondence[char]) * (baseFrom ** num)
    
    return convertedBase10


#cODIGO EXTERNO 
def convertToBase(number = "10", baseTo = 10, correspondenceString = correspondenceString):
    baseTo = int(baseTo)
    numToCharCorrespondence = {i:j for i, j in enumerate(correspondenceString)}
    convertedNum = ""

    while number != 0:
        remainder = number % baseTo
        corresponding = numToCharCorrespondence[remainder]
        convertedNum += str(corresponding)
        number //= baseTo

    return convertedNum[::-1]

#dEFINICION QUE AYUDO A PODER IDENTIFICAR SI LA BASE ES VALIDA O NO, SE SOPORTA O NO
def checks(number, baseFrom, baseTo, correspondenceString = correspondenceString):
    try:
        baseTo = int(baseTo);baseFrom = int(baseFrom)
    except Exception:return checkMessage(False, "base invalida")
    
    if baseTo < 1 or baseFrom < 1:return checkMessage(False, "Base debe de ser mayor a 0")
    if baseTo > len(correspondenceString):return checkMessage(False, "Base not supported")
    for i in str(number):
        if i not in correspondenceString:return checkMessage(False, "Caracter Invalido")
    
    return checkMessage(True, "Aceptado")
    
#Se crea una clase aceptando mensaje
#accepted es un bolleano si se acepta o no el mensaje
#usamos init para inizializar los atributos de instancia de los argumentos acepted y messaged
class checkMessage:
    def __init__(self, accepted, message):
        self.accepted, self.message = accepted, message