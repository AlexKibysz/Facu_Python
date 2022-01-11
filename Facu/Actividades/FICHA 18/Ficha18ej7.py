# 7. Estudio de Arquitectura
# Un estudio de arquitectos desea almacenar la información referida a sus n
# proyectos para sus clientes en un arreglo de registros (

# cargar n por teclado).
# Por cada proyecto se pide guardar su número de identificación,
# el nombre del cliente para el cual se hizo el diseño,
# el monto de honorarios por el proyecto,
# y un código numérico entre 0 y  14 para indicar el tipo de construcción a la
# que se sujeta el diseño
# (0: barrio cerrado, 1: casa de verano, 2: departamento, etc.)


# Se pide desarrollar un programa en Python controlado por un menú de opciones.
# Ese menú  debe  permitir  gestionar las siguientes tareas, siempre usando funciones
# que acepten parámetros y/o retornen valores en cada situación en que se considere apropiado:


# 1. Cargar el arreglo pedido. Validar que el código numérico para el tipo de
# proyecto esté efectivamente entre 0 y 14.


# 2. Mostrar todos los datos, a razón de un registro por línea en la pantalla.


# 3. Determinar el monto de honorarios acumulado en cada uno de los 15
# tipos posibles de construcción (un acumulador para sumar los montos de
# los diseños tipo 0, otro para los proyectos tipo 1, etc.)


# 4. Muestre todos los proyectos cuyo código de tipo de proyecto sea diferente
# de 4. Este listado debe salir ordenado de menor a mayor, de acuerdo al monto
# de honorarios.


# 5. Determinar si existe algún diseño para el cliente cuyo nombre sea igual a x,
# siendo x una cadena que se carga por teclado. Si existe, mostrar todos los
# datos de ese diseño por pantalla. Si no existe, informar con un mensaje.

class Proyecto:
	def __init__(self, nombre, honorarios, tipo_cons):
		self.nombre = nombre
		self.honorarios = honorarios
		self.tipo_cons = tipo_cons


def sumatoria(v):
	cont = 0
	for i in range(len(v)):
		cont += v[i].honorarios
	return cont


def verif_diseño_nombre(v, nombre):
	for i in range(len(v)):
		hay_nom_pr = False

		if v[i].nombre == nombre:
			hay_nom_pr = True
			print('se ha encontrado un proyecto con ese nombre: ')
			write(v[i], True)  # write(v[0])
	if not hay_nom_pr:
		print('no se ha encontrado proyecto con ese nombre')


def ordenamiento(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].honorarios < v[j].honorarios:
				v[i], v[j] = v[j], v[i]
	return v


# fijarse como almacenarlo a los distintos de tipo 4
def mostrar_dist_4(v):
	v2 = [None] * len(v)
	for i in range(len(v)):
		if v[i].tipo_cons != 4:
			nombre = v[i].nombre
			honorario = v[i].honorarios
			tipo_cons = v[i].tipo_cons
			v2[i] = Proyecto(nombre, honorario, tipo_cons)
	ordenamiento(v2)


def write(v, elem=False):
	if elem == False:
		print('(=)' * 20)
		print('{0:5} {1:12} {2:17}'.format('Nombre', 'Honorarios',
										   'Tipo Construccion'))
		for i in range(len(v)):
			print('{0:5}{1:12}{2:17}'.format(v[i].nombre, v[i].honorarios,
											 v[i].tipo_cons))
		print('(=)' * 20)
	else:
		print('{0:5} {1:12} {2:17}'.format('Nombre', 'Honorarios',
										   'Tipo Construccion'))
		print('{0:5}{1:12}{2:17}'.format(v.nombre, v.honorarios, v.tipo_cons))


def menu(v):
	x = 1
	while x != 6:
		print(
			'MENU DE PROYECTOS \n 1.Cargar de proyectos \n 2.Mostrar todos los datos'
			'\n 3.Mostrar el monto de honorarios acumulado en '
			'cada uno de los 15 tipos de construccion \n 4.Mostrar los proyectos '
			'cuyo código de tipo de proyecto sea diferente de 4 \n'
			' 5.mostrar si existe algún diseño tiene el nombre a ingresar \n 6.Salir')
		x = validar(0, 6)
		if x == 1:
			carga(v)
		if x == 2:
			write(v)
		if x == 3:
			print('la cantidad acumulada de honorarios en los 15 tipos es de: ',
				  sumatoria(v))
		if x == 4:
			v=mostrar_dist_4(v)
			write(v)
		if x == 5:
			nombre = input('ingrese el nombre que desea buscar: ')
			verif_diseño_nombre(v, nombre)
		if x == 6:
			break


def validar(x, y, msg='Ingrese una opcion: '):
	num = x - 1
	while num < x or num > y:
		num = int(input(msg))
		if num < x or num > y:
			print('valor incorrecto elija un valor entre', x, 'o ', y)
	return num


def carga(v):
	for i in range(len(v)):
		nombre = input('ingrese nombre: ')
		honorarios = float(input('ingrese honorarios: '))
		tipo_cons = validar(1, 14, 'Ingrese tipo de construccion: ')
		v[i] = Proyecto(nombre, honorarios, tipo_cons)


def principal():
	print('Estudio De Arquitectos Gestor de Proyectos')
	n = int(input('Ingrese la cantidad de proyectos que quiere almacenar: '))
	v = [None] * n
	menu(v)


if __name__ == '__main__':
	principal()
