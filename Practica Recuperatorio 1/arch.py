import pickle
import os
from registro import *

def crear_arch(fd, v):
	m = open(fd, 'wb')
	for i in range(len(v)):
		if v[i].pais != 2:
			pickle.dump(v[i], m)
	m.close()
	print('Archivo generado!')


def leer_archivo(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			to_string(a, False)
		m.close()
	else:
		print('Primero debe generar el archivo')
