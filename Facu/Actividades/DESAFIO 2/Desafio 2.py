'''En este Desafio 02 se propone el desarrollo y prueba de un programa que
implemente el cálculo de los valores de la conocida Sucesión 3n + 1 o Sucesión de Collatz.
Se parte de un número entero positivo n y se aplica en forma sucesiva la siguiente relación numérica
hasta llegar eventualmente al valor 1:
Por ejemplo, si partimos de n = 13 y aplicamos la relación sucesivamente sobre el último valor calculado, se genera la
siguiente secuencia hasta que finalmente se llega al 1: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. El conjunto de valores así
obtenidos, se suele designar como la órbita de n, y el número de iteraciones (que es el tamaño del conjunto de valores
obtenidos) hasta alcanzar el 1 partiendo desde n, se suele conocer como la longitud de la órbita de n o también como el
tiempo total de parada de n (o el total stopping time de n).

Su tarea es desarrollar un programa que permita cargar por teclado el valor de n, y luego calcule y
    muestre todos los valores de la órbita de n,
mostrando también (al final)
    el valor de la longitud de la órbita de n,
    el promedio entre todos los valores de esa órbita,
    y el valor que haya sido el mayor de todos en la órbita. Por ejemplo, si se carga n = 13,
 la salida del programa debería ser la siguiente:

 n = 13

Orbita de n = 13 (valores calculados incluyendo al 13 y al 1): [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): 10

Promedio de todos los valores de la órbita:  11.9

Mayor de los números en esa órbita:  40
 '''
def sequencia_collatz(x):
    cant_elementos = 0
    secuencia = [x]
    cant_elementos+=1
    if x < 1:
       return []
    while x > 1:
       cant_elementos+=1
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       secuencia.append(x)
    mayor=max(secuencia)
    promedio=round(sum(secuencia)/len(secuencia),2)
    print('orbita, cant elementos, promedio, mayor en la lista')
    return secuencia, cant_elementos, promedio, mayor
print('ingrese numero!')
numero=int(input())
f=sequencia_collatz(numero)
print(f)
