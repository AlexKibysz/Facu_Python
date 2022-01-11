import pickle
import os
class Cobros:   #cambiar segun datos del archivo
	def __init__(self, dia, monto, serv, cuenta):
		self.dia = dia
		self.monto = monto
		self.serv = serv
		self.cuenta = cuenta



def to_string(a):
	m = '{0:<6}{1:^4}'.format('Valor1: ', a.dia)
	m += '{0:<8}{1:^5}'.format('Valor2: ', a.monto)
	m += '{0:<8}{1:^6}'.format('Valor3: ', a.serv)
	m += '{0:<}{1:^}'.format('Valor4: ', a.cuenta)
	print(m)


def mostrar_archivo(fd):
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		to_string(a)


def principal(fd):
	  #cambiar nombre segun archivo
	mostrar_archivo(fd)


if __name__ == '__main__':
	fd = 'COBROS_BIN.dat'
	principal(fd)
