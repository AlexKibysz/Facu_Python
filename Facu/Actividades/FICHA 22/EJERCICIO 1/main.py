import os.path
import pickle
from random import *


def generar(fd):
	m = open(fd, 'wb')
	v = [0] * 6
	for f in range(6):
		x = randint(1, 36)
		v[f] = x
		pickle.dump(x, m)
	return v


def mostrar(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		for i in range(6):
			x = pickle.load(m)
			print(x)
	else:
		print('No existe')


def principal():
	fd = 'extracto.dat'
	v = generar(fd)
	print()
	mostrar(fd)


if __name__ == '__main__':
	principal()
