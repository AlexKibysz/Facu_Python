import pickle
import os
from simp4reg import *


def grabar_arvchivo(v, fd):
	x=float(input('Ingrese monto minimo: '))
	tipos=(3,4,5)
	m = open(fd, 'wb')
	for i in range(len(v)):
		if v[i].tipo in tipos and v[i].importe > x:
			pickle.dump(v[i], m)
	m.close()


def mostrar_archivo(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell()<os.path.getsize(fd):
			a=pickle.load(m)
			to_string(a)
		m.close()
	else:
		print('Tiene que generar un archivo primero')
