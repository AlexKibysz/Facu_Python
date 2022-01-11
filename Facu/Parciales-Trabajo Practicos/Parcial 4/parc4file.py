from parc4reg import *
import pickle
import os

#crea el archivo por medio de registro
def crear_archivo(fd, v):
	m = open(fd, 'wb')
	for i in range(len(v)):
		pickle.dump(v[i], m)
	m.close()
	print('Archivo Generado con Exito!')

#muestra los archivos segun parametros
def mostrar_arch_param(fd):
	ph = [3, 1, 5]
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			if a.ph in ph:
				to_string(a)
		m.close()
	else:
		print('No se encontro Archivo, por favor generelo! (┬┬﹏┬┬).')
