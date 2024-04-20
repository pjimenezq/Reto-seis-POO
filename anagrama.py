# Función que recibe una lista de string y retorna aquellos elementos que tengan los mismos caracteres.

def anagrama(lista):
    listaDos=[] #Luego, se le añade a esta lista los elementos que tienen los mismo caracteres
    x=0 #Se utiliza para acceder al primer string de la lista
    y=0 #Se utiliza para acceder a cada una de las letras del primer string
    z=0 #Se utiliza para acceder a cada una de las palabras de las lista

    while z<len(lista):
        bandera=True
        while y<len(lista[x]):
            if lista[x][y] in lista[z]:#Cuando la letra con la posición y del primer string se encuentra en la palabra con la posición z, se evalua la siguiente letra
                y+=1
            else:
                bandera=False
                z+=1#Se suma una unidad para evaluar la siguiente palabra
                y=0
        if bandera==True:
            listaDos.append(lista[z])#Se añade la palabra con los mismo caracteres a la segunda lista
            y=0
            z+=1

    a=-1 #Se utiliza para acceder a cada una de las palabras de la lista (esperando por el final de la lista de palabras)
    b=0 #Se utiliza para acceder a cada una de las letras de los strings
    c=0 #Se utiliza para acceder al primer string de la lista

    while abs(a)<len(listaDos):
        bandera=True
        while b<len(lista[a]):
            if lista[a][b] in lista[c]:#Cuando la letra con la posición b del último string se encuentra en la primera palabra, se evalua la siguiente letra
                b+=1
            else:
                bandera=False
                listaDos.remove(lista[a])#Si la letra con la posición b del último string no se encuentra en la primera palabra, se quita esa palabra de la lista
                a-=1#Se resta una unidad para evaluar la anterior palabra
                b=0
        if bandera==True:#Si coinciden todas las letras de ambas palabras, la palabra se mantiene en la lista
            b=0
            a-=1#Se resta una unidad para evaluar la anterior palabra

    return listaDos

try:
    resultado=anagrama(["arma","marra","rama","amores"]) #Se llama la función creada anteriormente
    print("De la lista de strings, aquellos elementos que tienen los mismos caracteres son " + str(resultado))
except TypeError as error:#Si uno o más elementos de la lista no son de tipo string, se ejecuta el except TypeError
    print("Error: los elementos de la lista deben ser strings.")