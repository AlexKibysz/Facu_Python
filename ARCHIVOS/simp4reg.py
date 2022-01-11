#Dni (entero
#Nombre (cadena
#importe paga(float)
#tipo afiliacion (0,4 0: vitalicio, 1: transitorio, 2: indirecto, etc)
#tipo trabajo 0 al 14
from random import *
class Profesionales:
	def __init__(self,dni,nombre,importe,afiliacion,tipo):
		self.dni=dni
		self.nombre=nombre
		self.importe=importe
		self.afiliacion=afiliacion
		self.tipo=tipo

def to_string(a):
	p='{0:<10}{1:<10}'.format('Dni: ', a.dni)
	p+='{0:<10}{1:<10}'.format('Nombre: ', a.nombre)
	p+='{0:<10}{1:<10}'.format('Importe: ', a.importe)
	p+='{0:<10}{1:<10}'.format('Afiliacion: ', a.afiliacion)
	p+='{0:<10}{1:<10}'.format('tipo: ', a.tipo)
	print(p)

def add_in_order_bin(v,nuevo):
	n = len(v)
	pos = n
	i , d= 0, n-1
	while i<=d:
		c=(i+d)//2
		if v[c].dni == nuevo.dni:
			pos=c
		elif nuevo.dni < v[c].dni:
			d = c-1
		else:
			i = c + 1
	if i>d:
		pos=i
		v[pos:pos]=[nuevo]

def random_name():
	n1=['A','B','C']
	n2=['1','2','3']
	n3=['AZUL','NEGRO','BLANCO']
	n4=['CECH','PEPE','MAICOL']
	nombre=str(choice(n1))+str(choice(n2))+str(choice(n3))+str(choice(n4))
	return nombre

def generar_reg(n):
	v = []
	for i in range(n):
		dni = randint(50000000,70000000)
		nombre =random_name()
		importe = round(uniform(100,8000),2)
		afiliacion = randint(0,4)
		tipo = randint(0,14)
		nuevo = Profesionales(dni,nombre,importe,afiliacion,tipo)
		add_in_order_bin(v,nuevo)
	return v

def search_in_reg(v):
	nom = input('Ingrese nombre a buscar: ')
	for i in range(len(v)):
		x=v[i].nombre
		if x==nom:
			to_string(v[i])
			break

def mostrar_reg(v):
	for i in range(len(v)):
		to_string(v[i])
