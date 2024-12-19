import math

def selector_primos(num_list):
    numprimo=[]

    for num in num_list:

        cousin_num = 1

        if num < 2:
            cousin_num = 0
        else:
            top_num= int(math.sqrt(num))
            for i in range (2, top_num + 1):
                if num % i == 0:
                    cousin_num = 0
                    break
         
        if cousin_num == 1:
            numprimo.append(num)
    return numprimo




num_list = [2, 517, 13, 17, 59]
resultado = selector_primos(num_list)
print(resultado)

            

