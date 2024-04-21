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

**Código**
```
import math #importando math 

ARCOCOSENO = math.acos #Declarando arcocoseno como una constante
GRADOS = math.degrees #Declarando la conversión de radianes a grados como una constante

class Point:
    def __init__(self, x:float, y:float):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError("Las coordenadas de los puntos deben ser de tipo float·")
        #Si alguna de las coordenadas de un punto no es de tipo numérico, se levanta una excepción TypeError.
        self.__x = x
        self.__y = y

    # Setter x
    def set_x(self, new_x):
        self.__x = new_x

    # Getter x
    def get_x(self):
        return self.__x

    # Setter y
    def set_y(self, new_y):
        self.__y = new_y

    # Getter y
    def get_y(self):
        return self.__y
    
    def compute_distance(self, Point):
        return ((self.__x-Point.__x)**2+(self.__y-Point.__y)**2)**0.5 #Formula para calcular distancia entre dos puntos
    
class Line:
    def __init__(self, start_point:Point, end_point:Point): #Hay composición: una línea tiene dos puntos
        if start_point.get_x()==end_point.get_x() and start_point.get_y()==end_point.get_y():
            raise ValueError("Una línea no puede comenzar y terminar en el mismo punto.")
        #En caso de que el punto de inicio y el punto final de una línea sean iguales, se levanta una excepción ValueError.
        self.__start_point = start_point
        self.__end_point = end_point
        self.__length = start_point.compute_distance(end_point) #Length se cálcula con el método compute_distance de la clase Point

    # Setter start point
    def set_start_point(self, new_start_point):
        self.__start_point = new_start_point

    # Getter start point
    def get_start_point(self):
        return self.__start_point
    
    # Setter end point
    def set_end_point(self, new_end_point):
        self.__end_point = new_end_point

    # Getter end point
    def get_end_point(self):
        return self.__end_point
    
    # Setter length
    def set_length(self, new_length):
        self.__length = new_length

    # Getter length
    def get_length(self):
        return self.__length
    
class Shape: #Clase base
    def __init__(self, is_regular:bool, vertices:list=[Point], edges:list=[Line]):
        if not isinstance(is_regular, (bool)):
            raise TypeError("El dato de la variable is_regular debe ser de tipo booleano. ")
        #Si el dato de is_regular no es de tipo bool, se levanta una excepción TypeError.
        if len(vertices)!=len(edges):
            raise ValueError("El polígono debe tener el mismo número de lados y de vértices.")
        #Si la cantidad de vertices y de lados de la figura no son iguales, se levanta una excepción ValueError
        self.__is_regular = is_regular 
        self.__vertices = vertices
        self.__edges = edges
        
    # Setter is regular
    def set_is_regular(self, new_is_regular):
        self.__is_regular = new_is_regular

    # Getter is regular
    def get_is_regular(self):
        return self.__is_regular
    
    # Setter vertices
    def set_vertices(self, new_vertices):
        self.__vertices = new_vertices

    # Getter vertices
    def get_vertices(self):
        return self.__vertices
    
    # Setter edges
    def set_edges(self, new_edges):
        self.__edges = new_edges

    # Getter edges
    def get_edges(self):
        return self.__edges
    
    def compute_area(self): #Se define el método para calcular área
        pass

    def compute_perimeter(self): #Se define el método para calcular perímetro
        pass
    
    def compute_inner_angles(self): #Se define el método para calcular ángulos internos
        pass

class Triangle(Shape): #Subclase
    def __init__(self, is_regular:bool, vertices:list=[Point], edges:list=[Line]):
        super().__init__(is_regular, vertices, edges) #Llamando atributos y métodos de la clase base
    
    def compute_area(self):#Polimorfismo
        #Para calcular el área de los triangulos se usa la fórmula de Herón
        #Formula de Herón:(s(s-a)(s-b)(s-c))**0.5, donde s=(a+b+c)/2
        x = 0
        sum = 0 #suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        s = sum/2 #Se calcula s 
        area = (s*(s-self.get_edges()[0].get_length())*(s-self.get_edges()[1].get_length())*(s-self.get_edges()[2].get_length()))**0.5
        #Se usa la formula de Herón
        return area

    def compute_perimeter(self):#Polimorfismo
        x = 0
        sum = 0 #suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        return sum

    def compute_inner_angles(self):#Polimorfismo
        #Para calcular los ángulos se usa la ley del coseno
        #a,b y c corresponden a cada uno de los lados del triángulo
        a = self.get_edges()[0].get_length()
        b = self.get_edges()[1].get_length()
        c = self.get_edges()[2].get_length()
        #Se obtiene cada uno de los ángulos con teniendo en cuenta la fórmula: a^2=b^2+c^2-2bc*cosA
        angle_a = (GRADOS(ARCOCOSENO((a**2-b**2-c**2)/(-2*b*c))))
        angle_b = (GRADOS(ARCOCOSENO((b**2-a**2-c**2)/(-2*a*c))))
        angle_c = (GRADOS(ARCOCOSENO((c**2-b**2-a**2)/(-2*a*b))))
        return [angle_a, angle_b, angle_c]

class Isosceles(Triangle):#Subclase
    def __init__(self, is_regular: bool, vertices: list = [Point], edges: list = [Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

class Equilateral(Triangle):#Subclase
    def __init__(self, is_regular: bool, vertices: list = [Point], edges: list = [Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

    def compute_perimeter(self):#Polimorfismo
        if self.get_is_regular()==True:
            return self.get_edges()[0].get_length()*3#El perimetro de un triángulo equilatero es cualquier lado multiplicado por 3
        else:
            return "The triangle should be regular."
        
    def compute_inner_angles(self):#Poliformismmo
        if self.get_is_regular()==True:#Todos los ángulos de un triángulo equilatero miden 60 grados
            return [60, 60, 60]
        else:
            return "The triangle should be regular."

class Scalene(Triangle):#Subclase
    def __init__(self, is_regular: bool, vertices: list = [Point], edges: list = [Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

class Rectangle(Shape):#Subclase
    def __init__(self, is_regular:bool, vertices:list=[Point], edges:list=[Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

    def compute_area(self):#Polimorfismo
        #Se obtienen las coordenadas del último punto de la primera línea dada
        vertice_x = self.get_edges()[0].get_end_point().get_x()
        vertice_y = self.get_edges()[0].get_end_point().get_y()
        x = 0
        while x<len(self.get_edges()):
            #Se busca la línea que tiene como primer punto las mismas coordenadas que el último punto de la primera linea dada
            #Lo anterior se hace para asegurarse de que se multipliquen la base y la altura del rectángulo y no los lados paralelos
            if self.get_edges()[x].get_start_point().get_x()==vertice_x and self.get_edges()[x].get_start_point().get_y()==vertice_y:
                area = self.get_edges()[0].get_length()*self.get_edges()[x].get_length() #Se multiplican la base y la altura del rectángulo
                return area
            else:
                x+=1

    def compute_perimeter(self):#Polimorfismo
        x = 0
        sum = 0#suma de la longitud de todos los lados del triángulo
        while x<len(self.get_edges()):
            sum+=self.get_edges()[x].get_length()
            x+=1
        return sum
    
    def compute_inner_angles(self):#Polimorfismo
        return [90, 90, 90, 90]#Todos los ángulos de un rectángulo miden 90 grados
    
class Square(Rectangle):#Subclase
    def __init__(self, is_regular:bool, vertices:list=[Point], edges:list=[Line]):
        super().__init__(is_regular, vertices, edges)#Llamando atributos y métodos de la clase base

    def compute_area(self):#Polimorfismo
        if self.get_is_regular()==True:
            return self.get_edges()[0].get_length()**2#El área de un cuadrado es la longitud de cualquier elevado al cuadrado
        else:
            return "The square should be regular."
    
    def compute_perimeter(self):#Polimorfismo
        if self.get_is_regular()==True:
            return self.get_edges()[0].get_length()*4#El perimetro de un cuadrado es la longitud de cualquier lado multiplicado por 4
        else:
            return "The square should be regular."
```
**Excepciones**
1. Se levanta una excepción _TypeError_ cuando el usuario ingresa como coordenadas de un punto datos que no son float ni int.
2. En caso de que el punto de inicio y el punto final de la clase Line sean los mismos, se levanta una excepción _ValueError_ debido a que una línea no puede comenzar y terminar en el mismo punto.
3. Para el atributo de la clase Shape que se llama is_regular, se levanta una excepción _TypeError_ en caso de que se le ingrese un valor que no sea de tipo bool.
4. Si la cantidad de vertices y de lados en una figura es distinta, se levanta una excepción _ValueError_, teniendo en cuenta que cualquier polígono debe tener el mismo número de lados y de vértices.
