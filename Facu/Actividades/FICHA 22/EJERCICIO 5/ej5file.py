from ej5reg import *
from random import *
import pickle
import os


def generar_file(n, fd):
	m = open(fd, 'wb')
	v = [None]*n
	for i in range(n):
		nombre = ('GamesOfThrones', 'MrRobot', 'SiliconValley', 'Elpepelaserie',
				  'ETESECH la serie', 'naruto', 'boruto',
				  'maicolmamaguevaso la serie',
				  'The Ofiice', 'Zack y Cody', 'Gemelos a Bordo', 'Sailor Moon',
				  'Los guerreros shaolin',
				  'DBZ', 'DBZ KAKAROTO', 'DBZ TENKAICHI', 'DBZ REVOLUTION',
				  'SINC', 'TERMINAITOR', 'SpiderMan1999', 'Ultimate Spider Man',
				  'El Azombroso Hombre Araña', 'Backyorgidans',
				  'Barnie el Dinosaurio', 'PepaPig',
				  'ESSESS', 'SOPA', 'INTERNET', 'PIPIPIPIPI', 'El Chavo Del 8')
		nombres = choice(nombre)
		genero = randint(0, 5)
		idioma = randint(0, 4)
		temporada = randint(1, 8)
		duracion = randint(0, 500)
		nuevo = SeriesR(nombres, genero, idioma, temporada, duracion)
		for i in range(n):
			v[i]=nuevo
		pickle.dump(v[n], m)
	m.close()
	return v


def generar_file_param(fd, idioma):
	fd2 = 'Series' + str(idioma) + '.dat'
	arch = open(fd2, 'wb')
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		if a.temporada > 1 and convertir_idioma(a.idioma) == idioma:
			pickle.dump(a, arch)
	m.close()
	arch.close()
	mostrar_archivo(fd2)


def search_file_param(fd, param):
	ban = True
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		if a.nombre == param:
			to_string(a)
			ban = False
	m.close()
	if ban:
		print('No se encontro la serie')


def sum_param_file(fd, idioma):
	v = [0] * 6
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		if convertir_idioma(a.idioma) == idioma:
			v[a.genero] += a.duracion
	m.close()
	for i in range(len(v)):
		print(
			'{0:<10}{1:17}{2:>6}{3:<4}'.format('Genero: ', convertir_genero(i),
											   v[i], 'min'))


def generar_matriz(fd):
	matriz=[[0]*6 for f in range(5)]
	m=open(fd,'rb')
	while m.tell()<os.path.getsize(fd):
		a=pickle.load(m)
		x=a.genero
		y=a.idioma
		matriz[a.idioma][a.genero]+=1
	m.close()
	return matriz


def mostrar_matriz(matriz):
	for i in range(len(matriz)):
		for c in range(len(matriz[0])):
			if matriz[i][c]!=0:
				p='{0:<10}{1:<10}'.format('Idioma: ',convertir_idioma(i))
				p+='{0:<10}{1:<10}'.format('Genero: ',convertir_genero(c))
				p+='{0:<10}{1:<10}'.format('Cantidad: ',matriz[i][c])
				print(p)
		print()

def mostrar_archivo(fd):
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		to_string(a)
	m.close()
