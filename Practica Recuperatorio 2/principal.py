# dni nomcad titulocad num(0,29) monto
from modulo import *

def menu(fd):
	num = 1
	ban = False
	while num != 0:
		print()
		print('Menu inscriptos: \n'
			  '1. Cargar datos de n Inscriptos\n'
			  '2.Ordenar el arreglo de menor a mayor por dni y mostrar datos \n'
			  '3.Crear un Archivo que contenga los datos de todos los inscriptos '
			  'con monto a pagar inferior a  x \n4.Mostrar el archivo que contenga los datos de todos los inscriptos del arreglo'
			  '\4. Mostrar el archivo que acaba de crear en el punto 3, a razon de  un registro por linea\n'
			  '5.Buscar en el arreglo un nombre ingresado por teclado'
			  '\n6. Apartir del arreglo creado en el punto 1 contar cuantos estan inscriptos en ciertos cursos mostrar distinto de 0\n'
			  '7. Cargar Cadena de caracteres y determinar cuantos caracteres de la cadena no eran letras: \n0. Salir')
		num = verificar_intervalo(0, 7)
		if num == 1:
			ban = True
			n = verificar_mayor_cero()
			v = carga(n)
			print()
		elif num == 2:
			if ban == True:
				ordenar_dni(v)
			else:
				print('Primero tiene que generar registro!')
			print()

		elif num == 3:
			param = float(
				input('Ingrese monto maximo para generar el archivo: '))
			crear_arch(fd, v, param)
			print()
		elif num == 4:
			leer_arch(fd)
			print()
		elif num == 5:
			if ban:
				nom = input('Ingrese nombre que quiera buscar: ')
				buscar_reg_nom(v, nom)

			else:
				print('Primero tiene que generar registro')
			print()
		elif num == 6:
			if ban == True:
				vec_cont_curso(v)
			else:
				print('Primero tiene que generar registro!')
			print()
		elif num == 7:
			texto = input('Ingrese texto que desea analizar: ')
			analizar_texto_no_letras(texto)
			print()
		elif num == 0:
			print('Programa cerrado')
			break


if __name__ == '__main__':
	fd = 'ListaInscriptos'
	print('▧▧▧▧▧  Recuperatorio numero 2  ▧▧▧▧▧')
	menu(fd)
