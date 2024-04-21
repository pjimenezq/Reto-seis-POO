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
        