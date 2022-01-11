# El gobierno de la provincia de Córdoba desea guardar la información referida a los resultados de los exámenes de concursos por cargos en la administración pública, en un arreglo de n registros (donde n es un valor que se carga por teclado). Por cada resultado del concurso, se pide guardar el dni del concursante, su nombre, el cargo para el que se postuló (un código que va de 0 a 19, o sea, hay 20 cargos) y el puntaje obtenido (un valor de 0 a 100 , que puede tener decimales).

# Se pide desarrollar un programa en Python controlado por un menú de opciones.
# Ese menú debe permitir gestionar las siguientes tareas a partir del arreglo
# pedido en el párrafo anterior:

#1
# Cargar el arreglo pedido con los datos de los n resultados.
# Validar que el código del cargo se encuentre entre 0 y 19.

#2
# Mostrar los datos de los concursantes que hayan aprobado el examen
# (se aprueba con 70 puntos o más).


# preguntar o revisar como eran los vectores de conteo

#3
# Determinar cuántos concursantes rindieron el examen por cada tipo de cargo
# (es decir, cuántos concursantes rindieron por el cargo 0, cuántos por
# el cargo 1, cuántos por el cargo 2, etc... hasta el cargo 19).

#4
# Mostrar los datos del arreglo, ordenados de mayor a menor, por el puntaje
# obtenido en el examen.
#5
# Cargar por teclado el nombre de un postulante, y mostrar por pantalla todos
# los datos del mismo si se encuentra en el vector. Si este postulante además
# aprobó el concurso, muestre un mensaje que resalte ese resultado además de
# sus datos. Informe con otro mensaje si el postulante no se encuentra en
# el vector.

class Sorteo:
	def __init__(self, nombre, puesto, puntaje):
		self.nombre = nombre
		self.puesto = puesto
		self.puntaje = puntaje


def carga(v):
	for i in range(len(v)):
		nombre = input('ingrese nombre: ').upper()
		puesto = int(validacion_intervalo(0,20,'ingrese el puesto: '))
		puntaje = float(validacion_intervalo(0,101,'ingrese el puntaje: '))
		v[i] = Sorteo(nombre, puesto, puntaje)


def write(v, elem=False):
	if elem:
		print('{0:5}{1:5}{2:5}'.format(v.nombre, v.puesto, v.puntaje))
	else:
		print('{0:10}{1:10}{2:10}'.format('nombre', 'puesto', 'puntaje'))
		for i in range(len(v)):
			print('{0:5}{1:5}{2:5}'.format(v[i].nombre, v[i].puesto, v[i].puntaje))


def validacion_intervalo(x, y, msg='ingrese cargo: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('ingrese un numero valido por el amor de Dios!!!!')
	return num


def search_name(v, nombre):
	find = False
	for i in range(len(v)):
		if v[i].nombre == nombre:
			find = True
			write(v[i] , True)
	if not find:
		print('no se encontro el nombre en nuestros registros')


def orden_puntaje(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].puntaje < v[j].puntaje:
				v[i], v[j] = v[j], v[i]
	return v


def verificacion(x):
	if x < 70:
		return False
	return True


def vec_cont(v):
	n=len(v)
	vector_conteo=[0]*19 #OJO CON ESTO, NO PONER EL LEN DEL ARREGLO SINO LA CANTIDAD QUE PUEDE RECIBIR
	for i in range(len(v)):
		if v[i].puesto!=None:
			x=v[i].puesto
			vector_conteo[x]+=1 #error
	return vector_conteo


def menu(v):
	x = 1
	while x != 0:
		print('MENU DE SORTEOS \n1. Cargar el arreglo pedido con los datos de'
			  ' los n resultados.\n2. Mostrar datos de ganadores'
			  ' \n3. cuántos concursantes rindieron el examen por '
			  'cada tipo de cargo \n4.los datos del arreglo, ordenados'
			  ' de mayor a menor, por el puntaje\n5.Cargar por teclado '
			  'el nombre de un postulante, y mostrar por pantalla\n0.Salir')
		x = validacion_intervalo(0,5, 'ingrese su opcion: ')
		if x==1:
			carga(v)
		if x==2:
			for i in range(len(v)):
				x=v[i].puntaje
				if verificacion(x):
					print('{0:5}{1:5}{2:5}'.format('nombre', 'puesto', 'puntaje'))
					write(v[i] , True)
		if x==3:
			conteo=vec_cont(v)
			for i in range(len(conteo)):
				print('{0:2}{1:5}{2:5}'.format(i,'-->', conteo[i]))
		if x==4:
			orden_puntaje(v)
			write(v)
		if x==5:
			name=input('ingrese el nombre que quiere buscar').upper()
			search_name(v, name)
		if x==0:
			break


def principal():
	n=int(input('ingrese cuantos sorteos desea cargar: '))
	v=[None]*n
	menu(v)


if __name__ == '__main__':
    principal()
