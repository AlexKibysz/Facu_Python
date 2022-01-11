# Una tienda dedicada a la venta de productos para el hogar, desea un programa para procesar los
# datos de los productos que tiene a la venta. Por cada producto se tienen los siguientes datos:
# - número de identificación del producto
# - la descripción del producto
# - el importe del producto
# - el tipo de producto (un valor entre 0 y 10 ambos incluidos, de la forma 0: Muebles, 1: Jardín, 2: Bazar, etc.).
# - Se desea almacenar la información referida a los n productos en un arreglo de registros de tipo Producto (definir el
# tipo Producto y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
#
# 1 Cargar el arreglo pedido con los datos de los n productos. Valide que el tipo de producto sea un valor entre
# 0 y 10 (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática
# (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
# 2 Mostrar todos los datos de los productos, en un listado ordenado de mayor a menor según el importe de los productos.
# 3 Usando el arreglo creado en el punto 1, determine la cantidad de productos por cada tipo de producto (o sea, 11 contadores).
# Muestre sólo los resultados mayores a 0.
# 4 Determinar cuál es la cantidad de productos que tienen un importe mayor al importe promedio de todos los productos.
# 5 Determinar si existe un producto cuyo importe sea impar y su número de identificación sea igual a x
#  (siendo x un valor que se carga por teclado). Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
#  Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.


import random


class Producto:
    def __init__(self, numero_iden, descripcion, importe, tipo):
        self.numero_iden = numero_iden
        self.descripcion = descripcion
        self.importe = importe
        self.tipo = tipo


def carga_automatica(tabla):
    for i in range(len(tabla)):
        numero_iden = random.randint(1, 100)
        descripcion = random.choice(['Nuevo', 'Usado', 'Reparar', 'Eliminar de Stock'])
        importe = random.randint(500, 2000)
        tipo = random.randint(0, 10)
        tabla[i] = Producto(numero_iden, descripcion, importe, tipo)


def ordenar(tabla):
    n = len(tabla)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tabla[i].importe < tabla[j].importe:
                tabla[i], tabla[j] = tabla[j], tabla[i]


def to_string(tabla, i):
    r = ''
    if (i + 1) != 0:
        r += str(i + 1) + ') '
    r += 'Numero de identificacion: ' + str(tabla.numero_iden)
    r += ' - Descripcion: ' + str(tabla.descripcion)
    r += ' - Importe: ' + str(tabla.importe)
    r += ' - Tipo: ' + str(tabla.tipo)
    return r


def mostrar(tabla):
    for i in range(len(tabla)):
        print(to_string(tabla[i], i))


def cantxtipo(tabla):
    contadores = [0] * 11
    for i in range(len(tabla)):
        if tabla[i].tipo == 0:
            contadores[0] += 1
        elif tabla[i].tipo == 1:
            contadores[1] += 1
        elif tabla[i].tipo == 2:
            contadores[2] += 1
        elif tabla[i].tipo == 3:
            contadores[3] += 1
        elif tabla[i].tipo == 4:
            contadores[4] += 1
        elif tabla[i].tipo == 5:
            contadores[5] += 1
        elif tabla[i].tipo == 6:
            contadores[6] += 1
        elif tabla[i].tipo == 7:
            contadores[7] += 1
        elif tabla[i].tipo == 8:
            contadores[8] += 1
        elif tabla[i].tipo == 9:
            contadores[9] += 1
        else:
            contadores[10] += 1
    for i in range(len(contadores)):
        if contadores[i] != 0:
            print('Cantidad de articulos de tipo:', i, ' cargados: ', contadores[i])


def mas_prom(tabla):
    total = may_prom = 0
    for i in range(len(tabla)):
        total += tabla[i].importe
        print('Importe', str(i + 1), ': ', tabla[i].importe)
    prom = round(total / len(tabla), 2)
    for i in range(len(tabla)):
        if tabla[i].importe > prom:
            may_prom += 1
    print('El promedio de importes es: ', prom)
    print('La cantidad de productos con mayor importe que el promedio es ', may_prom)


def productox(tabla):
    producto = None
    n = int(input('Ingrese el Numero de indetificacion de un producto: '))
    for i in range(len(tabla)):
        if not tabla[i].importe % 2 == 0 and tabla[i].numero_iden == n:
            producto = i
            break
    if producto is not None:
        print('\n Primer producto encontrado con importe impar y numero de indentificacion:', n, ':')
        print(to_string(tabla[producto], -1))
    else:
        print(' - No existen productos con importe impar con ese numero de identificacion.')


def menu(tabla):
    cargado = False
    eleccion = 0
    while eleccion != 6:
        print('\n', '=' * 80)
        print(' -------- MENU DE OPCIONES ---------')
        print('1 - Cargar datos de productos (aleatorio)')
        print('2 - Mostrar datos de los productos')
        print('2 - Cantidad de productos por tipo.')
        print('4 - Cantidad de productos con importe mayo al promedio.')
        print('5 - Producto de importe impar y con numero de indentificacion X:')

        eleccion = int(input('Ingrese una opcion: '))
        print('', '=' * 80)

        if eleccion == 1:
            carga_automatica(tabla)
            cargado = True

        elif eleccion == 2 and cargado:
            ordenar(tabla)
            mostrar(tabla)

        elif eleccion == 3 and cargado:
            cantxtipo(tabla)

        elif eleccion == 4 and cargado:
            mas_prom(tabla)

        elif eleccion == 5 and cargado:
            productox(tabla)

        elif eleccion == 6:
            print('Que tenga buen dia. :)')

        else:
            print('ERROR.. La opción ingresada es inválida o no cargó los datos(1)')


def validar(n):
    while n <= 0:
        print('\n ERROR.. La opcion ingresada debe ser positiva')
        n = int(input('Ingrese la cantidad de productos a cargar: '))

def test():
    print(' - Bienvenido al programa analizador de productos - ')
    n = int(input('Ingrese la cantidad de productos a cargar: '))
    validar(n)
    tabla = [None] * n
    menu(tabla)


if __name__ == '__main__':
    test()
