"""
Una tienda dedicada a la venta de productos para el hogar, desea un programa para procesar los datos de los productos
que tiene a la venta. Por cada producto se tienen los siguientes datos:
-número de identificación del producto,
-la descripción del producto,
-el importe del producto
-el tipo de producto (un valor entre 0 y 10 ambos incluidos,de la forma 0: Muebles, 1: Jardín, 2: Bazar, etc.).
Se desea almacenar la información referida a los n productos en un
arreglo de registros de tipo Producto (definir el tipo Producto y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:

1   Cargar el arreglo pedido con los datos de los n productos.
    Valide que el tipo de producto sea un valor entre 0 y 10 (ambos incluidos).
    Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
    o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2    Mostrar todos los datos de los productos, en un listado ordenado de mayor a menor según el importe de los productos.

3    Usando el arreglo creado en el punto 1, determine la cantidad de productos por cada tipo de producto
    (o sea, 11 contadores). Muestre sólo los resultados mayores a 0.

4    Determinar cuál es la cantidad de productos que tienen un importe mayor al importe promedio de todos los productos.

5    Determinar si existe un producto cuyo importe sea impar y su número de identificación sea igual a x
    (siendo x un valor que se carga por teclado). Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
    Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
"""
import random


class Venta:
    def __init__(self, ident, descrip, costo, tipo):
        self.identificacion = ident
        self.descripcion = descrip
        self.costo = costo
        self.tipo = tipo


def validar_intervalo(min_, max_, msg):
    n = int(input(msg))
    while n < min_ or n > max_:
        print('\033[3;1;31mERROR: Ingrese valor entre', min_, 'y', max_, '\033[0m')
        n = int(input(msg))
    return n


def validar_mayor_que(min_, msg):
    n = int(input(msg))
    while n <= min_:
        print('\033[3;1;31mERROR: Ingrese valor mayor a', min_, '\033[0m')
        n = int(input(msg))
    return n


def to_string(v):
    show = 'Numero de indentificacion: {:^6} | Descripcion: {:<12} | Costo: {:>6} | Tipo: {}'
    print(show.format(v.identificacion, v.descripcion, v.costo, v.tipo))


def menu():
    print('\033[33m≣' * 30, '\033[0m')
    print('1. Cargar datos'
          '\n2. Mostrar datos por el precio mas alto.'
          '\n3. Mostrar la cantidad de productos por tipo.'
          '\n4. Mostrar datos con precio mayor al promedio.'
          '\n5. Mostrar datos de un producto de importe impar, identificacion manual.'
          '\n0. Salir')
    op = validar_intervalo(0, 5, '\tSu opcion:')
    print('\033[33m≣' * 30, '\033[0m')
    return op


# ================ opcion 1
def cargar():
    print('\033[34m≣' * 30, '\033[0m')
    n = validar_mayor_que(0, 'Cantidad de datos a cargar: ')
    v = [None] * n
    for i in range(n):
        identificacion = random.randrange(100, 1000)
        descripcion = random.choice(['Nuevo', 'Usado', 'Casi Nuevo', 'Degastado', 'Antiguo'])
        costo = random.randint(500, 2000)
        tipo = random.randint(0, 10)
        v[i] = Venta(identificacion, descripcion, costo, tipo)
        print('Se cargó el', str(i + 1) + '° Producto.')
    print('\033[34m≣' * 30, '\033[0m')
    return v


# ================ opcion 2
def ordenar_por_precio(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].costo < v[j].costo:
                v[i], v[j] = v[j], v[i]


def opcion2(v):
    ordenar_por_precio(v)
    print('\033[36m≣' * 30, '\033[0m')
    for i in range(len(v)):
        to_string(v[i])
    print('\033[36m≣' * 30, '\033[0m')


# ================ opcion 3
def cant_productos_por_tipo(v):
    cant = [0] * 11
    for i in range(len(v)):
        cant[v[i].tipo] += 1
    print('\033[35m≣' * 30, '\033[0m')
    for i in range(len(cant)):
        if cant[i] != 0:
            print('Cantidad para el tipo', str(i) + ':', cant[i])
    print('\033[35m≣' * 30, '\033[0m')


# ================ opcion 4
def prom(v):
    suma = 0
    for i in range(len(v)):
        suma += v[i].costo
    return round(suma / len(v), 2)


def mostrar_mayor_al_prom(v):
    promedio = prom(v)
    contador = 0
    print('\033[35m≣' * 30, '\033[0m')
    for i in range(len(v)):
        if v[i].costo > promedio:
            to_string(v[i])
            contador += 1
    print('\tEn total hubo', contador, 'Productos mayores al promedio')
    print('\033[35m≣' * 30, '\033[0m')


# ================ opcion 5
def mostrar_importe_impart_tipo_x(v):
    print('\033[35m≣' * 30, '\033[0m')
    tipo = validar_intervalo(0, 10, 'Ingrese el numero tipo que busca: ')
    ban = False
    for i in range(len(v)):
        if v[i].costo % 2 != 0 and v[i].tipo == tipo:
            to_string(v[i])
            ban = True
            break
    if not ban:
        print('\033[31mNo se encontró ningun producto con las especificaciones.\033[0m')
    print('\033[35m≣' * 30, '\033[0m')


# ================ principal
def ppal(op=-1):
    cargo = False
    while op != 0:
        op = menu()
        if op == 1:
            v = cargar()
            cargo = True
        elif cargo:
            if op == 2:
                opcion2(v)
            elif op == 3:
                cant_productos_por_tipo(v)
            elif op == 4:
                mostrar_mayor_al_prom(v)
            elif op == 5:
                mostrar_importe_impart_tipo_x(v)
        elif op == 0:
            print('\033[32m≣' * 30, '\033[0m')
            print('Hasta luego!')
            print('\033[32m≣' * 30, '\033[0m')
        else:
            print('\033[1;3;31mNo se cargó la base de datos.\033[0m')


if __name__ == '__main__':
    ppal()
