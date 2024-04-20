# Reto seis
## Punto uno
Add the required exceptions in the Reto 1 code assigments

**1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.**

**Código**
```
# Función que realiza operaciones básicas entre dos números

class CaracterInvalidoException(Exception):#Creando excepción personalizada
    def __init__(self, message):
        super().__init__(message)

def operaciones(x:float, y:float, operacion:str)->float: #Los argumentos de la función corresponden respectivamente al primer número, el segundo número y el símbolo de la operación
    if operacion=="+":
        return x+y
    elif operacion=="-":
        return x-y
    elif operacion=="*":
        return x*y
    elif operacion=="/":
        if y==0:#Si el denominador es cero se levanta la excepción ZeroDivisionError
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return x/y
    else:#Si el usuario no ingresa la operación adecuada se levanta la excepción personalizada
        raise CaracterInvalidoException("El caracter que corresponde a la operación no es válido.")

try:
    resultado = operaciones(9, 0, "x")
    print(resultado)
except TypeError as error:#Si los operandos no son de tipo numérico se ejecuta el except TypeError
    print(("Error: Se introdujo un valor no númerico para los operandos."))
except ZeroDivisionError as error:
    print("Error:" + str(error))
except CaracterInvalidoException as error:
    print("Error: " + str(error))
```
**Excepciones**

* _CaracterInvalidoException_: Excepción personalizada para cuando el usuario no ingresa un caracter válido como operación.
* _ZeroDivisionError_: Excepción si el denominador de la división es cero.
* _TypeError_: Excepción si los operandos no son de tipo numérico.

**2. Realice una función que permita validar si una palabra es un palíndromo.**

**Código**
```
#Función que permite validar si una palabra es un palíndromo

def palindromo(palabra:str): #El argumento de la función corresponde a la palabra que se quiere validar como palíndromo
    x: int = 0 #Se usa para obtener la primera letra de la palabra
    y: int = -1 #Se usa para obtener la última letra de la palabra
    palindromo:bool = True
    while x<len(palabra) and palindromo==True:
        if palabra[x]==palabra[y]:
            x+=1 #Se aumenta el valor, para obtener la siguiente letra
            y-=1 #Se disminuye el valor, para obtener la letra anterior
        else:
            palindromo = False #Cuando las letras no son iguales, la palabra no es palíndromo
            return("La palabra '" + palabra +"' no es un palíndromo.")
    
    if palindromo==True: #Cuando se acaba el ciclo while y siempre coincidieron las letras, la palabra es palíndromo
        return("La palabra '" + palabra +"' sí es un palíndromo.")

try:
    palabra=10101
    resultado = palindromo(palabra)
    print(resultado)
except TypeError as error:#Si la palabra no es un string se ejecuta el except TypeError
    print("Error: la palabra debe ser un string.")
```
**Excepciones**

* _TypeError_: Excepción si la palabra ingresada no es un string.
  
**3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos.**

**Código**
```
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
```
**Excepciones**

* _ValorInvalidoException_: Excepción personalizada para cuando el usuario ingresa uno o más números que son menores o iguales a 1.
* _TypeError_: Excepción si los elementos ingresados en la lista no son números enteros.

**4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.**

**Código**
```
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

```
**Excepciones**

* _TypeError_: Excepción cuando uno o más elementos de la lista no son números enteros (si estos son strings o flotantes).

**5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.**

**Código**
```
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
```
**Excepciones**

* _TypeError_: Excepción si algún elemento de la lista no es de tipo string.
  
## Punto dos
In the package Shape identify at least 3 cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.
