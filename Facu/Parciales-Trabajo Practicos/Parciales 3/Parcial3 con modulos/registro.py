# Creación del registro
class Poliza:
    def __init__(self, identificacion, nombre, tipo, costo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.tipo = tipo
        self.costo = costo


# Función para pasar a string
def to_string(registro):
    cadena = ''
    cadena += 'Número de Identificación: ' + str(registro.identificacion) + ' - '
    cadena += 'Nombre del cliente: ' + str(registro.nombre) + ' - '
    cadena += 'Tipo de Póliza: ' + str(registro.tipo) + ' - '
    cadena += 'Costo mensual de Póliza: $' + str(registro.costo)

    return cadena
