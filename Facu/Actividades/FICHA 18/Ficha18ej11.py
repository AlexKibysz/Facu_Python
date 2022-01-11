# usuarios

# 11. Usuarios
# Nos solicitaron un software para registrar los usuarios que acceden un
# determinado software.

# Cada usuario registrado debe contener un código identificatorio,
#
# un nombre de usuario, un password (que debe ser igual 4 caracteres y no ser mayor de 10 caracteres),
#
# el departamento al que pertenece el usuario (número entre 0 y 19)

# Se pide:

# 1 -Generar las estructuras correspondientes para se registren los usuarios en un array de Registros.

# Controlar que el password cumpla con los requerimientos antes mencionados al igual que el departamento.

# 2 - Listar los usuarios, omitiendo el password.

# 3 - Contar y mostrar cuantos usuarios hay por departamento.

# 4 - Modificar el password de un usuario.
from random import *


class Usuario:
	def __init__(self, nombre, password, departamento):
		self.nombre = nombre
		self.password = password
		self.departamento = departamento


def name_selector():
	Nm1 = ['rosa', 'armando', 'Alan', 'Alba', 'Naruto', 'Tobi', 'Pepe',
		   'Monica', 'Susana', 'Chicken', 'Hamburgeso']
	Nm2 = ['melano', 'Britos', 'Paredes', 'Sura', 'Torio', 'Inca', 'kentuky',
		   'King', 'Lopez', 'Correa']
	nombre = choice(Nm1).upper() + ' ' + choice(Nm2).upper()
	return nombre


def password_generator(inicial, final):
	x = choice(range(inicial, final))
	password = 0
	carac = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v',
			 'b', 'n', 'm', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
			 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
			 'B', 'N', 'M', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I',
			 'O', 'P', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	for i in range(x):
		if i == 0:
			password = choice(carac)
		password += choice(carac)
	return password


def carga(v):
	for i in range(len(v)):
		nombre = name_selector()
		password = password_generator(1, 100)
		departamento = randint(0, 19)
		v[i] = Usuario(nombre, password, departamento)


def write(v, List=True, Pass=True):
	if List and Pass:
		print('{0:20}{1:^10}{2:>3}'.format('Nombre ', 'Password ',
										   'departamento '))
		for i in range(len(v)):
			print(
				'{0:20}{1:^10}{2:>3}'.format(v[i].nombre, v[i].password,
											 v[i].departamento))
	elif List:
		print('{0:18}{1:3}'.format('Nombre ', 'departamento '))
		for i in range(len(v)):
			print('{0:18}{1:3}'.format(v[i].nombre, v[i].departamento))
	if List == False:
		print('{}{}{}'.format(v.nombre, v.password, v.departamento))


def contador_dep(v):
	v2 = [0] * 20
	for i in range(len(v)):
		if v[i].departamento != None:
			x = v[i].departamento
			v2[x] += 1
	return v2


def menu(v):
	opcion = 1
	while opcion > 0:
		print(
			'Menu\n1. Generar las estructuras correspondientes para se registren los usuarios en un array de Registros'
			'\n2. Listar los usuarios, omitiendo el password.\n3.  Contar y mostrar cuantos usuarios hay por departamento'
			'\n4. Modificar el password de un usuario\n 0. Salir')
		opcion = int(input('ingrese su seleccion: '))
		if opcion == 1:
			carga(v)
			write(v)
		if opcion == 2:
			write(v, True, False)
		if opcion == 3:
			v2 = contador_dep(v)
			for i in range(len(v2)):
				print(i, '--->', v2[i])
		if opcion == 4:
			n = len(v)
			selecion_cambiar = int(
				input(f'Ingrese cual de las {n} quiere cambiar: '))
			v[selecion_cambiar].password = input('ingrese nueva contraseña')
			write(v[selecion_cambiar], False, False)
			wres=int(input('desea mostrar de nuevo la lista(1.si 2.no)?: '))
			if wres==1:
				write(v)
			else:
				continue

			if opcion == 0:
				break


def principal():
	n = int(input('Ingrese cantidad de registros que desea generar: '))
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
