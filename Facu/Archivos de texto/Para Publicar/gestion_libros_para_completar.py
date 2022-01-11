__author__ = 'Catedra de AED'

import random
import pickle
import os
import os.path

from RegistroLibro import *


def cargar_arreglo(v):
    n = int(input('Cuantos libros desea cargar?: '))
    for i in range(n):
        cod = random.randint(1, 10000)
        tit = 'Título ' + str(i)
        aut = 'Autor ' + str(i)
        lib = Libro(cod, tit, aut)
        v.append(lib)

def mostrar_arreglo(v):
    for i in range(len(v)):
        display(v[i])

# Generar un archivo desde el vector
# Almacenar cada registro del vector a un archivo: libros.dat
def crear_archivo(v, fd):

    m = open(fd, 'wb')

    # Completar ...

    m.close()
    print('Se creó el archivo', fd, 'con todos los registros del vector')
    print()

# Mostrar por pantalla cada uno de los registros almacenados en el archivo.
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return

    print('Contenido actual del achivo', fd, ':')
    m = open(fd, 'rb')

    # Completar ...

    m.close()
    print()

# Almacenar un vector de registros en un archivo.
def crear_archivo2(v, fd):

    m = open(fd, 'wb')

    # Completar ...
    # Se desea que al archivo contenga el vector de registros

    m.close()

# Mostrar por pantalla los datos del vector contenido en el arhivo.
def mostrar_archivo2(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return

    print('Contenido actual del achivo', fd, ':')
    m = open(fd, 'rb')

    # Completar ...
    # Si el archivo contenía un vector...

    m.close()

# Almacenar en un archivo los registros del vector cuyo codigo ISBN sea mayor a x, siendo x
# un valor pasado por parametro
def crear_archivo_algunos(v, fd,x):

    m = open(fd, 'wb')

    # completar

    m.close()

# Crear un archivo de registros de tipo Libro
# generando los datos de forma aleatoria
def crear_archivo_desde_teclado():
    pass


# Leer los registros almacenados en un archivo y almacenarlos en un vector.
def crear_arreglo_desde_archivo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return

    m = open(fd, 'rb')

    # Si el archivo contenía los registros almacenados
    # uno a uno en forma secuencial...


    m.close()



def test():
    v = []
    fd = 'libros.dat'
    op = -1
    while op != 6:
        print('Procesamiento combinado de arreglos, registros y archivos...')
        print('1. Crear el arreglo de libros (en forma automática)')
        print('2. Mostrar el arreglo de libros')
        print('3. Almacenar los datos del vector en un archivo: libros.dat')
        print('4. Mostrar el archivo datos.dat')
        print('5. Crear un archivo con los libros del arreglo de ISBN igual a x')
        print('6. Salir')

        op = int(input('\t\tIngrese número de opción: '))
        print()

        if op == 1:
            cargar_arreglo(v)
        else:
            if len(v) != 0:
                if op == 2:
                    print('Los libros registrados son:')
                    mostrar_arreglo(v)

                elif op == 3:
                    # Enviar los registros del vector a un archivo: libros.dat
                    crear_archivo(v, fd)

                elif op == 4:
                    # Leer los registros almacenados en el archivo y mostrarlos por pantalla
                    mostrar_archivo(fd)

                elif op == 5:
                    # Crear un archivo con los registros del vector cuyo número de ISBN
                    # sea igual a x, donde x se ingresa desde teclado.
                    x = int(input('Ingrese el código a comparar: '))
                    crear_archivo_algunos(v, fd,x)
                    print('Se creó el archivo', fd, 'con los registros con código: ', x)

                elif op == 6:
                    print('Fin de programa')
            else:
                print(' Aún no se registraron datos ... ')
        print()

if __name__ == '__main__':
    test()
