from random import *

def generar_matriz_metodo1():
    matriz=[]
    #filas y columna
    filas=int(input('Ingrese cantidad de filas: '))
    columnas=int(input('ingrese cantidad de columnas: '))
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(randint(1,20))
    print(matriz)
    return matriz

#metodo resumido
def generar_matriz_metodo2():
    filas= int(input('Ingrese filas'))
    columnas = int(input('Ingrese columnas'))
    matriz=[[None]*columnas for f in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=randint(1,20)
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz[0])):
        print('{0:>4}'.format(str(i)),end='')
    print()
    for f in range(len(matriz)):
        print('{0:<1} {1:}'.format(f,str(matriz[f])))

def sumatoria_matriz_total(matriz):
    cont=0
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
          cont += matriz[f][c]
    print(cont)
    return cont

def sumatoria_fila(matriz):
    x=int(input(f'Ingrese la fila que quiera hacer la sumatoria (entre 0 y {len(matriz)-1}): '))
    cont=0
    for i in range(len(matriz[x])):
        cont+=matriz[x][i]
    print('la cantidad en la fila seleccionada es de: ',cont)
    return matriz

def sumatoria_columna(matriz):
    x=int(input(f'ingrese la matriz a la cual le desea hacer la sumatoria (entre 0 y {len(matriz[0])-1}): '))
    cont=0
    for c in range(len(matriz)):
        cont+=matriz[c][x]
    print('la cantidad en la columna seleccionada es de: ',cont)
    return cont

def remplazar(matriz, x, y):
    ant=matriz[x][y]
    matriz[x][y]=int(input('Ingrese numero: '))
    print(f'cambio el valor de {ant} por {matriz[x][y]}')
    return matriz

if __name__ == '__main__':
    matriz=generar_matriz_metodo2()
    print(matriz)
    print('=0'*23)
    print('Matriz con indices y format')
    mostrar_matriz(matriz)
    print()
    print('sumatoria de los valores')
    sumatoria_matriz_total(matriz)
    print()
    print('sumatoria de una fila')
    sumatoria_fila(matriz)
    print()
    print('sumatoria de una columna')
    sumatoria_columna(matriz)
    print('------remplazar un valor---------')
    x=int(input(f'posicion de la fila del 0 al {len(matriz)-1}'))
    y=int(input(f'posicion de la columna del 0 al {len(matriz[0])-1}'))
    matriz = remplazar(matriz, x, y)
    mostrar_matriz(matriz)
