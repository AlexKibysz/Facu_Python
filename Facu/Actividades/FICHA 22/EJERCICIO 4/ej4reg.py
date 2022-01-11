#nombre y apellido, mail y teléfono.
class Contacto:
	def __init__(self,nombre, apellido, mail, telefono):
		self.nombre= nombre
		self.apellido= apellido
		self.mail=mail
		self.telefono=telefono

def to_string(a):
	m= '{0:<10}{1:^10}'.format('Nombre: ',a.nombre)
	m+= '{0:<10}{1:^10}'.format('Apellido: ',a.apellido)
	m+= '{0:<10}{1:<49}'.format('Mail: ',a.mail)
	m+= '{0:<10}{1:^15}'.format('telefono: ',a.telefono)
	print(m)
