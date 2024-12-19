
all_numbers = []
for i in range(10):
    numero = int(input(f'Ingrese el número {i + 1}: '))  
    all_numbers.append(numero) 
print("Los números ingresados son:", all_numbers)
numero_mayor = all_numbers[0] 
for numero in all_numbers:
    if numero > numero_mayor:
        numero_mayor = numero 
print("El número mayor es:", numero_mayor)