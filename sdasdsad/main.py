import math


def primo_mostrar(x):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    if x == 2:
        print('es el numero 2 no es primo')
    elif x % 2 == 0:
        print('el resto es 0 del numero dividido 2')
    else:
        raiz = int(math.sqrt(x))
        for i in primos:
            resto = x % i
            if resto == 0:
                print('No es primo')
                print(f'{x}mod{i}={resto}')
            elif raiz<i:
                break


x = int(input('ingrese un numero'))
primo_mostrar(x)