''''4. Agenda
Se solicita un programa que permita agendar contactos en un archivo.
De cada contacto se debe ingresar su nombre y apellido, mail y teléfono.

Se pide:

Cargar el archivo por teclado.
Mostrar el archivo.
Generar a partir del archivo un vector con todos los contactos.'''
from ej4reg import *
from ej4file import *


def validar(x, y, msg='Ingrese una opcion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('valor incorrecto elija un valor entre', x, 'o ', y)
	return num


def menu(fd):
	op = 1
	while op != -1:
		print(' 0. Crear Archivo Aleatorio \n1. Cargar el archivo por teclado. '
			  '\n2 2. Mostrar el archivo.\n3. Generar a partir del'
			  ' archivo un vector con todos los contactos.\n-1.Salir')
		op = validar(-1, 3)
		if op == 0:
			sel = validar(1, 2,
						  'Desea Crear un Nuevo Archivo?(los datos seran eliminados) (1.si 2.no): ')
			if sel == 1:
				x = int(input('Cuantos contactos quiere agendar?'))
				gen_file(x, fd)
			if sel == 2:
				continue
		elif op == 1:
			sel = validar(1, 2,
						  'Desea Crear un Nuevo Archivo?(los datos seran eliminados) (1.si 2.no): ')
			if sel == 1:
				x = int(input('Cuantos contactos quiere agendar?'))
				gen_file(x, fd, False)
		elif op == 2:
			mostrar_archivo(fd)
		elif op == 3:
			vector_from_file(fd)
		else:
			break


if __name__ == '__main__':
	fd = 'Contactos_Bin.dat'
	menu(fd)
