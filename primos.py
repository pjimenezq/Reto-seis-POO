#Función que recibe una lista de números enteros y devuelve solo aquellos que son primos

class ValorInvalidoException(Exception):#Creando excepción personalizda
    def __init__(self, message):
        super().__init__(message)

def primos(lista:int): #El argumento de la función corresponde a la lista de números enteros
    x : int = 2 #Se usa como divisor, para calcular el modulo entre el entero y x
    y : int = 0 #Se usa como la posición de la lista de enteros y permite acceder a cada uno de los números de la lista
    listaPrimos = [] #Posteriormente, se le añaden los números enteros que cumplen con las características de los primos
    
    while y<len(lista): #El ciclo se ejecuta hasta que se evaluen todos los números de la lista
        if lista[y]<=1:#Si algún número de la lista es menor o igual a 1 se levanta la excepción personalizada
            raise ValorInvalidoException("Todos los números de la lista deben ser mayores que 1.")
        if not isinstance(lista[y],(int)):#Si algún número de la lista es flotante, se levanta la excepción TypeError
            raise TypeError
        if x<=(lista[y]**0.5):
            if lista[y]%x==0: #Si el modulo es igual a 0, el número entero sí es primo
                y+=1 #Se suma una unidad, para evaluar si es primo el siguiente número de la lista
                x=2 #x vuelve a su valor original
            else:
                x+=1 #Se le suma una unidad a x y se repite el ciclo
        else:
            listaPrimos.append(lista[y]) #Se añade el número entero y primo a la lista de números primos
            y+=1 #Se suma una unidad, para evaluar si es primo el siguiente número de la lista
            x=2 #x vuelve a su valor original
    return listaPrimos

try:
    resultado = primos([8, 9, 1])
    print("De la lista de números enteros, los números que son primos son: " + str(resultado))
except TypeError as error:#Si uno o más elementos de la lista no son de tipo numérico se ejecuta el except TypeError
    print("Error: los elementos ingresados a la lista deben ser números enteros.")
except ValorInvalidoException as error:
    print("Error:" + str(error))

