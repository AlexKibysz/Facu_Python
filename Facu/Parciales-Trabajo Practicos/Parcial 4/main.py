__author__ = 'Alexander Kibysz 85698 1K2'
'''Enunciado T1E3

Una compañía que realiza cultivos hidropónicos desea desarrollar un programa Python que le permita gestionar la información de cada operación de riego realizada. Por cada riego se dispone de la siguiente información: volumen de agua (un valor float) nivel de PH (un valor entero que va del 1 al 10 ambos inclusive), conductividad eléctrica (un valor entero que va del 1 al 5 ambos inclusive) y código de la solución utilizada (un valor entero). Se pide definir el tipo registro Riego con los campos pedidos, y desarrollar un programa en Python controlado por un menú de opciones que permita gestionar las siguientes tareas:

1- Cargar un arreglo de registros con los datos de n riegos. Valide que el nivel de PH y la conductividad eléctrica estén dentro de los valores descriptos. Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor por código de solución. Para esto debe utilizar el algoritmo  inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el contenido completo del vector a razón de un registro por línea.

3- Ingresar desde teclado un nivel de PH y mostrar los datos del primer registro que encuentre que tenga ese nivel de PH. Si no lo encuentra mostrar un mensaje. La búsqueda debe finalizarse inmediatamente si se encuentra un registro.

4- A partir del vector de registros, genere una matriz para acumular los volúmenes de agua por cada nivel de PH y por cada valor de conductividad eléctrica (matriz de acumulación de 10 * 5 acumuladores). Pude ubicar los niveles de PH en filas y los de conductividad eléctrica en columnas. Al finalizar la generación de la matriz, muestre el contenido de la misma pero solo en aquellos casos en los que se encuentren valores mayores a cero.

5- A partir del vector de registros, genere un archivo que contenga todos los datos del mismo.

6- Muestre el contenido del archivo a razón de un registro por línea, pero solo de aquellos donde el nivel de PH sea 1, 3 o 5.'''
from parc4reg import *
from parc4file import *

print('\033[0;30;45m◉' * 20 + ' Parcial Numero 4 ' + '◉' * 20 + '\033[0m')
print('\t\t\t\t\033[0;30;45m 🔰 Cultivos Hidropónicos 🔰 \033[0m')

#validar intervalo
def validar(x, y, msg='Ingrese su seleccion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print(f'Por favor ingrese valores entre {x} y {y}')
	return num

#validacion numero mayor a
def validar_m(x, msg='Ingrese valor: '):
	num = x - 1
	while num <= x:
		num = int(input(msg))
		if num <= x:
			print(f'Ingrese un valor correcto mayor a {x}')
	return num

#Crea matriz acumulacion segun registro

def crear_matriz_cont(v):  # ph filas(1,10)
	# cond (1,5) columnas
	matriz = [[0] * 5 for f in range(1, 11)]
	tam = len(v)
	for i in range(len(v)):
		x = v[i].ph - 1
		y = v[i].conduct - 1
		t = round(v[i].vol, 2)
		matriz[x][y] += t  # dato vol
	return matriz

#printea matriz a razon de una fila
def mostrar_matriz(matriz):
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			if matriz[f][c] != 0:
				p = '{0:<12}{1:<5}{2:<42}{3:<5}{4:<20}{5:<5}'.format(
					'Nivel PH: ', f+1,
					'Nivel Conductividad Electrica: ',
					c + 1,
					'Volumen de agua: ',
					matriz[f][c])
				print(p)

#verificacion vector
def verificacion(ban_v):
	if ban_v:
		print('Primero genere Registro!:')
		return False
	else:
		return True


def menu(fd):
	ban_v = True
	op = 1
	while op != 0:
		print()
		print('=' * 105)
		print(
			'1.Cargar un arreglo de registros con los datos de n riegos\n2.Mostrar '
			'el contenido completo del vector a razón de un registro por línea.\n3.Ingresar desde '
			'teclado un nivel de PH y\n  mostrar los datos del'
			' primer registro que encuentre que tenga ese nivel de PH. \n4 A '
			'partir del vector de registros,\n  genere una matriz para acumular '
			'los volúmenes de agua por cada nivel de PH y por cada valor de '
			'conductividad eléctrica.\n5.A partir del vector de registros, genere un archivo que contenga todos los datos del mismo.'
			'\n6.Muestre el contenido del archivo a razón de un registro '
			'por línea, pero solo de aquellos donde el nivel de PH sea 1, 3 o 5.'
			'\n0. Salir')

		op = validar(0, 6, '🍁💦 Ingrese la opcion: ')
		if op == 0:
			print('🌊 Gracias por usar el programa!! 🌊')
			break
		elif op == 1:
			n = validar_m(0,
						  '🚿Ingrese cuantos Registros de Riegos desea generar: ')
			v = carga(n)
			ban_v = False
		elif op == 2:
			print()
			if verificacion(ban_v):
				print('{0:^100}'.format('Registros de Riegos: '))
				print('⨌' * 45)
				mostrar_reg(v)
				print('⨌' * 45)
		elif op == 3:
			print()
			if verificacion(ban_v):
				ph = validar(1, 10,
							 'Ingrese valor de PH que desea buscar en los registros: ')
				search_reg_param(v, ph)
		elif op == 4:
			print()
			if verificacion(ban_v):
				matriz = crear_matriz_cont(v)
				mostrar_matriz(matriz)
		elif op == 5:
			print()
			sl = validar(1, 2,
						 '📃🖊 Desea Crear Archivo? ⚠si existe el archivo se remplazara⚠ (1.Si 2.No): ')
			if sl == 1:
				if verificacion(ban_v):
					crear_archivo(fd, v)
			else:
				continue
		elif op == 6:
			print()
			print('⨌' * 45)
			mostrar_arch_param(fd)
			print('⨌' * 45)


if __name__ == '__main__':
	fd = 'Riegos.dat'
	menu(fd)
