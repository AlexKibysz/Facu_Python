# Título o nombre
# Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
# Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
# Cantidad de temporadas.
# Duracion total (en minutos)

# En primer lugar, cargar el contenido del archivo en un vector de registros y ordenarlo por título.

# menu

# 1. Listar el contenido del vector, mostrando una línea por serie (usar género y el idioma en lugar de sus códigos).

# 2. Ingresar por teclado un idioma x. Generar un archivo cuyo nombre tenga la forma
# “SeriesX.dat” (reemplazando x por el número del idioma seleccionado) conteniendo
# todas las series de ese idioma que tengan más de una temporada. Mostrar el nuevo archivo generado.

# 3. Buscar en el vector una serie con el título x (x se ingresa por teclado). Si la serie existe, mostrar
# sus datos. Si no, informar con un mensaje.

# 4. Determinar la duración total de las series en idioma español por cada género disponible.

# 5. A partir del vector determinar la cantidad de series por género y por idioma.
# Para eso se debe utilizar una matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0.
from ej5file import *



def validar(x, y, msg='Ingrese una opcion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('valor incorrecto elija un valor entre', x, 'o ', y)
	return num


def menu(fd):
	op = 1
	while op != -1:
		print(
			'MENU SERIES AGENDAR\n0.Crear Archivo\n1. Listar el contenido del vector, mostrando una línea por serie '
			'(usar género y el idioma en lugar de sus códigos)\n2.Ingresar por '
			'teclado un idioma x. Generar un archivo cuyo nombre tenga la forma '
			'SeriesX.datreemplazando x por el número del idioma seleccionado) '
			'contenie todas las series de ese idioma que tengan más de una'
			' temporada. Mostrar el nuevo archivo generado.\n3.Buscar en el'
			' vector una serie con el título x (x se ingresa por teclado). Si la serie existe, mostrar '
			'sus datos. Si no, informar con un mensaje\n4.Determinar la'
			' duración total de las series en idioma español por cada género disponible.\n5.A partir del vector '
			'determinar la cantidad de series por género y por idioma. Para eso se debe utilizar una matriz de conteo. '
			'Mostrar las cantidades sólo cuando sean mayores a 0.\n-1.Salir')
		op = validar(-1, 5)
		if op == 1:
			mostrar_archivo(fd)
		elif op == 2:
			idioma = input('Ingrese Idioma para crear archivo series: ')
			generar_file_param(fd, idioma)
		elif op == 3:
			print('*' * 100)
			param = input('Ingrese nombre de la Serie que desea buscar')
			search_file_param(fd, param)
		elif op == 4:
			idioma2 = input('Ingrese el Idioma: ')
			sum_param_file(fd, idioma2)
		elif op == 5:
			matriz=generar_matriz(fd)
			mostrar_matriz(matriz)
		elif op == 0:
			print(
				'Desea Crear un Nuevo Archivo?: (1.si 2.no) los datos seran borrados')
			sl = validar(1, 2)
			if sl == 1:
				n = int(input('Cuantas Series desea Generar'))
				generar_file(n, fd)
			else:
				continue
		elif op == -1:
			break


if __name__ == '__main__':
	fd = 'Series.dat'
	menu(fd)
