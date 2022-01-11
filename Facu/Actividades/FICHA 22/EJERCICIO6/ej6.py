'''Un club deportivo necesita procesar los pagos realizados por sus socios.

Para ello, se cuenta con un archivo denominado cuotas.dat, donde cada registro contiene: número de socio, deporte que realiza (0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin), día del mes en que pagó, valor de la cuota. Si el socio aún no abonó, el día del mes debe ser 0.

Se debe cargar el archivo en un vector y luego implementar un menú con las siguientes opciones:

Consulta: mostrar el contenido del vector
Cobro: buscar un socio y deporte ingresados por teclado. Si el registro existe, registrar el día y valor de pago (también ingresado por teclado). Si no, agregar un nuevo registro en el vector con esos datos. Informar el cambio realizado
Morosos: generar un archivo de texto conteniendo los registros de los socios que aun no pagaron la cuota
Totales: indicar cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes
Grabar: reemplazar el archivo pagos.dat con el contenido del vector. Mostrar el contenido del archivo.

#numero de socio
#deporte ((0: Natacion/1: Basquet/2: Karate/3: Futbol/ 4: Patin))
#día del mes en que pagó
#valor de la cuota
#Si el socio aún no abonó
#el día del mes debe ser 0

menu
1. Consulta: mostrar el contenido del vector

2.Cobro: buscar un socio y deporte ingresados por teclado.
Si el registro existe, registrar el día y valor de pago (también ingresado por teclado).
Si no, agregar un nuevo registro en el vector con esos datos. Informar el cambio realizado

3.Morosos: generar un archivo de texto conteniendo los registros de los socios que aun no pagaron la cuota

4.Totales: indicar cantidad de cobros por cada deporte, y cuál es el deporte con mayor cantidad de participantes

5.Grabar: reemplazar el archivo pagos.dat con el contenido del vector. Mostrar el contenido del archivo.
'''
from ej6file import *


def validar(x, y, msg='Ingrese una opcion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('valor incorrecto elija un valor entre', x, 'o ', y)
	return num


def menu(fd):
	op = 1
	while op != 0:
		print('MENU \n1. Consulta: mostrar el contenido del vector\n2.Cobro:'
			  ' buscar un socio y deporte ingresados por teclado.\n Si el '
			  'registro existe, registrar el día y valor de pago'
			  ' (también ingresado por teclado).\n Si no, agregar un nuevo '
			  'registro en el vector con esos datos. Informar el '
			  'cambio realizado\n3.Morosos: generar un archivo de texto'
			  ' conteniendo los registros de los socios que '
			  'aun no pagaron la cuota\n4.Totales: indicar cantidad de cobros '
			  'por cada deporte, y cuál es el deporte con mayor cantidad '
			  'de participantes\n5.Grabar: reemplazar el archivo pagos.dat '
			  'con el contenido del vector. Mostrar el contenido del archivo.')
		op = validar(0, 5, 'Ingrese Seleccion: ')
		if op == 0:
			break
		elif op == 1:
			mostrar_archivo(fd)
		elif op == 2:
			param1 = int(input('Ingrese ID del Socio: '))
			param2 = float(input('Ingrese Pago del Socio: '))
			file_search(fd, param1, param2)
		elif op == 3:
			fd2 = 'Morosos.dat'
			build_file_param(fd2, v)
			print('')
			mostrar_archivo(fd)

		elif op == 4:
			pass
		elif op == 5:
			pass


if __name__ == '__main__':
	fd = 'SociosFile.dat'
	sel = validar(1, 2,
				  'Desea Generar Archivo Todos los datos se Remplazaran: (1.si 2.No)')
	if sel == 1:
		n = int(input('Cuantos Socios desea generar: '))
		v = build_file(fd, n)
		sel2 = validar(1, 2, 'Desea mostar archivo generado?')
		if sel2 == 1:
			mostrar_archivo(fd)
	menu(fd)
