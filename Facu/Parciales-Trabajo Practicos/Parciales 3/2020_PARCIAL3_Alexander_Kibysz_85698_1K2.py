
''''Una veterinaria desea un programa que procese los datos de las ventas que realiza.
 En cada venta se registran los siguientes datos: el número de factura,
  importe de la factura, el tipo de factura (A, B, C o E), el apellido
  de la persona que realiza la compra, y un tipo de alimento que indica
  la marca del alimento vendido (un número entero entre 0 y 20, por ejemplo:
   0: Dogui, 1: Dog Chow, etc.). Se desea almacenar la información referida a
    las n ventas que realiza la veterinaria en un arreglo de registros de tipo
    Venta (definir el tipo Venta y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de
 opciones,  que permita gestionar las siguientes tareas:

Cargar el arreglo pedido con los datos de las n ventas realizadas. Valide
 que el número identificador de la venta sea positivo. El importe de la
 factura debe ser mayor a 0 y menor a 100.000 pesos. El tipo de factura
 debe ser alguno de los tipos válidos: A, B, C o E, y el tipo de alimento
 debe ser un número entero entre 0 y 20 ambos incluidos. Puede hacer la
 carga en forma manual, o puede generar los datos en forma automática
 (con valores aleatorios) o puede disponer de ambas técnicas si lo desea.
 Pero al menos una debe programar.
Mostrar todos los datos de las ventas cuyo importe de factura se encuentre
en el rango de dos valores "x" e "y", donde x e y son valores que se cargan
por teclado. Ellistado debe salir ordenado de mayor a menor según los apellidos
 de las personas que realizaron la compra.
Determinar y mostrar el importe total facturado para cada uno de los 21 tipos
 posibles (en un vector de acumulación) e informe por pantalla solamente los
  totales facturados por los tipos 0 al 12, es decir mostrar 13 números por
  pantalla con el importe acumulado solamente por esos tipos
  (incluidos aquellos cuyo conteo dió 0).
Ingresar por teclado un tipo de factura y mostrar el número de factura y el
apellido de las ventas con ese tipo, que tengan un precio mayor que el
precio promedio de ventas de todo el vector. Si no existe ninguna venta
con ese tipo de factura informarlo por pantalla.
Determinar si existe una venta cuyo número de factura sea igual a
num pero que no sea del tipo de factura E,  siendo n un valor que
se carga por teclado. Si existe, mostrar todos sus datos.
 Si no existe, informar con un mensaje. Si existe más
 de un registro que coincida con esos parámetros de búsqueda,
  debe mostrar el primero que encuentre.'''

# CLASS DATOS.... NUMERO DE FACTURA, IMPORTE FACTURA,
# FACTURA(A,B,C),APELLIDO, MARCA (0 AL 20)
from random import *


class Ventas:
	def __init__(self, numfac, importe, tipo_fac, apellido, marca):
		self.numfac = numfac
		self.importe = importe
		self.tipo_fac = tipo_fac
		self.apellido = apellido
		self.marca = marca


def validar_intervalo_entero(n1, n2, msg='Ingrese su seleccion: '):
	num = n1 - 1
	while num < n1 or num > n2:
		num = int(input(msg))
		if num < n1 or num > n2:
			print(f'porfavor elija valor entre {n1} y {n2}')
	return num


def random_apellido():
	apellidos = ['Lopez', 'Correa', 'Sarmiento', 'Soldado',
				 'Ruiz', 'Fernandez', 'Kauff', 'Orwell', 'Reed',
				 'Kengsinton', 'Suarez', 'Leiva', 'Garcia']
	sel = choice(apellidos)
	return sel


def carga(v):
	tipos = ['A', 'B', 'C', 'E']
	for i in range(len(v)):
		numero_factura = randint(10000, 90000)
		importe = round(uniform(0, 100000), 2)
		tipo_fac = choice(tipos)
		apellido = random_apellido()
		marca = randint(0, 20)
		v[i] = Ventas(numero_factura, importe, tipo_fac, apellido, marca)


print('Parcial Numero 3...')


