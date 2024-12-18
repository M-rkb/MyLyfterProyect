num_uno=0
num_dos=0

def sumar (num_uno, num_dos):
    return num_uno+ num_dos
 


def restar (num_uno, num_dos):
    return num_uno - num_dos
 

def multiplicar (num_uno, num_dos):
    return num_uno * num_dos
     


def dividir (num_uno, num_dos):
    if num_dos == 0:
        raise ValueError("No se puede dividir por 0")
    return num_uno/num_dos

aritmetica = {'+': sumar, '-': restar, '*': multiplicar, '/': dividir}

again = "Y"

try:
    num_uno = input("Ingrese el numero uno: ")
    if num_uno.isdigit():
          num_uno= int(num_uno) 
    else:  
        raise ValueError("Ingrese un numero valido!")
except ValueError as error:
    print(error)
    exit()  

while again.upper() == "Y":

    operacion = input("Ingrese la operación (+, -, *, /): ")

    try:
        operacion_funcion = aritmetica[operacion]
    except KeyError:
        print("Operación no válida. Ingrese +, -, * o /.")
        continue     

    try:
        num_dos = input("Ingrese el numero dos: ")
        if num_dos.isdigit():
          num_dos= int(num_dos) 
        else:  
            raise ValueError("Ingrese un numero valido!")
    except ValueError as error:
        print(error)
        continue   

    resultado = operacion_funcion(num_uno, num_dos)
    print(f"El resultado de {num_uno} {operacion} {num_dos} es: {resultado}")
    
    num_uno = resultado

    again = input ("Desea realizar otro ejercicio con el resultado? (Y/N):")

print("Fin")

