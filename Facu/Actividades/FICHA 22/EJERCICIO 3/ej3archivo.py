from ej3registro import *
import pickle
import os
from random import *


def mostrar_archivo(fd):
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		to_string(a)
	m.close()


def agregar(fd):
	n = int(input('Cuantos nuevos Cobros desea generar'))
	m = open(fd, 'ab')
	for i in range(n):
		dia = int(input('Ingrese dia: '))
		monto = int(input('Ingrese monto: '))
		serv = int(input('Ingrese servicio: '))
		cuenta = int(input('Ingrese cuenta: '))
		nuevo = Cobros(dia, monto, serv, cuenta)
		pickle.dump(nuevo, m)
	m.close()

def generar(x):
	if x == 's':
		fd = 'COBROS_BIN.dat'
		n = int(input('Ingrese cantidad de Registros que Quiera Generar: '))
		crear_auto(fd, n)
		mostrar_archivo(fd)
		print('ARCHIVO GENERADO')

def crear_auto(fd, n):
	m = open(fd, 'wb')
	for i in range(n):
		dia = randint(1, 31)
		monto = round(uniform(100, 600), 2)
		serv = randint(1, 15)
		cuenta = randint(100, 999)
		nuevo = Cobros(dia, monto, serv, cuenta)
		pickle.dump(nuevo, m)
	m.close()

