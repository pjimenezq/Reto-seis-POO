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

