# Título o nombre
# Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
# Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
# Cantidad de temporadas.
# Duracion total (en minutos)

class SeriesR:
	def __init__(self, nombre, genero, idioma, temporada, duracion):
		self.nombre = nombre
		self.genero = genero
		self.idioma = idioma
		self.temporada = temporada
		self.duracion = duracion


def to_string(a):
	m = '{0:<10}{1:<30}'.format('Nombre: ', a.nombre)
	m += '{0:<10}{1:<25}'.format('Genero: ', convertir_genero(a.genero))
	m += '{0:<10}{1:<10}'.format('Idioma: ', convertir_idioma(a.idioma))
	m += '{0:<10}{1:<10}'.format('Temporada: ', a.temporada)
	m += '{0:<10}{1:<10}'.format('Duracion: ', a.duracion)
	print(m)


def convertir_genero(x):
	if x == 0:
		return 'Infantil'
	elif x == 1:
		return 'Comedia'
	elif x == 2:
		return 'Romántico'
	elif x == 3:
		return 'Drama'
	elif x == 4:
		return 'Ciencia Ficción'
	elif x == 5:
		return 'Otros'


def convertir_idioma(x):
	if x == 0:
		return 'Español'
	elif x == 1:
		return 'Inglés'
	elif x == 2:
		return 'Francés'
	elif x == 3:
		return 'Portugués'
	elif x == 4:
		return 'Otros'
