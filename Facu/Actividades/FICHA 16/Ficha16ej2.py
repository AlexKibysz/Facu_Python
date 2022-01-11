''''Hace algunas semanas se desarrolló una aplicación estadística,
lanzando simultáneamente 2 dados y anotando en 2 vectores paralelos los
 resultados obtenidos, para n lanzamientos (n se ingresa por teclado).

El mismo cliente nos pide ahora que agreguemos la generación de una tabla
de doble entrada, donde cada fila represente uno de los dados y cada columna
uno de sus valores posibles. La tabla debe contar cuantas veces apareció cada
valor en los lanzamientos efectuados.

El programa deberá:

Mostrar la tabla generada
Indicar qué valores aparecieron la misma cantidad de veces en ambos dados
Informar cuál fue el número con más apariciones para cada dado'''
from random import *

def dados(v, i):
	for i in range(i):
		v.append(randint(1,6))
	return v

def dados_generacion():
	x=int(input('Cuantas veces quiere lanzar los dados?: '))
	d1=[]
	d2=[]
	d1=dados(d1, x)
	d2=dados(d2, x)
	return d1, d2

def crear_matriz(d1,d2):
	matriz=[[0]*6 for c in range(2)]
	for i in range(len(d1)):
		x=d1[i]
		y=d2[i]
		matriz[0][x-1] += 1
		matriz[1][y-1] += 1
	return matriz

def mostrar_mayores_fila(matriz):
	mayor=matriz[0][0]
	mayor2=matriz[1][0]
	for c in range(len(matriz[0])):
		if mayor<matriz[0][c]:
			mayor=matriz[0][c]
			pos=c

		if mayor2<matriz[1][c]:
			mayor2=matriz[1][c]
			pos2=c
	print(f'el mayor valor en la fila 0 es {mayor}, en la posicion (0,{pos+1})')
	print(f'el mayor valor en la fila 0 es {mayor2}, en la posicion (1,{pos2+1})')
	return mayor, mayor2

def mostrar_iguales(matriz):
	for c in range(6):
		if matriz[0][c]==matriz[1][c]:
			print(f'Los valores son iguales en la columna: {c+1}')



def mostrar_matriz(matriz):
	filas = len(matriz)
	columnas = len(matriz[0])
	print('\033[0;36;47mnumeros: ', end='')
	for c in range(6):
		print('{0:^6}'.format(c+1), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f<10:
			print(f'\033[0;36;47mdado 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mdado {f}: |\033[0m', end='')
		for c in range(6):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()



def principal():
	d1, d2=dados_generacion()
	print('dado 1 : ',d1)
	print('dado 2 : ',d2)
	matriz= crear_matriz(d1, d2)
	print(matriz)
	mostrar_matriz(matriz)
	mostrar_iguales(matriz)
	mostrar_mayores_fila(matriz)

if __name__ == '__main__':
    principal()