def write(v, List=True):
	if List:
		print('{0:^14}{1:^10}{2:^13}{3:^12}{4:3}'.format('numero factura',
														 'importe',
														 'tipo factura',
														 'apellido',
														 'Marca'))
		for i in range(len(v)):
			print('{0:^14}{1:^10}{2:^13}{3:^12}{4:5}'.format(v[i].numfac,
															 v[i].importe,
															 v[i].tipo_fac,
															 v[i].apellido,
															 v[i].marca))
	else:
		print('{0:^14}{1:^10}{2:^13}{3:^12}{4:3}'.format('numero factura',
														 'importe',
														 'tipo factura',
														 'apellido',
														 'Marca'))
		print('{0:^14}{1:^10}{2:^13}{3:^12}{4:5}'.format(v.numfac,
														 v.importe,
														 v.tipo_fac,
														 v.apellido,
														 v.marca))


def vector_acumulador(v):
	v2 = [0] * 21
	for i in range(len(v)):
		x = v[i].marca
		v2[x] += v[i].importe
	return v2


def ordenar(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].apellido > v[j].apellido:
				v[i], v[j] = v[j], v[i]
	return v


def punto_2(v):
	x = float(input('ingrese valor Minimo: '))
	y = float(input('ingrese valor Maximo: '))
	v = ordenar(v)
	for i in range(len(v)):
		if x <= v[i].importe and v[i].importe <= y:
			write(v[i], False)


def busqueda_factura(v, tipo):
	print('{0:^20}{1:10}'.format('Numero Factura', 'Apellido'))
	for i in range(len(v)):
		if v[i].tipo_fac == tipo:
			print('{0:^20}{1:10}'.format(v[i].numfac, v[i].apellido))


def punto_5(v, numero):
	b = False
	for i in range(len(v)):
		if v[i].numfac == numero and v[i].tipo_fac != 'E':
			write(v[i], False)
			b = True
	if b == False:
		print('No se encontro valor')


def validar_positivo(num, msg='Ingrese cuantos valores quiere generar:  '):
	x = num - 1
	while x <= num:
		x = int(input(msg))
		if x <= num:
			print(f'Error ingrese un valor mayor a {num}')
	return x


def menu(v):
	ban = False
	opcion = 1
	while opcion > 0:
		print('⁕' * 100)
		print('Menu de Ventas \n1. Cargar datos al las ventas\n2.'
			  ' Mostrar todos los datos de las ventas cuyo importe de factura se '
			  'encuentre en el rango de dos valores "x" e "y"\n3. Determinar y mostrar el'
			  ' importe total facturado para cada uno de las 13 marcas\n4.'
			  ' Ingresar por teclado un tipo de factura y mostrar el número de'
			  ' factura y el apellido de las ventas con ese tipo\n5. Determinar '
			  'si existe una venta cuyo número de factura sea igual a num pero '
			  'que no sea del tipo de factura E\n0. Salir')
		print('⁕' * 100)
		opcion = validar_intervalo_entero(0, 5)
		if opcion == 1:
			carga(v)
			ban = True
			op = int(input('desea mostrar los datos cargados: (1.si 2.no)'))
			if op == 1:
				print('⁕' * 50)
				write(v)
				print('⁕' * 50)
		if opcion == 2:
			if ban:
				print('⁕' * 50)
				punto_2(v)
			else:
				print('Por favor cargue datos en el punto 1 antes de continuar')
				continue
		if opcion == 3:
			if ban:
				v2 = vector_acumulador(v)
				print('⁕' * 50)
				for i in range(13):
					print('Marca: ', i, '------->', v2[i])
				print('⁕' * 50)
			else:
				print('Por favor cargue datos en el punto 1 antes de continuar')

		if opcion == 4:
			if ban:
				print('⁕' * 50)
				tipo = input('Ingrese el tipo de Factura: (A,B,C,E): ').upper()
				busqueda_factura(v, tipo)
				print('⁕' * 50)
			else:
				print('Por favor cargue datos en el punto 1 antes de continuar')
		if opcion == 5:
			if ban:
				numero = int(input('Ingrese numero de factura'))
				punto_5(v, numero)
			else:
				print('Por favor cargue datos en el punto 1 antes de continuar')
			if opcion == 0:
				break


def principal():
	n = validar_positivo(0, 'Ingrese cuantas ventas quiere generar: ')
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
