from simp4file import *
from simp4reg import *


def validar(x, y, msg='Ingrese su seleccion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print(f'error ingrese valor entre {x} y {y}')
	return num


def gen_matriz(v, x, y):
	matriz = [[0] * y for f in range(len(x))]
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			matriz[v[f].afiliacion][v[c].tipo] += 1
	return matriz


def mostrar_matriz(matriz):
	for f in range(len(matriz)):
		for c in range(len(matriz[0])):
			if matriz[f][c] != 0:
				print(
					'{0:<10}{1:<10}{2:<10}{3:<10}{4:<10}'.format('Afiliacion: ',
																 f, 'Tipo: ',
																 c, 'Cant: ',
																 matriz[f][c]))


def menu(fd):
	op = 1
	while op != 0:
		print('Menu \n1.Cargar los datos de n registros de tipo Profesional '
			  'en un arreglo de registros (cargue n por teclado). Puede cargarlos'
			  ' datos manualmente, o puede generarlos aleatoriamente\n2.Mostrar el arreglo creado'
			  ' en el punto 1, a razón de un registro por línea.\n3.A partir del arreglo, '
			  'crear un archivo de registros en el cual se copien los datos de todos los profesionales '
			  'cuyo tipode trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un '
			  'valor x que se carga por teclado.\n4.Mostrar el archivo '
			  'creado en el punto 3, a razón de un registro por línea en la '
			  'pantalla.\n5.Buscar en el arreglo creado en el punto 1 un '
			  'registro en el cual el nombre del profesional sea igual a '
			  'nom (cargarnom por teclado). Si existe, mostrar por '
			  'pantalla todos los datos de ese registro. Si no '
			  'existe, informar con un '
			  'mensaje. La búsqueda debe detenerse al encontrar '
			  'el primer registro que coincida con el patrón pedido.\n6. Usando '
			  'el arreglo creado en el punto 1, determine la cantidad de'
			  ' profesionales de cada posible tipo d afiliación porcada '
			  'posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en'
			  ' una matriz de conteo). Muestre sólo los resultadosque sean'
			  'diferentes de 0.')
		op = validar(0, 6)
		if op == 0:
			break
		elif op == 1:
			n = int(input('Cuantos Registros Quiere generar?: '))
			v = generar_reg(n)
		elif op == 2:
			mostrar_reg(v)
		elif op == 3:
			grabar_arvchivo(v,fd)
		elif op == 4:
			mostrar_archivo(fd)
		elif op == 5:
			search_in_reg(v)
		elif op == 6:
			matriz=gen_matriz(v, 5, 14)
			mostrar_matriz(matriz)

if __name__ == '__main__':
	fd = 'Profesionales.dat'
	menu(fd)
