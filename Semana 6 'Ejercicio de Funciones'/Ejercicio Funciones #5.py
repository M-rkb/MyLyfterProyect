def counter_cases():
    my_string = 'hola amigoS' 
    upper_w = 0
    lower_w = 0
    space = 0

    for word in my_string:
        if word.isupper():
            upper_w += 1
        elif word.isspace():  
            space += 1
        else:
            lower_w += 1
    print(f'En esta cadena hay {upper_w} en mayusculas y {lower_w} minusculas')

print(counter_cases())

