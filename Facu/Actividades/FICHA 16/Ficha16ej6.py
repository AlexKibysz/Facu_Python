# 6. Recorridos en matriz rectangular
# Hacer un programa que permita cargar una matriz de m x n números enteros,
# con m y n cargados previamente. Luego de la carga calcular y mostrar:

# Suma de todos los números
# Suma de cada fila
# Suma de cada columna
# Suma del contorno
# Suma de la mitad de arriba
# Suma del cuarto inferior derecho
from random import *


def crear_matriz(m, n):
	matriz = [[0] * m for c in range(n)]
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			matriz[f][c] = randint(1, 100)
	return matriz


def sumatoria(matriz):
	cont = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			cont += matriz[f][c]
	print(f'La sumatoria de la matriz es de: {cont}')
	return cont


def mostrar_matriz(matriz):
	filas = len(matriz)
	print('\033[0;36;47mm: ', end='')
	for c in range(len(matriz[0])):
		print('{0:^6}'.format(c + 1), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f < 10:
			print(f'\033[0;36;47mn 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mn {f}: |\033[0m', end='')
		for c in range(len(matriz[0])):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()


def sumatoria_columna(matriz):
	cont = 0
	cont2 = 0
	for c in range(len(matriz[0])):
		for f in range(len(matriz)):
			cont += matriz[f][c]
			if f == 0 or f == len(matriz):
				cont2 += matriz[f][c]
		print(f'La sumatoria de la columna {c} es de: {cont}')
		cont = 0
	return cont


def sumatorias_fila(matriz):
	cont = 0
	cont2 = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			cont += matriz[f][c]
			if c == 0 or c == len(matriz[0]):
				cont2 += matriz[f][c]
		print(f'La sumatoria de la Fila {f} es de {cont}')
		cont = 0
	return cont2


def principal():
	x = int(input('Ingrese cuantas filas quiere armar: '))
	y = int(input('Ingrese cuantas columnas quiere armar: '))
	matriz = crear_matriz(x, y)
	mostrar_matriz(matriz)
	total = sumatoria(matriz)
	print('=' * 50)
	laterales_fil = sumatorias_fila(matriz)
	print('=' * 50)
	laterales_col = sumatoria_columna(matriz)
	print('=' * 50)
	print(f'La sumatoria de los laterales son: {laterales_col + laterales_fil}')

if __name__ == '__main__':
	principal()
