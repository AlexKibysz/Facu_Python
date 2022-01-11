from BasicosAED import *

# Cargar un vector con valores ingresados desde teclado
# Parámetros (datos): un vector
# Retorno (resultados): None
def cargarVector(vec):
    for i in range(len(vec)):
        vec[i] = int(input('Ingrese valor: '))

# Sumatoria de todos los números
# Parámetros (datos): un vector
# Retorno (resultados): el valor de la suma de todos los valores contenidos del vector
def suma(v):
    sum = 0
    for i in range(len(v)):
       sum += v[i]
    return sum

# Cantidad de números pares
# Parámetros (datos): un vector
# Retorno (resultados): cantidad de valores en el vector que son pares
def cantidadPares(v):
    cant = 0
    for i in range(len(v)):
       if v[i] % 2 == 0:
           cant += 1
    return cant

# Suma los valores ubicados en un índice Impar
# Parámetros (datos): un vector
# Retorno (resultados): el valor de la suma
def sumaIndiceImpar(v):
    sum = 0
    for i in range(1, len(v), 2):
        sum += v[i]
    return sum

def mostrarVector(vec):
    print('Contenido del Vector')
    for i in range(len(vec)):
        print('Indice ', i , ': ', vec[i])


def test():
    tam = int(input('Ingrese la cantidad de valores: '))
    vec = tam * [0]

    # Cargar los datos en el vector
    cargarVector(vec)

    # Mostrar los valores almacenados en el vector
    mostrarVector(vec)

    # PUNTO 1
    # Sumatoria de los números
    s = suma(vec)
    print('1- Suma de números: ', s)

    # PUNTO 2
    # Promedio de todos los números.
    prom = promedio(s, len(vec))
    print('2- Promedio: ', prom)

    # PUNTO 3
    # Cantidad de números Pares.
    cant = cantidadPares(vec)
    print('3- Cantidad  de números pares: ', cant)

    # PUNTO 4
    # Porcentaje de números pares
    porc = porcentaje(len(vec), cant)
    print('4- Porcentaje de números pares: ', porc, ' %')

    # PUNTO 5
    # Suma de los elementos ubicados en índice impar.
    sum = sumaIndiceImpar(vec)
    print('5- Suma de los valores ubicados en un indice impar: ', sum)

if __name__ == '__main__':
    test()




