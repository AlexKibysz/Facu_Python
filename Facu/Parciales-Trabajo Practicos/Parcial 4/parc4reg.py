#volumen agua (float)
#nivel PH(1,10)
#conductividad electrica(1,5)
#codigo solu(int)
from random import *
class Riegos:
	def __init__(self,vol,ph,conduct,cod):
		self.vol=vol
		self.ph=ph
		self.conduct=conduct
		self.cod=cod

def to_string(a):
	p='{0:<10}{1:<20}'.format('Volumen: ', a.vol)
	p+='{0:<10}{1:<5}'.format('Nivel PH: ', a.ph)
	p+='{0:<30}{1:<5}'.format('Conductividad Electrica: ', a.conduct)
	p+='{0:<10}{1:<20}'.format('Codigo Solucion: ', a.cod)
	print(p)

def mostrar_reg(v):
	for i in range(len(v)):
		to_string(v[i])


def add_in_order_bin(v, val):
	n=len(v)
	pos=n
	i,d=0,n-1
	while i<=d:
		c=(i+d)//2
		if v[c].cod==val.cod:
			pos=c
		if val.cod>v[c].cod:
			i=c+1
		else:
			d=c-1
	if i>d:
		pos=i
	v[pos:pos]=[val]


# Ingresar desde teclado un nivel de PH y mostrar los datos del primer registro que encuentre que tenga ese nivel de PH.
# Si no lo encuentra mostrar un mensaje. La búsqueda debe finalizarse inmediatamente si se encuentra un registro.

def search_reg_param(v,param):
	ban=True
	for i in range(len(v)):
		if v[i].ph==param:
			ban=False
			to_string(v[i])
			break
	if ban:
		print(f'No se encontro datos con el ph {param}')


def carga(n):
	v=[]
	for i in range(n):
		vol=round(uniform(100,1000),2)
		ph=randint(1,10)
		conduct=randint(1,5)
		codigo=randint(1000,5000)
		val=Riegos(vol,ph,conduct,codigo)
		add_in_order_bin(v,val)
	return v
