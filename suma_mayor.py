# Función que recibe una lista de números enteros y retorna la mayor suma entre dos elementos consecutivos

def sumaMayor(lista:int): #El argumento de la función corresponde a la lista de números enteros
    listaSumatorias = [] #Luego, a esta lista se le añaden todas las sumatorias entre los elementos consecutivos
    x : int = 0 #Se usa para acceder a los números de la lista, según su posición
    y : int = 1 #Se usa para acceder al número consecutivo de x en la lista 

    while y<len(lista):
        if not isinstance(lista[x],int) or not isinstance(lista[y],int): #Si los elementos de las lista no son enteros se levanta la excepción TypeError
            raise TypeError
        listaSumatorias.append(lista[x]+lista[y]) #Se le agrega a la lista la suma entre los números consecutivos
        x+=1#Se suma una unidad para acceder al siguiente elemento
        y+=1#Se suma una unidad para acceder al siguiente elemento
    return max(listaSumatorias) #La función retorna la suma con el valor mayor

try:
    resultado=sumaMayor([9, 1, -3, 12,-1.2]) #Se llama la función creada anteriormente
    print("De la lista de números enteros, la mayor suma entre dos elementos consecutivos es " + str(resultado))
except TypeError as error:#Si uno o más elementos de la lista no son de tipo numérico se ejecuta el except TypeError
    print("Error: los elementos ingresados a la lista deben ser números enteros.")

