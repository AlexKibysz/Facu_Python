from random import *
import time


# genera vector de meses del año y promedios en cada uno...
def carga_meses(meses):
	lis = [0] * 12
	for i in range(len(lis)):
		lis[i] = int(
			input('-->Ingrese el promedio del mes ' + str(meses[i]) + ': '))
	return lis


# genera el promeido de una sumatoria de los valores de una lista...
def promedio(cant, lista):
	suma = prom = 0
	if len(lista) != 0:
		for i in range(cant):
			suma += lista[i]

		prom = suma / cant
	return prom

def porcentaje(cant, cant_total):
	if cant_total != 0:
		calculo = round((cant * 100) / cant_total, 2)
		print(f'el porcentaje de {cant} respecto al total es de: {calculo}%')
		return calculo
	else:
		return 0

# realiza la sumatoria de una lista
def sumatoria(lista):
	suma = 0
	for i in range(len(lista)):
		suma += lista[i]
	return suma


# teniendo 12 meses en una lista analiza los trimestres
def trimestre_promedio(lista, trimestre):
	if trimestre == 1:
		trimestre_1 = lista[:3]
		print(trimestre_1)
		return promedio(sumatoria(trimestre_1), 3)
	if trimestre == 2:
		trimestre_2 = lista[3:6]
		print(trimestre_2)
		return promedio(sumatoria(trimestre_2), 3)
	if trimestre == 3:
		trimestre_3 = lista[6:9]
		print(trimestre_3)
		return promedio(sumatoria(trimestre_3), 3)
	if trimestre == 4:
		trimestre_4 = lista[9:]
		print(trimestre_4)
		return promedio(sumatoria(trimestre_4), 3)


# Busca el menor en una lista...
def menor_cant(lista):
	menor = lista[0]
	for i in range(len(lista)):
		if lista[i] < menor:
			menor = i + 1
	return menor


# crea un vector con los numeros mayores al promedio de la lista...
def mayor_prom(lista, promedio):
	mayores = []
	for i in range(len(lista)):
		if lista[i] > promedio:
			mayores.append(i + 1)
	return mayores


# Genera un vector de n componentes por carga de teclado
def carga_manual():
	vector = []
	n = int(input('Ingrese cuantos valores quiere cargar al vector: '))
	if n == 0:
		return vector
	else:
		for i in range(n):
			numero = int(input(f'ingrese valor del {i + 1} elemento: '))
			vector.append(numero)
		return vector


# busca en la lista cuantas componentes estan repetidas(tiene que estar ORDENADO)
def repeticion(lista):
	repetidas = 0
	for i in range(len(lista)):
		if lista[i] == lista[-1]:
			repetidas += 1
	return repetidas


# Verifica si un numero es primo
def esPrimo(num):
	if num <= 1:
		return False
	elif num == 2:
		return True
	else:
		for i in range(2, num):
			if num % i == 0:
				return False
		return True


# Genera una lista con los valores primos
def lista_primos(lista):
	primos_lista = []
	for i in range(len(lista)):
		if esPrimo(lista[i]):
			primos_lista.append(lista[i])
	return primos_lista


# Genera una fusion de una lista con los valores mayores entre estos
def lista_mayores(lista1, lista2):
	lista = []
	for x in range(len(lista1)):
		if lista1[x] > lista2[x]:
			lista.append(lista1[x])
		else:
			lista.append(lista2[x])
	return lista


# genera un vector de n valores aleatorios(importar random)
def gen_rand_list(vector, numero):
	for i in range(numero):
		vector.append(random.randint(1, 100))
	return vector


# imprime mensaje con delay o tiempo de espera #importar time
def delay(segundos):
	texto = input('ingrese texto: ')
	for i in texto:
		time.sleep(segundos)
		print(i, end='')


# Validar intervalo
def validar_intervalo(n1, n2, mensaje='Ingrese seleccion ➡:  '):
	num = n1 - 1
	while num < n1 or num > n2:
		num = int(input(mensaje))
		if num < n1 or num > n2:
			print('Porfavor elija un valor entre:', n1,
				  'y', n2)
	return num


# validar que un numero sea mayor a
def validar_mayor_que(num, msg='Ingrese un valor: '):
	x = num - 1
	while x <= num:
		x = int(input(msg))
		if x <= num:
			print('ERROR: Porfavor elija un valor mayor a', num)
	return x


# menu generico


