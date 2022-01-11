'''3. Rapipago
Una empresa de pagos de servicios necesita un programa que permita llevar los cobros que ha realizado, para ello marco como muy importante que los datos no se pierdan. De un cobro se sabe el dia en que se cobró, el tipo de servicio (un valor de 1 a 15), el monto cobrado y el número de cuenta asociada a la persona que pagó dicho servicio.

Se desea manejar la siguiente lógica a través de un menú de opciones que cumpla:

Agregar un nuevo cobro al archivo de cobros.
Determinar el monto total para un número de cuenta X pasado por parámetro
Indicar el monto total acumulado para cada servicio, en el día del mes que se lo cobro (matriz de acumulación)
Indicar, a partir de la matriz, el día con mayor monto cobrado
Indicar, a partir de la matriz, el promedio cobrado para el servicio X pasado por parámetro


dia en que se cobró
el tipo de servicio(1,15)
el monto cobrado
número de cuenta

1.Agregar un nuevo cobro al archivo de cobros.

2.Determinar el monto total para un número de cuenta X pasado por parámetro

3.Indicar el monto total acumulado para cada servicio, en el día del mes que se lo cobro (matriz de acumulación)

4.Indicar, a partir de la matriz, el día con mayor monto cobrado

5.Indicar, a partir de la matriz, el promedio cobrado para el servicio X pasado por parámetro
'''
import pickle
import os
from random import *
from ej3archivo import *
from ej3registro import *



def mostrar_mayor(matrix):
	valor = 0
	mayor = 0
	for c in range(len(matrix[0])):
		for f in range(len(matrix)):
			valor += matrix[f][c]
			if valor > mayor:
				pos1 = c
				mayor = valor
		valor = 0
	print(f'El dia que mas se cobro fue en el dia {pos1}, con {mayor} cobros')


def mostrar_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j], end=" ")
		print()


def buscar_matriz(matriz, serv):
	cont = 0
	total = 0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			total += matriz[f][c]
			cont += matriz[serv][c]
	prom = cont / total
	print(f'El promedio del servicio respecto al total es de {prom}')







def sum_param_file(fd, x):
	cont = 0
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		cobro = pickle.load(m)
		if cobro.cuenta == x:
			cont += cobro.monto
	print(f'EL total cobrado en la cuenta {x} es de: {cont}')


def crear_matriz(fd):
	matriz = [[0] * 31 for i in range(1,16)]
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		matriz[a.serv-1][a.dia-1]+=1
	mostrar_matrix(matriz)
	return matriz


def totalizar_dia(c,m):
	cont=0
	for f in range(len(m)):
		cont+=m[f][c]
	return cont



def sum_col(matriz):
	mayor=totalizar_dia(0,matriz)
	for c in range(1, len(matriz[0])):
		total=totalizar_dia(c,matriz)
		if total>mayor:
			mayor=total
			dia=c
	print(f'El mayor monto juntado fue en el dia {dia} con un total de : {mayor}')



def promedio_param(matriz, serv):
	cont1=0
	cont2=0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			cont1+=matriz[f][c]
			cont2+=matriz[serv-1][c]
	prom = cont2 / cont1
	print(f'El promedio de los cobros({cont2}) del servicio {serv}, respecto '
		  f'al total {cont1} es de {prom}')



def menu(v):
	op = 1
	ban=False
	fd = 'COBROS_BIN.dat'
	while op != -1:
		print('MENU DE RAPIPAGO\n'
			  '0. Genrear ARCHIVO'
			  '\n1.Agregar un nuevo cobro al archivo de cobros.'
			  '\n2. Determinar el monto total para un número de cuenta X pasado por parámetro'
			  '\n3. Indicar el monto total acumulado para cada servicio, en el día del mes que se lo cobro (matriz de acumulación)'
			  '\n4. Indicar, a partir de la matriz, el día con mayor monto cobrado'
			  '\n5. Indicar, a partir de la matriz, el promedio cobrado para el servicio X pasado por parámetro')
		op = int(input('Ingrese opcion: '))
		if op == 1:
			agregar(fd)
			mostrar_archivo(fd)
		elif op == 2:
			x = int(input('Ingrese cuenta que quiera buscar: '))
			sum_param_file(fd, x)
		elif op == 3:
			matriz=crear_matriz(fd)
			ban=True
		elif op == 4:
			if ban:
				sum_col(matriz)
			else:
				print('Primero tiene que generar la matriz en el paso 3')
		elif op == 5:
			if ban:
				#servicio  promedio cobro matriz
				serv = int(input('Ingrese el Servicio que desea buscar'))
				promedio_param(matriz, serv)
			else:
				print('Primero tiene que generar la matriz en el paso 3')
		else:
			pass




if __name__ == '__main__':
	x = input('Desea Generar Archivo: (s o n)')
	v = generar(x)
	menu(v)
