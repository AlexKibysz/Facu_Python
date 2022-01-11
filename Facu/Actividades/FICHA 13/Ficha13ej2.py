# 2. Alumnos
# Ingresar (o generar de manera aleatoria) los legajos de los n alumnos de un
# curso, siendo n un valor que se carga por teclado, y almacenarlos en un
# arreglo unidimensional. Se pide para ello:

# a - Ordenar el arreglo de menor a mayor. Mostrar por pantalla como quedó.

# b - Buscar en el arreglo el alumno con el legajo x, x se ingresa por teclado.
# Si existe mostrarlo, si no mostrar un mensaje de error.
from random import *

def legajo_gen():
	cantidad = int(input('ingrese cuantos valores quiere generar'))
	print('1.random')
	print('2.Carga por teclado')
	print('-1. no generar')
	opcion = int(input('ingrese opcion (1,2)'))
	while opcion != -1:
		if opcion == 1:
			v = []
			for i in range(cantidad):
				(v, v.append(randint(10000, 99999)))
			return v
			break
		elif opcion == 2:
			v = []
			for i in range(cantidad):
				v.append(int(input(f'ingrese el {i} legajo')))
			return v
			break


def selection_sort(vector, decendente=True):
	n = len(vector)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if decendente:
				if vector[i] < vector[j]:
					vector[i], vector[j] = vector[j], vector[i]
			else:
				if vector[i] > vector[j]:
					vector[i], vector[j] = vector[j], vector[i]
	return vector

def search_number(v,x):
	flag=False
	for i in range(len(v)):
		if v[i]==x:
			flag=True
			break
	if flag:
		return f'se encontro el valor {v[i]}'
	else:
		return 'No se encontro valor'


def test():
	v = legajo_gen()
	print('vector')
	print(v)


	f=selection_sort(v)
	print('Vector ordenado')
	print(f)

	t=int(input('ingrese el legajo que quiera buscar: '))
	print(search_number(v, t))

	delay(0.2)

if __name__ == '__main__':
	test()
