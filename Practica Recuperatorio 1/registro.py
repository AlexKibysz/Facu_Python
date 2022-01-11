from random import *

class Inventario:
	def __init__(self, id, nom, pais, precio):
		self.id = id
		self.nom = nom
		self.pais = pais
		self.precio = precio


def gen_name():
	nombre = ''
	sec1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	for i in range(4):
		nombre += choice(sec1)
	return nombre


def carga(n):
	v = [None] * n
	for i in range(n):
		id = randint(1, 1000)
		nom = gen_name()
		pais = randint(0, 49)
		precio = round(uniform(1000, 10000000), 2)
		v[i] = Inventario(id, nom, pais, precio)
	return v


def ordenar_dni(v):
	menor = v[0].id
	mayor = None
	for i in range(len(v) - 1):
		for j in range(i + 1, len(v)):
			if v[i].id > v[j].id:
				v[i].id, v[j].id = v[j].id, v[i].id

	# ayor  #menor
	to_string(v)
	return v


def busqueda_reg(v, param):
	for i in range(len(v)):
		if v[i].nom == param:
			print('Se encontro el nombre buscado!')
			to_string(v[i], False)
			break


def to_string(v, all=True):
	if all:
		for i in range(len(v)):
			print('ID {0} Nombre {1} Pais {2} Precio {3}'.format(v[i].id,
																 v[i].nom,
																 v[i].pais,
																 v[i].precio))
	else:
		print('ID {0} Nombre {1} Pais {2} Precio {3}'.format(v.id, v.nom,
															 v.pais,
															 v.precio))


def v_cont(v):
	cont = [0] * 50
	for i in range(len(v)):
		cont[v[i].pais] += 1
	for j in range(len(cont)):
		if cont[j]!=0:
			print('Pais {} Cantidad {}'.format(j,cont[j] ))
	return cont
