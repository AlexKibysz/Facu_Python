# 9. se pide guardar el nombre y dni,
# monto del alquiler y
# un código entre 0 y 9 que indica el tipo de cabaña
# alquilada (suponiendo que por ejemplo, el 0 indica que se alquiló una
# cabaña de tipo Común, el 1 Premiun, el 2 Super Premiun, y así hasta el código 9).

# 1. Cargar el arreglo de alquileres. Validar que el código de tipo de
# cabaña esté efectivamente entre 0 y 9. (no realizar otra validación más que
# la solicitada).

# 2. Determinar la cantidad de alquileres que registraron un monto mayor a x,
# siendo x un valor pasado por parámetro.

# 3. Determinar y mostrar el monto total recaudado por cada tipo de cabaña
# posible (un acumulador que indique el monto total recaudado por el alquiler
# de las cabañas de tipo 0, otro para las cabañas de tipo 1, etc.).

# 4.Mostrar los datos de todos los alquileres en orden de mayor a menor por
# el dni de las personas que realizaron la reserva.

# 5 Mostrar un informe con todos los alquileres que registraron el menor monto
# (note que podría haber más de un alquiler con el mismo monto menor).
from random import *


class Cliente:
	def __init__(self, nombre, documento, monto, tipo_cabania):
		self.nombre = nombre
		self.documento = documento
		self.monto = monto
		self.tipo_cabania = tipo_cabania


def validar_entre(x, y, msg='ingrese codigo de habitacion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('Error', msg)
	return num


def name_selector():
	Nm1 = ['rosa', 'armando', 'Alan', 'Alba', 'Naruto', 'Tobi', 'Pepe',
		   'Monica', 'Susana', 'Chicken', 'Hamburgeso']
	Nm2 = ['melano', 'Britos', 'Paredes', 'Sura', 'Torio', 'Inca', 'kentuky',
		   'King', 'Lopez', 'Correa']
	nombre = choice(Nm1).upper() + ' ' + choice(Nm2).upper()
	return nombre


def carga(v, Manual=True):
	if Manual:
		for i in range(len(v)):
			nombre = input('ingrese nombre')
			dni = int(input('ingrese dni del cliente: '))
			monto = int(input('ingrese monto de la cabania'))
			tipo_caba = validar_entre(0, 9, 'ingrese tipo de cabania: ')
			v[i] = Cliente(nombre, dni, monto, tipo_caba)
	else:
		for i in range(len(v)):
			nombre = name_selector()
			dni = randint(43000000, 45000000)
			monto = randint(100, 10000)
			tipo_caba = randint(0, 9)
			v[i] = Cliente(nombre, dni, monto, tipo_caba)


def write(v, elm=True):
	if elm:
		print('{0:<20}{1:^8}{2:^10}{3:^16}'.format(v.nombre, v.documento,
												v.monto,

												v.tipo_cabania))

	else:
		print('{0:20}{1:8}{2:10}{3:16}'.format('Nombre', 'Dni', 'Monto',
												'Tipo de cabaña'))
		for i in range(len(v)):
			print('{0:<20}{1:^8}{2:^10}{3:^16}'.format(v[i].nombre, v[i].documento, v[i].monto, v[i].tipo_cabania))



def validar_mayores(v, x, may=True):
	if may:
		nhay=True
		print('{0:20}{1:8}{2:10}{3:16}'.format('Nombre', 'Dni', 'Monto',
												'Tipo de cabaña'))
		for i in range(len(v)):
			if v[i].monto > x:
				nhay=False
				write(v[i], True)
		if nhay:
			print('No se encontraron valores')
	else:
		nhay=True
		print('{0:20}{1:8}{2:10}{3:16}'.format('Nombre', 'Dni', 'Monto',
												'Tipo de cabaña'))
		for i in range(len(v)):
			if v[i].monto < x:
				nhay=False
				write(v[i], True)
		if nhay:
			print('No se encontraron valores')

def contador_tipo(v):
	v_cont = [0] * 10
	for i in range(len(v)):
		x=v[i].tipo_cabania
		v_cont[x]+=v[i].monto
	return v_cont


def ordenamiento(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].documento < v[j].documento:
				v[i], v[j] = v[j], v[i]
	return v


def menu(v):
	opcion = 1
	while opcion >= 0:
		print('1. Cargar el arreglo de alquileres\n2.'
			  ' Determinar la cantidad de alquileres que registraron '
			  'un monto mayor a x\n3. Determinar y mostrar el monto total '
			  'recaudado por cada tipo de cabaña posible\n4. Mostrar los datos '
			  'de todos los alquileres en orden de mayor a menor por dni\n5.'
			  ' Mostrar un informe con todos los alquileres que '
			  'registraron el menor monto\n0. pa sali')
		print('')
		b=False
		opcion = validar_entre(0, 5, 'Ingrese su seleccion: ')
		if opcion == 1:
			b=True
			carga(v, False)
			write(v, False)
		if opcion == 2:
			if b==False:
				print('Ingrese registros: ')
				continue
			else:
				x = float(input('Ingrese valor para buscar '
								'alquileres con monto mayor a este: '))
				validar_mayores(v, x)
		if opcion == 3:
			if b==False:
				print('Ingrese registros: ')
				continue
			else:
				v_cont=contador_tipo(v)
				for i in range(len(v_cont)):
					print(i,'---->monto: ', v_cont[i])
		if opcion == 4:
			if b==False:
				print('Ingrese registros: ')
				continue
			else:
				ordenamiento(v)
				write(v, False)
		if opcion == 5:
			if b==False:
				print('Ingrese registros: ')
				continue
			else:
				x = float(input('Ingrese valor para buscar '
								'alquileres con monto menor a este: '))
				validar_mayores(v, x, False)
		if opcion == 0:
			break


def principal():
	n = int(input('Ingrese cantidad de arreglos: '))
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
