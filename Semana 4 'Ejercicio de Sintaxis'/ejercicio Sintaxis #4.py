numero_uno=int(input ("Ingrese numero 1: "))
numero_dos=int(input ("Ingrese numero 2: "))
numero_tres=int(input ("Ingrese numero 3: "))
if numero_uno>numero_dos and numero_tres:
    mayor=f"El numero mayor es {numero_uno}"
    print(mayor)
if numero_dos>numero_uno and numero_tres:
    mayor=f"El numero mayor es {numero_dos}"
    print(mayor)
if numero_tres>numero_dos and numero_uno:
    mayor=f"El numero mayor es {numero_dos}"
    print(mayor)