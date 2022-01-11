# conocemos su legajo de admisión a la Escuela (un número entero), su nombre y su apellido

# 1. Agregar un aspirante a la lista. Tener en cuenta que el legajo no puede repetirse,
# y este factor hay que validarlo antes de permitir la carga de cada nuevo aspirante

# 2. Listar los aspirantes. De a un aspirante por línea

# 3. Asignar los aspirantes a las Casas de Hogwarts.
# Aquí viene lo importante lo que tenemos que tener en cuenta al realizar
# este proceso es que el sombrero no puede mandar a todos los magos a Gryffindor
# y por ello, si bien la asignación
# se hace mediante un número aleatorio, deberemos ir validando que
# las cantidades de cada casa no queden desbalanceadas para esto vamos a
# poner como cota que una casa no puede
# tener más de dos aspirantes de diferencia con la que le sigue en cantidad.

# 4. Determinar la cantidad de aspirantes asignados por cada casa.
# Mostrar las 4 casas con la cantidad de aspirantes que se asignaron a cada una de ellas.

# 5. Listar las casas con los aspirantes asignados a cada una.
# Realizar un listado donde figure cada casa como Título y luego
# todos los aspirantes que fueron asignados a ella.
from random import *


class Estudiantes:
	def __init__(self, legajo, nombre, apellido, casa):
		self.legajo = legajo
		self.nombre = nombre
		self.apellido = apellido
		self.casa = casa


def generador_legajo():
	v=[]
	if v[0] == None:
		legajo = randint(0, 600)
	while legajo in v:
		legajo = randint(0, 600)
		v.append(legajo)
	return v


def random_name():
	nombre = (
		"Alex", "Bian", "Jere", "Benja", "Juan", "Mateo", "Matias", "Marcos",
		"Lucas", "Melisa", "Anilem", "Valentino", "Uriel", "Brian", "Kevin",
		"Erick", "Lara", "Lucia", "Maximo", "Vladimir", "Jorge")
	apellido = ("ito", "med", "dez", "wn", "íguez",
				"lva", "cía", "arez", "ller ", "as",
				"dos", "Cabrera", "Iglesias", "illo", "do",
				"po", "ón", "man", "pin")
	nombre1 = choice(nombre)
	apellido1 = choice(apellido)
	completo = (nombre1 + " " + apellido1)
	return completo


def random_apellido():
	apellido = ("Abbott", "Avery", "Blishwick", "Bones", "Boot",
				"Bulstrode", "Burke", "Calderon-Boot", "Crabbe ", "Crouch",
				"Dumbledore", "Fawley", "Flint", "Gamp", "Goldstein",
				"Rowle", "Shafiq", "Snape", "Umbridge")
	apellido1 = choice(apellido)
	completo = (apellido1)
	return completo




def random_casas(v):
	cc=[]
	if cc==[]:
		seleccion=choice('casa 1', 'casa 2', 'casa 3', 'casa 4')
		cc.append(seleccion)
		return seleccion
	else:
		n=len(v)/4
		for i in range():





def carga(v):
	for i in range(len(v)):
		leg=generador_legajo()
		legajo=leg[i]
		nombre= random_name()
		apellido= random_apellido()
