# 3. Concurso de baile
# Desarrollar un programa que permita procesar el puntaje obtenido por una pareja de bailarines en un concurso de TV.

# Para ello, generar un vector de 7 elementos, representando a los miembros del
# jurado. Por cada celda, generar un valor aleatorio entre -1 y 10 (inclusive)
# indicando la puntuación recibida.

# A continuación, informar:

# •Los tres mejores puntajes recibidos.
# •Si algún jurado los calificó con 6. En caso afirmativo, indicar cuántas notas mayores a esa recibieron.
# •La diferencia entre el mayor y el menor puntaje.
# 1•El puntaje total obtenido. Si es menor a 20, indicar que quedan descalificados.
import random


def generate_list():
	v = []
	for i in range(6):
		v.append(random.randint(-1, 10))
	return v


def ordenar(vector):
	n = len(vector)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if vector[i] < vector[j]:
				vector[i], vector[j] = vector[j], vector[i]
	print(vector)
	return vector


def mayores_a(v, x):
	print(f'mayores a {x}')
	n = len(v)
	v1 = []
	for i in range(n):
		if v[i] > x:
			v1.append(v[i])
	return v1


def dif_max_min(v):
	n = len(v)
	operacion = abs(v[n - 1] - v[0])
	return operacion


def total_list(v):
	n = len(v)
	sumatoria = 0
	for i in range(n):
		sumatoria += v[i]
	return sumatoria


def cut_best(v, x):
	v1 = ordenar(v)
	print(f'los {x} mejores son: ')
	v1 = v1[:x]
	return v1


def test():
	puntajes = generate_list()
	p_c = ordenar(puntajes)
	n=cut_best(p_c, 3)
	print(n)
	print('*' * 78)
	punto_2 = mayores_a(p_c, 6)
	print(punto_2)
	print('diferencia entre el mas grande y el mas chico')
	dif = dif_max_min(p_c)
	print(dif)
	if 20 > total_list(p_c):
		print(f'equipo descalificado con: {total_list(p_c)}')
	else:
		print(f'el total puntuado es: {total_list(p_c)}')


if __name__ == '__main__':
	test()
