# 1. Empresa de colectivos
# Una empresa de colectivos desea generar estadística sobre sus pasajeros.
# Sus líneas están enumeradas de 0 a n, y las paradas de 0 a m.

# En primer lugar, se debe ingresar por teclado la cantidad de líneas
# de colectivo y el número de paradas a procesar.

# Luego cargar una tabla de doble entrada, donde cada fila represente a
# una de las líneas y cada columna una parada, indicando la cantidad de
# pasajeros que subieron al colectivo.

# Con esa información establecer:

# Cuál fue el total de pasajeros transportado por cada una de las líneas
# Cuál fue la cantidad promedio de pasajeros, para una parada que se ingresa por teclado
# Cuál fue la menor cantidad de pasajeros, para una línea que se ingresa por teclado.
# Cuál fue la recaudación de la empresa en el período analizado, sabiendo que el precio del boleto es de $8,5.
from random import *


def validar_mayor_que(num, msg='Ingrese un valor: '):
	x = num - 1
	while x <= num:
		x = int(input(msg))
		if x <= num:
			print('ERROR: Porfavor elija un valor mayor a', num)
	return x


def crear_matriz(x, y):
	matriz = [[None] * x for c in range(y)]
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			matriz[f][c] = randint(1, 100)
	return matriz


def mostrar_matriz(matriz):
	filas = len(matriz)
	columnas = len(matriz[0])
	print('\033[0;36;47mcolectivos: ', end='')
	for c in range(columnas):
		print('{0:^6}'.format(c), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f<10:
			print(f'\033[0;36;47mlineas 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mlineas {f}: |\033[0m', end='')
		for c in range(columnas):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()


def sumatoria(matriz):
	cont = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			cont += matriz[f][c]
	print(f'La cantidad total de pasajeros fue de: {cont}')
	return cont


def validar_intervalo(n1, n2, mensaje='Ingrese seleccion ➡:  '):
	num = n1 - 1
	while num < n1 or num > n2:
		num = int(input(mensaje))
		if num < n1 or num > n2:
			print('Porfavor elija un valor entre:', n1,
				  'y', n2)
	return num


def porcentaje(cant, cant_total):
	if cant_total != 0:
		calculo = round((cant * 100) / cant_total, 2)
		print(f'el porcentaje de {cant} respecto al total es de: {calculo}%')
		return calculo
	else:
		return 0


def porcentaje_fila(matriz):
	total = sumatoria(matriz)
	cant_fila = 0
	x = validar_intervalo(0, len(matriz),
						  'Ingrese La fila la cual quiere saber el porcentaje: ')
	for i in range(len(matriz[0])):
		cant_fila += matriz[x][i]
	porc = porcentaje(cant_fila, total)
	return porc


def menor_cantidad_matriz(matriz):
	filas = len(matriz)
	columnas = len(matriz[0])
	menor = matriz[0][0]
	for f in range(filas):
		for c in range(columnas):
			if menor > matriz[f][c]:
				menor = matriz[f][c]
				pos1 = f
				pos2 = c
	print(f'El menor valor fue {menor} en la fila {pos1} columna {pos2}')
	return menor


def mayor_cantidad_matriz(matriz):
	filas = len(matriz)
	columnas = len(matriz[0])
	mayor = matriz[0][0]
	for f in range(filas):
		for c in range(columnas):
			if mayor < matriz[f][c]:
				mayor = matriz[f][c]
				pos1 = f
				pos2 = c
	print(f'El mayor valor fue {mayor} en la fila {pos1} columna {pos2}')
	return mayor

def porcentaje_columna(matriz):
	total = sumatoria(matriz)
	cant_fila = 0
	x = validar_intervalo(0, len(matriz[0]),
						  'Ingrese La columna la cual quiere saber el porcentaje: ')
	for i in range(len(matriz[0])):
		cant_fila += matriz[i][x]
	porc = porcentaje(cant_fila, total)
	return porc

if __name__ == '__main__':
	colectivos = validar_mayor_que(0, 'Ingrese la cantidad de colectivos: ')
	paradas = validar_mayor_que(0, 'Ingrese la cantidad de paradas: ')
	matriz = crear_matriz(colectivos, paradas)
	mostrar_matriz(matriz)
	total = sumatoria(matriz)
	print('\n' * 3)
	porcentaje_fila(matriz)
	menor_cantidad_matriz(matriz)
	mayor_cantidad_matriz(matriz)
	print(f'la cantidad recaudada es de: {total * 8.5}')
	porcentaje_columna(matriz)
