from random import *
import os
import pickle


class Traslados:
	def __init__(self, identificacion, nombre, importe, destino, tipopago):
		self.identificacion = identificacion
		self.nombre = nombre
		self.importe = importe
		self.destino = destino
		self.tipopago = tipopago


def validar_intervalo(x, y, msg='Ingrese opcion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print(f'Seleccion no valida, Ingrese valor entre {x} y {y}.')
	return num


def validar_mayor_que(x, msg='Ingrese cantidad: ', entero=True):
	num = x - 1
	if entero:
		while x >= num:
			num = int(input(msg))
			if x >= num:
				print(f'Por favor ingrese un valor mayor a {x}')
		return num
	else:
		while x >= num:
			num = float(input(msg))
			if x >= num:
				print(f'Por favor ingrese un valor mayor a {x}')
		return num


def nombre_gen():
	sec1 = ['Pepe', 'Pablo', 'Juan', 'Gustavo', 'Val3rio', 'Juana', 'Selena',
			'Alexander', 'Sonia', '0o0o0Brian0o0o0o']
	sec2 = ['as', 'es', 're', 'te', 'be', 'si', '$', '🎆', ' ']
	sec3 = ['yao', 'Wolf', 'Carry', 'Sand', 'Lime', 'Silver', 'Stone']
	sec4 = ['ming', 'stram', 'son', 'los', 'isky', 'osky', 'hold']
	nombre = choice(sec1) + choice(sec2) + ' ' + choice(sec3) + choice(sec4)
	return nombre


def add_in_order_binary(v, valor):
	n = len(v)
	pos = n
	izquierda, derecha = 0, n - 1
	while izquierda <= derecha:
		c = (izquierda + derecha) // 2
		if v[c].identificacion == valor.identificacion:
			pos = c
			break
		if valor.identificacion < v[c].identificacion:
			derecha = c - 1
		else:
			izquierda = c + 1
		if izquierda > derecha:
			pos = izquierda
	v[pos:pos] = [valor]


def carga(n):
	v = []
	for i in range(n):
		id = randint(000, 99999)
		nombre_cliente = nombre_gen()
		importe = round(uniform(1000, 200000), 2)
		destino = randint(0, 22)
		tipo_pago = randint(0, 4)
		valor = Traslados(id, nombre_cliente, importe, destino, tipo_pago)
		add_in_order_binary(v, valor)
	return v


def to_string(v, all=True):
	if all:
		for i in range(len(v)):
			p = 'Identificacion {0:<10}'.format(v[i].identificacion)
			p += ' Nombre: {0:<25}'.format(v[i].nombre)
			p += ' Importe: {0:<15}'.format(v[i].importe)
			p += ' Provincia Destino: {0:<5}'.format(v[i].destino)
			p += ' Forma de pago: {0:<5}'.format(v[i].tipopago)
			print(p)
	else:
		p = 'Identificacion {0:<20}'.format(v.identificacion)
		p += ' Nombre: {0:<20}'.format(v.nombre)
		p += ' Importe: {0:<20}'.format(v.importe)
		p += ' Provincia Destino: {0:<5}'.format(v.destino)
		p += ' Forma de pago: {0:<5}'.format(v.tipopago)
		print(p)


def analisis_nombre_no_valido(nombre):
	letras = 'qwertyuipasdfghjklzxcvbnm '
	nombre = nombre.lower()
	ban = False
	for c in nombre:
		if c not in letras:
			ban = True
			return ban
			break
	if not ban:
		return ban


def busqueda_reg_nom(v, param):
	ban = True
	for i in range(len(v) - 1):
		for c in range(i + 1, len(v)):
			if v[i].nombre == param:
				ban = False
				to_string(v[i], False)
				if analisis_nombre_no_valido(v[i].nombre):
					v[i].nombre += '@'
					print('Nombre no Valido')
				else:
					print('Nombre Valido')
				if not ban:
					break

	if ban:
		print(f'No se encontro el nombre {param} en los registros')


def crear_archivo(fd, v, ):
	print(
		'Desea Crear Archivo, los datos almacenados anteriormente seran remplazados?')
	op = validar_intervalo(1, 2, '1. Si 2. No')
	if op == 1:
		a = float(input('Ingrese monto Minimo para generar el archivo!'))
		b = validar_mayor_que(a,
							  'Ingrese monto Maximo para generar el archivo!',
							  False)
		m = open(fd, 'wb')
		for i in range(len(v)):
			if v[i].tipopago == 0:
				if a < v[i].importe and v[i].importe < b:
					pickle.dump(v[i], m)
		m.close()
		print('Archivo Generado con exito!!!')
	else:
		print('No se genero Archivo')


def leer_archivo(fd):
	if os.path.exists(fd):
		print('Datos del archivo!: ')
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			to_string(a, False)
		m.close()


def menu(fd):
	sel = 1
	ban = ban2 = False
	while sel != 0:
		print('Menu de opciones Informacion Traslados\n'
			  '\n1. Cargar los datos de n registros ordenados de menor a mayor segun numero de id de los traslados'
			  '\n2. mostrar arreglo creado en el punto 1, a razon de una registro por linea'
			  '\n3. Buscar en el arreglo un nombre de cliente sea igual a nombre ingresado por teclado'
			  ' informar existencia si existe validar que el nombre sean solo '
			  'letras y espacios, en caso de no ser valido agregar un asterisco al final del nombre'
			  '\n4. crear un archivo de registros, con los traslados con forma de pago sea 0'
			  ' y su importe se encuentre en valores de a y b ingresados por teclado'
			  '\n5. mostrar el archivo creado a razon de un registro por linea'
			  '\n0. Salir')
		sel = validar_intervalo(0, 5)
		if sel == 1:
			n = validar_mayor_que(0, 'Ingrese cantidad de registros'
									 ' que quiera generar: ')
			v = carga(n)
			ban = True
		elif sel == 2:
			if ban:
				to_string(v)
			else:
				print('Primero genere registro!')
		elif sel == 3:
			if ban:
				param = input(
					'Ingrese el nombre que quiera buscar en el registro')
				busqueda_reg_nom(v, param)
			else:
				print('Primero genere registro')
		elif sel == 4:
			crear_archivo(fd, v)
		elif sel == 5:
			if os.path.exists(fd):
				leer_archivo(fd)
			else:
				print('Primero genere archivo!')
		else:
			print('Programa Cerrado')


def principal():
	print('\t\t\t\t\033[1;30;46m' '🔲 Parcial Recuperatorio 2020 🔲 \033[m')
	print('\t\t\t\t\t\tKibysz Alexander')
	print()
	fd = 'RegistroTraslados'
	menu(fd)


if __name__ == '__main__':
	principal()
