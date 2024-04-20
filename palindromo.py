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


