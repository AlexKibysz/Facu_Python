'''
2. Cabañas
Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar la información referida a los n alquileres de la temporada estival en un arreglo de registros (cargar n por teclado).

Por cada alquiler, se pide guardar el DNI de la persona que hizo la reserva, monto del alquiler y un código entre 0 y 9 que indica el tipo de cabaña alquilada.

Se pide desarrollar un programa en Python que permita:

Cargar el arreglo pedido (validar tipo de cabaña).
Trasladar a un archivo los alquileres que registraron un monto mayor a x, siendo x un valor pasado por parámetro.
Usando los datos del archivo, determinar y mostrar el monto total recaudado por cada tipo de cabaña posible.


datos = dni, monto, codigo(0,9)

1. cargar arreglo pedido de n se;ores
2. mostrar los datos que tengan monto mayor a x
3. mostrar el total recaudado por cada codigo
'''

import pickle
import os
from random import *


class Registro:
	def __init__(self, dni, monto, cod):
		self.dni = dni
		self.monto = monto
		self.cod = cod


def carga(fd, v, x):
	m = open(fd, 'wb')
	for i in range(len(v)):
		dni = randint(50000000, 90000000)
		monto = round(uniform(1000, 4500), 2)
		cod = randint(0, 9)
		v[i] = Registro(dni, monto, cod)
		if monto > x:
			pickle.dump(v[i], m)
	m.close()


def to_string(a):
	m = '{0:<4}{1:^10}'.format('Dni: ', a.dni)
	m += str('{0:<6}{1:^10}'.format('Monto: ', a.monto))
	m += '{0:<7}{1:^4}'.format('Codigo: ', a.cod)
	print(m)


def mostrar(fd):
	if os.path.exists(fd):
		size = os.path.getsize(fd)
		m = open(fd, 'rb')
		while m.tell() < size:
			a = pickle.load(m)
			to_string(a)
		m.close()


def recaudacion(fd, v2):
	if os.path.exists(fd):
		size = os.path.getsize(fd)
		m = open(fd, 'rb')
		while m.tell() < size:
			a = pickle.load(m)
			v2[a.cod] += a.monto
		return v2
		m.close()


def mostrar_cont(v):
	for i in range(len(v)):
		m = '{0:<6}{1:^10}{2:<2}'.format(f'Codigo {i} :', str(v[i]), '$')
		print(m)


def menu():
	op = 1
	print('1. Cargar el arreglo pedido (validar tipo de cabaña)'
		  '\n 2. Mostrar los datos que tengan monto mayor a x'
		  '\n 3. Mostrar el total recaudado por cada codigo')
	while op != -1:
		op = int(input('Ingrese su opcion: '))
		if op == 1:
			fd = 'Temporada.dat'
			n = int(input('Ingrese cuantos registros quiere genera: '))
			v = [0] * n
			print('Listo! puede continuar')
		elif op == 2:
			x = float(input('Ingrese monto a seleccionar: '))
			carga(fd, v, x)
			mostrar(fd)
		elif op == 3:
			v2 = [0] * 10
			v2 = recaudacion(fd, v2)
			mostrar_cont(v2)
		else:
			'Termino el programa'

if __name__ == '__main__':
	menu()
