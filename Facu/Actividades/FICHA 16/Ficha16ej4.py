# nxm n=Proyectos m=roles

# carga proyecto, cantidad de roles,
# valor horas consumidas por un rol para un proyecto
from random import *


def sum_columna(matriz):
	x=validar_mayor(0,'Ingrese la columna que quiera analizar: ')
	x-=1
	sum_col=0
	total=0
	for f in range(len(matriz)):
		sum_col +=	matriz[f][x]
		for c in range(len(matriz[0])):
			total+=matriz[f][c]
	operacion=porcentaje(sum_col, total)
	print(f'Tuvo un total de {sum_col} en los proyectos de la empresa.')
	print(f'el porcentaje de la columna {x+1} sobre el total {total} de horas es: {operacion}%')
	return operacion, total

def porcentaje(cant, cant_total):
	if cant_total != 0:
		calculo = round((cant * 100) / cant_total, 2)
		print(f'el porcentaje de {cant} respecto al total es de: {calculo}%')
		return calculo
	else:
		return 0

def horas_prom_rango(matriz, total):
	x=validar_mayor(0,'Ingrese el valor minimo: ')
	y=validar_mayor(0, 'elija el valor maximo: ')
	sum=0
	sum2=0
	for f in range(len(matriz)):
		if f>=x or f<=y:
			for c in range(len(matriz[0])):
					sum+=matriz[f][c]
			print(f'La cantidad de Horas del proyecto {f+1} es: {sum}')
			sum2=sum
			sum=0
	print(f'El promedio de el rango de proyectos del {x} al {y} es {total/sum2} ')

def sum_fila(matriz):
	sum=0
	x = validar_mayor(0,'Ingrese Fila a Analizar: ')
	for c in range(len(matriz[0])):
		sum+=matriz[x][c]
	print(f'la cantidad de horas que tomo el proyecto {x} fue: {sum}')


def mostrar_matriz(matriz):
	filas = len(matriz)
	print('\033[0;36;47mnumeros: ', end='')
	for c in range(len(matriz[0])):
		print('{0:^6}'.format(c + 1), end='')
	print('\033[0m')
	# printeo fila
	for f in range(filas):
		if f < 10:
			print(f'\033[0;36;47mdado 0{f}: |\033[0m', end='')
		else:
			print(f'\033[0;36;47mdado {f}: |\033[0m', end='')
		for c in range(len(matriz[0])):
			if matriz[f][c] <= 9:
				print('{0:>5}'.format(str(0) + str(matriz[f][c])), end='|')
			else:
				print('{0:>5}'.format(matriz[f][c]), end='|')
		print()


def validar_mayor(num, msg=f'Ingrese un numero: '):
	opcion = int(input(msg))
	while opcion < num:
		opcion = int(input(msg + f'(mayor a {num})'))
	return opcion


def crear_matriz(x, y):
	matriz = [[0] * y for c in range(x)]
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			matriz[f][c] = randint(1, 30)
	return matriz

def recorrido_fila_sum(matriz):
	cont=0
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			cont+=matriz[f][c]
		print(f'El proyecto {f+1} tardo {cont}hs por lo tanto cuesta: {175*cont}$')
		cont=0


def principal():
	x = validar_mayor(0)
	y = validar_mayor(-1)
	matriz = crear_matriz(x, y)
	print(matriz)
	mostrar_matriz(matriz)
	print('punto a==============')
	#a
	promedio, total= sum_columna(matriz)
	print('punto b==============')
	#b
	sum_fila(matriz)
	print('punto c==============')
	#c
	horas_prom_rango(matriz, total)
	print('punto d==============')
	#d
	recorrido_fila_sum(matriz)




if __name__ == '__main__':
	principal()