# fusiona dos listas de elementos
def fusion(a, b):
	# crear el tercer arreglo con lugar para n + m elementos...
	n, m = len(a), len(b)
	t = n + m
	c = t * [0]

	# aplicar proceso de fusión...
	i = k = j = 0
	while i < n and j < m:
		if a[i] < b[j]:
			c[k] = a[i]
			i += 1
		else:
			c[k] = b[j]
			j += 1

		k += 1
		# determinar cuál de los vectores (a o b) terminó primero...
		# ... apuntar con v al otro...
		v, pos = b, j
	if i < n:
		v, pos = a, i

	# copiar en el vector de salida todos los valores que
	# quedaban en el vector v...
	while pos < len(v):
		c[k] = v[pos]
		pos += 1
		k += 1

	# retornar el vector fusionado...
	return c


# busqueda lineal de un valor en una lista
def linear_search(v, x):
	r = -1
	for i in range(len(v)):
		if x == v[i]:
			r = i

	return r


# CLASE PARA COLORES EN EL TEXTO
class color:
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[1;36;48m'
	BOLD = '\033[1;37;48m'
	BLUE = '\033[1;34;48m'
	GREEN = '\033[1;32;48m'
	YELLOW = '\033[1;33;48m'
	RED = '\033[1;31;48m'
	BLACK = '\033[1;30;48m'
	UNDERLINE = '\033[4;37;48m'
	END = '\033[1;37;0m'


# print(color.PURPLE + 'Soy violeta'+ color.END)


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


# conversor de decimal a binario
def deci_a_binario():
	print('Calculadora de DECIMAL A BINARIO')
	x = float(input('Ingrese valor'))
	enterox = int(x)
	flotantex = x - enterox
	n = 1
	c = 1
	v = []
	while n != 0:
		n = enterox // (2)
		print(f'n es{n}')
		v.append(enterox % (2))
		enterox = n
		c += 1

	v.append(f'coma {flotantex * 2}')
	print(v, end='')
	return v


def generar_matriz_metodo1():
	matriz = []
	# filas y columna
	filas = int(input('Ingrese cantidad de filas: '))
	columnas = int(input('ingrese cantidad de columnas: '))
	for f in range(filas):
		matriz.append([])
		for c in range(columnas):
			matriz[f].append(randint(1, 20))
	print(matriz)
	return matriz


# metodo resumido
def generar_matriz_metodo2():
	filas = int(input('Ingrese filas'))
	columnas = int(input('Ingrese columnas'))
	matriz = [[None] * columnas for f in range(filas)]
	for f in range(filas):
		for c in range(columnas):
			matriz[f][c] = randint(1, 20)
	return matriz


def mostrar_matriz(matriz):
	for i in range(len(matriz[0])):
		print('{0:>4}'.format(str(i)), end='')
	print()
	for f in range(len(matriz)):
		print('{0:<1} {1:}'.format(f, str(matriz[f])))


def sumatoria_matriz_total(matriz):
	cont = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[f])):
			cont += matriz[f][c]
	print(cont)
	return cont


def sumatoria_fila(matriz):
	x = int(input(
		f'Ingrese la fila que quiera hacer la sumatoria (entre 0 y {len(matriz) - 1}): '))
	cont = 0
	for i in range(len(matriz[x])):
		cont += matriz[x][i]
	print('la cantidad en la fila seleccionada es de: ', cont)
	return matriz


def sumatoria_columna(matriz):
	x = int(input(
		f'ingrese la matriz a la cual le desea hacer la sumatoria (entre 0 y {len(matriz[0]) - 1}): '))
	cont = 0
	for c in range(len(matriz)):
		cont += matriz[c][x]
	print('la cantidad en la columna seleccionada es de: ', cont)
	return cont


def remplazar(matriz, x, y):
	ant = matriz[x][y]
	matriz[x][y] = int(input('Ingrese numero: '))
	print(f'cambio el valor de {ant} por {matriz[x][y]}')
	return matriz

def menor_cantidad_matriz(matriz):
	filas=len(matriz)
	columnas=len(matriz[0])
	menor=matriz[0][0]
	for f in range(filas):
		for c in range(columnas):
			if menor>matriz[f][c]:
				menor=matriz[f][c]
				pos1=f
				pos2=c
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

def porcentaje_fila(matriz):
	total = sumatoria(matriz)
	cant_fila = 0
	x = validar_intervalo(0, len(matriz),
						  'Ingrese La fila la cual quiere saber el porcentaje: ')
	for i in range(len(matriz[0])):
		cant_fila += matriz[x][i]
	porc = porcentaje(cant_fila, total)
	return porc

def porcentaje_columna(matriz):
	total = sumatoria(matriz)
	cant_fila = 0
	x = validar_intervalo(0, len(matriz[0]),
						  'Ingrese La columna la cual quiere saber el porcentaje: ')
	for i in range(len(matriz[0])):
		cant_fila += matriz[i][x]
	porc = porcentaje(cant_fila, total)
	return porc

