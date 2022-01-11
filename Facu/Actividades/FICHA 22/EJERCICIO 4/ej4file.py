from ej4reg import *
from random import *
import os
import pickle


# nombre y apellido, mail y teléfono

def random_name():
	nombre = (
		"Alexander", "Bianca", "Jeremias", "Bruno", "Juan", "Mateo", "Matias",
		"Marcos",
		"Lucas", "Melisa", "Anilem", "Valentino", "Uriel", "Brian", "Kevin",
		"Erick", "Lara", "Lucia", "Maximo", "Vladimir", "Jorge", 'Exequiel',
		'Felipe', 'Andrea'
		, 'Alan', 'Lautaro', 'Benjamin', 'Alex', 'Nadya', 'Juan Cruz', 'Karen',
		'Ulises', 'Osvaldo'
		, 'Thiago', 'Gael', 'Pablo', 'Hugo', 'Adrian', 'Martin', 'Alvaro',
		'Daniel', 'Javier', 'Ada',
		'Lia', 'Gimena', 'Jimena', 'Lola', 'Julia', 'Cloe', 'Maria', 'Amalia',
		'Paula', 'Pablo', 'Sofia', 'Catalina', 'Benjamin', 'Isabella',
		'Martina', 'Catalina', 'Bautista', 'Sofia', 'Olivia', 'Felipe',
		'Emma', 'Valentino', 'Benicio', 'Joaquín', 'Delfina', 'Lorenzo',
		'Francesca', 'Valentina', 'Emilia',
		'Mateo', 'Santino', 'Tomás', 'Francisco', 'Juana', 'Josefina',
		'Santiago', 'Simon', 'Guillermina',
		'Ignacio', 'Victoria', 'Guadalupe', 'Agustin', 'Julieta', 'Pedro',
		'Renata', 'Alma', 'Jazmin', 'Ciro',
		'Thiago', 'Lola', 'Pilar', 'Lucia', 'Lautaro', 'Bruno', 'Malena',
		'Julia', 'Dante', 'Valentin', 'Salvador',
		'Nicolas', 'Maximo', 'Mia', 'Tiziano', 'León', 'Camila', 'Clara',
		'Bianca', 'Milo', 'Facundo', 'Vicente',
		'Helena', 'Zoe', 'Agustina', 'Ambar', 'Ramiro', 'Manuel', 'Nina',
		'Julián', 'Bastian', 'María Paz',
		'Paulina', 'Mora', 'Jeremías', 'Amparo', 'Morena', 'Franco', 'Matias',
		'Felicitas', 'Luca', 'Genaro',
		'Lucas', 'Augusto', 'Mia Jazmin', 'Fausto', 'Camilo', 'Vera', 'Elena',
		'Giovanni', 'Lucio', 'Juliana',
		'Antonella', 'Antonia', 'Agostina', 'Matilda', 'Martin', 'Constanza',
		'Alejo', 'Paloma', 'Ian', 'Gael',
		'Lara', 'Luciano', 'Federico', 'Milagros', 'Lisandro', 'Pía',
		'Francesco', 'Lourdes', 'Noah', 'Sara',
		'Alfonsina', 'Lupe', 'Sebastián', 'Candelaria', 'Octavio', 'Jonás',
		'Geronimo', 'Teo', 'Abril', 'Tobias',
		'Gino')
	nombre1 = choice(nombre)
	return nombre1


def random_apellido():
	apellido = (
	'González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz',
	'Martínez', 'Pérez',
	'García', 'Sánchez', 'Romero', 'Sosa', 'Torres', 'Álvarez', 'Ruiz',
	'Ramírez', 'Flores', 'Benítez',
	'Acosta', 'Medina', 'Herrera', 'Suárez', 'Aguirre', 'Giménez',
	'Gutiérrez', 'Pereyra', 'Rojas', 'Molina', 'Castro', 'Ortiz', 'Silva',
	'Kibysz', 'González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz',
	'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero',
	'Sosa', 'Torres', 'Álvarez', 'Ruiz', 'Ramírez', 'Flores', 'Benítez',
	'Acosta', 'Medina', 'Herrera', 'Suárez',
	'Aguirre', 'Giménez', 'Gutiérrez', 'Pereyra', 'Rojas', 'Molina', 'Castro',
	'Ortiz', 'Silva', 'Núñez', 'Luna',
	'Juárez', 'Cabrera', 'Ríos', 'Morales', 'Godoy', 'Moreno', 'Ferreyra',
	'Domínguez', 'Carrizo', 'Peralta',
	'Castillo', 'Ledesma', 'Quiroga', 'Vega', 'Vera', 'Muñoz', 'Ojeda', 'Ponce',
	'Villalba', 'Cardozo', 'Navarro',
	'Coronel', 'Vázquez', 'Ramos', 'Vargas', 'Cáceres', 'Arias', 'Figueroa',
	'Córdoba', 'Correa', 'Maldonado', 'Paz',
	'Rivero', 'Miranda', 'Mansilla', 'Farias', 'Roldán', 'Méndez', 'Guzmán',
	'Agüero', 'Hernández', 'Lucero', 'Cruz',
	'Páez', 'Escobar', 'Mendoza', 'Barrios', 'Bustos', 'Ávila', 'Ayala',
	'Blanco', 'Soria', 'Maidana', 'Acuña', 'Leiva',
	'Duarte', 'Moyano', 'Campos', 'Soto', 'Martín', 'Valdez', 'Bravo', 'Chávez',
	'Velázquez', 'Olivera', 'Toledo')
	apellido = choice(apellido)
	return apellido


def random_mail(x, y):
	dominios = ('Yahoo', 'Gmail', 'Hotmail', 'Live',
				'Outlook', 'Utn.Frc.edu.ar')
	domin_rand = choice(dominios)
	numero_ran = randint(100, 999)
	mail = str(x) + '_' + str(y) + '_' + str(
		numero_ran) + '@' + domin_rand + '.com'
	return mail


def gen_file(x, fd, auto=True):
	if auto:
		m = open(fd, 'wb')
		for i in range(x):
			nombre = random_name()
			apellido = random_apellido()
			mail = random_mail(nombre, apellido)
			numero = randint(1000000000, 9999999999)
			nuevo = Contacto(nombre, apellido, mail, numero)
			pickle.dump(nuevo, m)
		m.close()
	else:
		m = open(fd, 'wb')
		for i in range(x):
			nombre = input('Ingrese nombre: ')
			apellido = input('Ingrese Apellido: ')
			mail = input('Ingrese Mail: ')
			numero = int(input('Ingrese Numero de Telefono: '))
			nuevo = Contacto(nombre, apellido, mail, numero)
			pickle.dump(nuevo, m)
		m.close()


def mostrar_archivo(fd):
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		to_string(a)
	m.close()


def vector_from_file(fd):
	v = []
	m = open(fd, 'rb')
	while m.tell() < os.path.getsize(fd):
		a = pickle.load(m)
		v.append(a.nombre)
	m.close()
	print('Lista Generada: ')
	s = "\n"
	lista = s.join(v)
	print(lista)
	return v
