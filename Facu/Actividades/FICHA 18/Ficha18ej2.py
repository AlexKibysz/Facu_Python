# 2. Analizando Temperaturas
# El Servicio Metereológico Nacional solicitó un programa que mediante un menu
# de opciones, permita analizar las amplitudes térmicas desde diferentes puntos
# de vista, para ello las opciones a las que el programa debe responder son:


# Cargar n analisis térmicos (n ingresado por el usuario), cuyos datos son:

# región,
# mes (numero del 1 al 12),
# temperatura máxima,
# temperatura mínima.

# informar la temperatura máxima promedio en el primer semestre
# informar la región y el mes en que se registró la menor mínima del año
# Salir
from random import *


class Termicas:
	def __init__(self, region, mes, temperatura_max, temperatura_min):
		self.region = region
		self.mes = mes
		self.temperatura_max = temperatura_max
		self.temperatura_min = temperatura_min


def carga(v):
	for i in range(len(v)):
		region = input('ingrese region: ')
		mes = int(input('ingrese mes (1 al 12): '))
		temp_max = int(input('ingrese temperatura maxima: '))
		temp_min = int(input('ingrese temperatura minima: '))
		v[i] = Termicas(region, mes, temp_max, temp_min)


def ordenar_mes(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].mes > v[j].mes:
				v[i], v[j] = v[j], v[i]


def mostrar_mes_temp_min(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].temperatura_min > v[j].temperatura_min:
				v[i], v[j] = v[j], v[i]
	return print(v[0].mes)


def promedio(v):
	n = len(v)
	suma = 0
	for i in range(n):
		suma += v[i].temperatura_max
	return suma / n


def write(v):
	for i in range(len(v)):
		print('ragion: ', v[i].region, 'mes: ', v[i].mes,
			  'temperatura_maxima: ',
			  v[i].temperatura_max, 'temperatura_minima: ',
			  v[i].temperatura_min)


def seleccion1():
	x = int(input('ingrese cantidad que quiere ingresar'))
	v = [None] * x
	carga(v)
	write(v)
	return v


def seleccion2(v):
	ordenar_mes(v)
	suma = cant = 0
	for i in range(len(v)):
		if v[i].mes < 7:
			cant += 1
			suma += v[i].temperatura_max
	return suma / cant


def mostrar_region_temp(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].temperatura_min > v[j].temperatura_min:
				v[i], v[j] = v[j], v[i]
	return print(v[0].region)


def menu():
	opcion1 = False
	seleccion = None
	while seleccion != -1:
		print(
			'opcion 1. Cargar n analisis térmicos (n ingresado por el usuario)')
		print(
			'opcion 2. informar la temperatura máxima promedio en el primer semestre')
		print(
			'opcion 3. informar la región y el mes en que se registró la menor mínima del año')
		print('opcion -1. Salir')
		print('*-'*100)
		seleccion = int(input('ingrese seleccion: '))
		if seleccion == 1:
			print('*-'*100)
			v = seleccion1()
			opcion1 = True
		if seleccion == 2 and opcion1:
			print('*-'*100)
			sumatoria = seleccion2(v)
			print(sumatoria)
		if seleccion == 3 and opcion1:
			print('*-'*100)
			mostrar_mes_temp_min(v)
			mostrar_region_temp(v)
		if seleccion == 4:
			exit


def principal():
	menu()


if __name__ == '__main__':
	principal()
