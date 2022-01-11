# 4. El Almacen
# Un pequeño almacén de barrio necesita hacer un analisis de su libreta de
# cuenta corriente, para ello nos solicita un programa que permita procesar
# n deudas. Por cada deuda se tiene el nombre del cliente, el monto adeudado
# El programa debe:

# Informar el monto adeudado promedio del almacen
# Informar los datos de la menor deuda
# Informar el porcentaje de clientes que presentan un monto adeudado menor
# a un valor ingresado por el usuario, respecto del total de deudas
from random import *


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


class Deudas:
	def __init__(self, nombre, monto):
		self.nombre = nombre
		self.monto = monto


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


def Generacion(v, aleatorio=True):
	if aleatorio:
		for i in range(len(v)):
			nombre_deudor = random_name()
			cantidad_deuda = randint(100, 2000)
			v[i] = Deudas(nombre_deudor, cantidad_deuda)

	else:
		for i in range(len(v)):
			nombre_deudor = input('ingrese nombre: ')
			cantidad_deuda = int(input(f'ingrese deuda de {nombre_deudor}: '))
			v[i] = Deudas(nombre_deudor, cantidad_deuda)


def write(v):
	print(color.PURPLE + '■■' * 40 + color.END)
	for i in range(len(v)):
		print(color.PURPLE + '■' + color.END, 'Nombre: ', v[i].nombre,
			  color.PURPLE + '■' * 10 + color.END, 'monto: ', v[i].monto,
			  color.PURPLE + '■' + color.END, )
	print(color.PURPLE + '■■' * 40 + color.END)


def cant_valores_men(v, x):
	cont = 0
	for i in range(len(v)):
		if x > v[i].monto:
			cont += 1
	return cont

def ordenar_deuda(v, creciente=True):
	n=len(v)
	if creciente:
		for i in range(n-1):
			for j in range(i+1,n):
				if v[i].monto>v[j].monto:
					v[i],v[j] = v[j], v[i]
	else:
		for i in range(n-1):
			for j in range(i+1,n):
				if v[i].montos<v[j].montos:
					v[i],v[j] = v[j], v[i]


def porcentaje(x, y):
		if y!=0:
			operacion= (x*100/y)
			return operacion
		else:
			return 0


def principal():
	print('EL ALMACEN\nLibreta Cuenta Corriente ')
	n = int(input('ingrese cuantos deudores hay: '))
	v = [None] * n
	Generacion(v)
	write(v)
	ordenar_deuda(v)
	print('los datos de la deuda mas baja es nombre: ',v[0].nombre, 'monto: '
		  , v[0].monto)
	promedio(v)
	x = int(input('ingrese valor para hacer la busqueda: '))
	vm=cant_valores_men(v, x)
	porc_clientes= porcentaje(vm, len(v))
	print('el porcentaje de clientes que presentan un monto adeudado menor a'
		  f' {x} por el usuario,\n respecto del total de deudas es de: {porc_clientes}')

def promedio(v):
	print('■' * 60)
	suma = 0
	for i in range(len(v)):
		suma += v[i].monto
	if len(v) != 0:
		operacion = suma / len(v)
		print('El promedio de las deudas es de: ', operacion)
	else:
		print('0')


if __name__ == '__main__':
	principal()
