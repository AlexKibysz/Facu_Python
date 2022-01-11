# filas= caja(0 al 9)  columna= turno(0,1,2) valor=monto cobrado
from random import *


def crear_matriz(auto=True):
	matriz = [[0] * 3 for c in range(10)]
	if auto:
		for f in range(10):
			for c in range(3):
				matriz[f][c] = randint(1, 100)
		return matriz
	else:
		for f in range(10):
			for c in range(3):
				matriz[f][c] = int(input(
					f'Ingrese monto cobrado: para la caja {f} y turno {c}'))
		return matriz


def mostrar_matriz(matriz):
	filas = len(matriz)
	print('\033[0;36;47mTurno: ', end='')
	for c in range(len(matriz[0])):
		print('{0:>6}'.format(c + 1), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f < 10:
			print(f'\033[0;36;47mCaja 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mCaja {f}: |\033[0m', end='')
		for c in range(len(matriz[0])):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()


def validar_intervalo(n1, n2, mensaje='Ingrese seleccion ➡:  '):
	num = n1 - 1
	while num < n1 or num > n2:
		num = int(input(mensaje))
		if num < n1 or num > n2:
			print('Porfavor elija un valor entre:', n1,
				  'y', n2-1)
	return num


def promedio_fila(matriz, total):
	x = validar_intervalo(0, len(matriz), 'Ingrese la fila que quiera analizar: ')
	cont1 = 0
	for c in range(len(matriz[0])):
		cont1 += matriz[x][c]
	promedio = total/cont1
	print(f'El promedio de recaudacion de la caja {x} es de : {promedio}')


def sumatoria_and_max_min(matriz):
	total = 0
	mayor = matriz[0][0]
	menor = matriz[0][0]
	pos1 = 0
	pos2 = 0
	pos3 = 0
	pos4 = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			if mayor < matriz[0][0]:
				mayor=matriz[f][c]
				pos1 = f
				pos2 = c
			elif menor > matriz[f][c]:
				menor=matriz[f][c]
				pos3 = f
				pos4 = c
			total += matriz[f][c]
	print(
		f'El mayor valor encontrado es {mayor} en la posicion ({pos1}, {pos2})')
	print(
		f'El Menor valor encontrado es {menor} en la posicion ({pos3}, {pos4})')
	porcentaje(mayor, total)
	return total


def porcentaje(cant, total):
	if total == 0:
		return 0
	else:
		operacion = (cant * 100) / total
		print(f'El promedio es de {operacion}%')
		return operacion


def principal():
	matriz = crear_matriz()
	mostrar_matriz(matriz)
	total = sumatoria_and_max_min(matriz)
	promedio_fila(matriz, total)


if __name__ == '__main__':
	principal()
