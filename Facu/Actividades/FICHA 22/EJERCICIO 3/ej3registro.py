class Cobros:
	def __init__(self, dia, monto, serv, cuenta):
		self.dia = dia
		self.monto = monto
		self.serv = serv
		self.cuenta = cuenta


def to_string(a):
	m = '{0:<6}{1:^4}'.format('DIA: ', a.dia)
	m += '{0:<8}{1:^5}'.format('MONTO: ', a.monto)
	m += '{0:<8}{1:^6}'.format('SERVICIO: ', a.serv)
	m += '{0:<}{1:^}'.format('Cuenta: ', a.cuenta)
	print(m)
