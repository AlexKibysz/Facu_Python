#El presente archivo contiene datos de clientes separados en filas y por , (comas)
#Cada fila del archivo contiene la información de los clientes separada por comas.
#Cada cliente contienen los atributos:
#<nombre>,<apellido>,<email>,<activo>,<fecha de alta>,<hora de alta [desestimar]>,<importe pagado>
#A partir de la importación de los datos ACTIVOS (el atributo activo con valor 1) del archivo
# crear un vector de registros de clientes y con dichos datos cargados se necesita que la aplicación pueda:
# 1) Mostrar Nombre y Apellido  Email y Fecha  de todos los clientes.
# 2) Filtrar y Mostrar solo los clientes cuyo apellido comienza con la letra l que se carga por teclado
# mostrando además en algun lado el total pagado por el grupo de clientes filtrado.
# 4) Finalmente generar un nuevo archivo de texto separado por comas con una línea por registro que guarde
# solo los registros que tienen un importe pagado mayor al promedio general de importe pagado de todos los clientes.

class Cliente:
    def __init__(self, nombre, apellido, mail, fecha, importe):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.fecha = fecha
        self.importe = importe


def write(cliente):
    print("Nombre:", cliente.nombre, end =" - ")
    print("Apellido:", cliente.apellido, end = " - ")
    print("Mail:", cliente.mail, end= " - ")
    print("Fecha:", cliente.fecha, end = " - ")
    print("Importe: $", cliente.importe)
