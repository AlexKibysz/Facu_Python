from random import *
import pickle
import os


class Inscriptos:
	def __init__(self, dni, nom, titulo, tipo, monto):
		self.dni = dni
		self.nom = nom
		self.titulo = titulo
		self.tipo = tipo
		self.monto = monto


def gen_nom():
	sec1 = ['Juan', 'Pedro', 'Pablo', 'Lucas', 'Simon', 'Pepe', 'Jere',
			'Tobias', 'Nicolas']
	sec2 = ['Ki', 'Ca', 'De', 'Usu', 'As', 'Yu', 'Yao']
	sec3 = ['ming', 'bysz', 'bisky', 'maki', 'pez', 'rales']
	nombre = choice(sec1)
	nombre += ' '
	nombre += choice(sec2) + choice(sec3)
	return nombre


def titulo_carac():
	sec1 = ['Informatica', 'Ciencia', 'Social', 'Medicina', 'Biomecanica',
			'Marketing']
	tit = choice(sec1)
	return tit


def verificar_mayor_cero():
	n = 0
	while n == 0:
		n = int(input('Ingrese cantidad: '))
		if n == 0:
			print('El valor tiene que ser mayor a 0!')
	return n


def ordenar_dni(v):
	for i in range(len(v) - 1):
		for j in range(i + 1, len(v)):
			if v[i].dni > v[j].dni:
				v[i].dni, v[j].dni = v[j].dni, v[i].dni
	to_string(v)
	return v


def to_string(v, all=True):
	if all:
		for i in range(len(v)):
			print(f'Dni: {v[i].dni} Nombre: {v[i].nom} Titulo {v[i].titulo}'
				  f' Tipo: {v[i].tipo} Monto: {v[i].monto}')
	else:
		print(f'Dni: {v.dni} Nombre: {v.nom} Titulo {v.titulo}'
			  f' Tipo: {v.tipo} Monto: {v.monto}')


def carga(n):
	v = [None] * n
	for i in range(n):
		dni = randint(1000000000, 9999999999)
		nom = gen_nom()
		titulo = titulo_carac()
		num = randint(0, 29)
		monto = round(uniform(1000, 20000), 2)
		v[i] = Inscriptos(dni, nom, titulo, num, monto)
	return v


def crear_arch(fd, v, param):
	m = open(fd, 'wb')
	for i in range(len(v)):
		if v[i].monto < param:
			pickle.dump(v[i],m)
	print('Archivo Generado con exito!')
	m.close()


def buscar_reg_nom(v, param):
	ban=True
	for i in range(len(v)):
		if v[i].nom == param:
			ban=False
			print('Se encontro nombre en el registro: ')
			to_string(v[i], False)
			break
	if ban:
		print('No se encontro nombre en el arreglo')


def leer_arch(fd):
	if os.path.exists(fd):
		m = open(fd, 'rb')
		while m.tell() < os.path.getsize(fd):
			a = pickle.load(m)
			to_string(a, False)
		m.close()
	else:
		print('Primero tiene que generar archivo!')


def vec_cont_curso(v):
	cont = [0] * 30
	for i in range(len(v)):
		cont[v[i].tipo] += 1
	for c in range(len(cont)):
		if cont[c] != 0:
			print(f'Tipo de Curso: {c} Cant de inscriptos: {cont[c]}')


def analizar_texto_no_letras(texto):
	texto = texto.lower()
	letras = 'qwertyuiopasdfghjklzxcvbnm'
	cont = 0
	con2=0
	jump=' .'
	for c in texto:
		if c not in letras:
			cont += 1
		if c in jump:
			con2+=1
	print(f'La cantidad de caracteres que no eran letras son: {cont} contando los espacios\n'
		  f'y sin contar los espacios {cont-con2}')

def verificar_intervalo(x, y, msg='Ingrese su seleccion'):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print(f'Ingrese valor entre {x} y {y}')
	return num
