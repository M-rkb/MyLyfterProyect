nombre = str(input("Ingrese su nombre: ")) 
apellido = str(input("Ingrese su apellido: ")) 
edad = int(input("Ingrese su su edad: "))
if (0 < edad <= 2):
    print (f'{nombre} {apellido} es un bebe')
elif (3 <= edad <= 11):
    print (f'{nombre} {apellido} es un nino')
elif (12 <= edad <= 14):
     print (f'{nombre} {apellido} es un preadolescente')
elif (15 <= edad <= 17):
    print (f'{nombre} {apellido} es un adolescente')
elif (18 <= edad <= 22):
     print (f'{nombre} {apellido} es un adulto Joven')
elif (23 <= edad <= 65):
    print (f'{nombre} {apellido} es un adulto ')
elif (66 <= edad <= 120):
    print (f'{nombre} {apellido} es un adulto mayor ')
else:
    print("Ingrese una edad valida") 

