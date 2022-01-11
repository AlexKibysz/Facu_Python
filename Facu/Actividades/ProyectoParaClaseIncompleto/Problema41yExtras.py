
# CASO DE ESTUDIO:

# Desarrollar un programa que permita cargar por teclado un arreglo de números enteros de n componentes,
# y permita determinar lo siguiente:
#
# 1- Cargar los datos del vector desde teclado, validando que los valores ingresados
#  estén comprendidos entre 0 y 15 (ambos incluidos).
#
# 2- Indicar con un mensaje si los datos del vector se encuentran ordenados.
#
# 3- Indicar si existe en el vector el número x, siendo x un valor ingresado desde teclado.
#
# 4- Ordenar el vector en forma ascendente (menor a mayor).
#
# 5- Determinar la cantidad de veces que se repite el valor x, siendo x ingresado desde teclado.
#
# 6- Mostrar por pantalla los valores del vector que se encuentren ubicados en un índice impar.

# 7 – Indicar si los componentes del vector se encuentran en secuencia de k en k,
#    siendo k un número que se ingresa también por teclado


def validar_mayor_que(mensaje, valor):
    tam = int(input(mensaje))
    while tam <= valor:
        print('ERROR')
        tam = int(input(mensaje))
    return tam


# 1- Cargar los datos del vector desde teclado, validando que los valores ingresados
#  estén comprendidos entre 0 y 15 (ambos incluidos).

def validar_entre(mensaje, inf, sup):
    pass


def cargar(vec):
    n = len(vec)
    print('Cargue ahora los datos de este arreglo...')
    for i in range(n):
        vec[i] = validar_entre('Ingrese valor entre 0 y 15: ', 0, 15)

# 2- Indicar con un mensaje si los datos del vector se encuentran ordenados.
def enOrdenAscendente(vec):
    ban = True
    # COMPLETAR
    return ban

# 3- Indicar si existe en el vector el número x, siendo x un valor ingresado desde teclado.
def existe(vec, x):
    pass

# 4- Ordenar el vector en forma ascendente (menor a mayor).
def ordenarMenorMayor(vec):
    pass

# 5- Determinar la cantidad de veces que se repite el valor x, siendo x ingresado desde teclado.
def determinarCantidad(vec, x):
    pass

# 6- Mostrar por pantalla los valores del vector que se encuentren ubicados en un índice impar.
def mostrarValoresIndiceImpar(vec):
    for i in range(len(vec)):
        print('Indice [', i, '] : ', vec[i])

# 7 – Indicar si los componentes del vector se encuentran en secuencia de k en k,
# siendo k un número que se ingresa también por teclado
def enSecuencia(vec, k):
    n = len(vec)
    for i in range(1, n):
        if vec[i] != vec[i-1] + k:
            return False
    return True


def test():
    vec = []
    op = 0
    while op != 4:
        print('*' * 60)
        print('MENU DE OPCIONES')
        print('*' * 60)
        print('1- Cargar números')
        print('2- Verificar si esta ordenado')
        print('3- Existe el valor de x')
        print('4- Ordenar en forma ascendente')
        print('5- Cantidad de veces que tiene x')
        print('6- Valores ubicados en índice impar')
        print('7- En secuencia k')
        print()
        op = int(input('Ingrese una opción: '))
        print()

        if op == 1:
            # Carga de los datos de los libros
            tam = validar_mayor_que('Ingrese la cantidad de valores: ', 0)
            vec = [None] * tam
            cargar(vec)

        elif op == 2:
            res = enOrdenAscendente(vec)
            if res == True:
                print('Los valores estan en orden ascendente...')
            else:
                print('El vector no esta en orden ascendente...')

        elif op == 3:
            x = int(input('Ingrese el valor a buscar: '))
            res = existe(vec, x)
            if res == True:
                print('Existe el valor ', x, ' NO existe en el vector...')
            else:
                print('El valor ', x, ' NO existe en el vector...')

        elif op == 4:
            ordenarMenorMayor(vec)

        elif op == 5:
            x = int(input('Ingrese el valor a buscar: '))
            cantidad = existe(vec, x)
            print('La cantidad de veces que aparece ', x, ' es: ', cantidad)

        elif op == 6:
            mostrarValoresIndiceImpar(vec)

        elif op == 7:
            k = int(input('Ingrese secuencia a verificar: '))
            res = existe(vec, k)
            if res == True:
                print('Esta en secuencia de ', k, ' en ', k)
            else:
                print('NO esta en secuencia de ', k, ' en ', k)

        input('Presione una tecla para continuar ...')

if __name__ == '__main__':
    test()
