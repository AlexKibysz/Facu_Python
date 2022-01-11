from random import *


class Jugadores:
	def __init__(self, nombre, pos, hits):
		self.nombre = nombre
		self.pos = pos
		self.hits = hits


def random_name():
	nombre = (
		"Alex", "Bian", "Jere", "Benja", "Juan", "Mateo", "Matias", "Marcos",
		"Lucas", "Melisa", "Anilem", "Valentino", "Uriel", "Brian", "Kevin",
		"Erick", "Lara", "Lucia", "Maximo", "Vladimir", "Jorge")
	apellido = ("Benito", "Mohamed", "Hernández", "Brown", "Rodríguez",
				"Da Silva", "García", "Álvarez", "Müller ", "Cuevas",
				"Cevedo", "Cabrera", "Iglesias", "Jaramillo", "Machado",
				"Ocampo", "Ramón", "Kauffman", "Krispin")
	nombre1 = choice(nombre)
	apellido1 = choice(apellido)
	completo = (nombre1 + " " + apellido1)
	return completo


def carga(v):
	for i in range(len(v)):
		nombre = random_name()
		pos = randint(1, 9)
		hits = randint(1, 20)
		v[i] = Jugadores(nombre, pos, hits)


def validar_mayor(valor, msg='Ingrese cantidad'):
	op = int(input(msg))
	while op < valor:
		print(f'Ingrese un numero mayor a {valor}')
		op = int(input(msg))
	return op


def crear_matriz(v):
	matriz = [[0] * 20 for c in range(9)]
	for i in range(len(v)):
		matriz[v[i].pos - 1][v[i].hits - 1] += 1
	return matriz


def mostrar_matriz(matriz):
	filas = len(matriz)
	print('\033[0;36;47mnumeros: ', end='')
	for c in range(20):
		print('{0:^6}'.format(c + 1), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f < 10:
			print(f'\033[0;36;47mdado 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mdado {f}: |\033[0m', end='')
		for c in range(20):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()


def mostrar_sum_fila(matriz):
	cont = 0
	x = int(input('Ingrese la posicion que quiera analizar: '))
	for c in range(len(matriz[0])):
		cont += matriz[x][c]
	print(f'la sumatoria de esa posicion es: {cont}')
	return cont


def principal():
	x = int(input('Ingrese cantidad de Jugadores que quiera crear'))
	v = [0] * x
	carga(v)
	matriz = crear_matriz(v)
	mostrar_matriz(matriz)
	cont = mostrar_sum_fila(matriz)


if __name__ == '__main__':
	principal()
