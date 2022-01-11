# numero de socio
# deporte
# día del mes en que pagó
# valor de la cuota
# Si el socio aún no abonó
# el día del mes debe ser 0

from ej6 import *
from ej6reg import *
import pickle
from random import *
import os


def build_file(fd, n):
	v = [None] * n
	m = open(fd, 'wb')
	for i in range(n):
		ind = i
		id = randint(1000, 9999)
		deporte = randint(0, 4)
		dia = randint(1, 31)
		cuota = randint(0, 1)
		pago = round(uniform(1000, 5000))
		v[i] = Asosiados(ind, id, deporte, dia, cuota, pago)
		pickle.dump(v[i], m)
	m.close()
	return v


def reg_from_file(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			to_string(a)
		m.close()
	else:
		print('Primero Tiene que Crear el archivo')


def build_file_param(fd2, v, param=0):
	m = open(fd2, 'wb')
	for i in range(len(v)):
		if v[i].cuota == param:
			pickle.dump(v[i], m)

	m.close()


def file_search(fd, param1, param2):
	ban = False
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			if a.id == param1 and float(a.pago) == param2:
				ban = True
				dia = validar(1, 31,
							  'Ingrese el dia en que se cobro al socio: ')
				pago = float(input('Ingrese el monto que se cobro: '))
				print('Se encontro al/los socios: ')
				to_string(a)
		m.close()
		m=open(fd,'ab')
		Asosiados(a.ind, param1, a.deporte, dia, a.cuota, pago)
		if ban == False:
			dia = validar(1, 31,
						  'Ingrese el dia en que se cobro al socio: ')
			cuota = validar(0, 1, 'Ingrese Cuota del socio: ')
			pago = float(input('Ingrese el monto que se cobro: '))
			nuevo = Asosiados(param1, param2, dia, cuota, pago)
			pickle.dump(nuevo, m)
		else:
			nuevo=Asosiados(a.ind, param1, a.deporte, dia, a.cuota, pago)
			pickle.dump(nuevo, m)
		m.close()
	else:
		print('Primero Tiene que Crear el archivo')


def mostrar_archivo(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			to_string(a)
		m.close()
	else:
		print('Primero Tiene que Crear el archivo')


# ((0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin))
def deporte_conv(x):
	if x == 0:
		return 'Natacion'
	if x == 1:
		return 'Basquet'
	if x == 2:
		return 'Karate'
	if x == 3:
		return 'Futbol'
	if x == 4:
		return 'Patin'
