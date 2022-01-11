# 1. Ordenar y buscar
# Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100
# inclusive (pueden existir duplicados). A partir de ese arreglo:
# Ordenarlo de forma ascendente y mostrarlo
# Buscar un elemento x dentro del arreglo (x se ingresa por teclado).
# Si no existe, informarlo. Si existe, determinar cuántos valores impares
# mayores a x se encontraron en el arreglo.
import random


# genera un vector de n valores aleatorios
def gen_rand_list(vector, numero):
	for i in range(numero):
		vector.append(random.randint(1, 100))
	return vector


# ordena una lista de forma acendente o decendente...
def selection_sort(v, acendent=True):
	n = len(v)
	if acendent == True:
		print('acendente')
		for i in range(n - 1):
			for j in range(i + 1, n):
				if v[i] < v[j]:
					v[i], v[j] = v[j], v[i]
		return v
	else:
		print('decendente')
		for i in range(n - 1):
			for j in range(i + 1, n):
				if v[i] > v[j]:
					v[i], v[j] = v[j], v[i]
		return v


# hace un conteo de impares mayores a un numero...
def cont_imp_may_num(vector, numero):
	contador_impares = 0
	for i in range(len(vector)):
		if vector[i] % 2 != 0 and vector[i] > numero:
			contador_impares += 1
	return contador_impares


# Busca un numero en una lista...
def search_number(vector):
	numero = int(input('ingrese valor que quiera buscar:'))
	n = len(vector)
	exist = False
	for i in range(n):
		if vector[i] == numero:
			exist = True
			return True, numero
			break
	return False, numero


def test():
	v = []
	n = int(input('ingrese cuantos valores quiere generar'))
	gen_rand_list(v, n)
	print(v)
	selection_sort(v)
	print(v)
	print('-' * 10)
	punto2 = search_number(v)
	if punto2[0]:
		print(f'se encontro el valor {punto2[1]}')
		impares = cont_imp_may_num(v, punto2[1])
		print('hay la cantidad de: ', impares, 'mayores al numero seleccionado')
	else:
		print(f'no se encontro el valor {punto2[1]} en el arreglo')


if __name__ == '__main__':
	test()
