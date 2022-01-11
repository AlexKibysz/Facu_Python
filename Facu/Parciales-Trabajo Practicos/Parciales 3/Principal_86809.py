"""El puerto de una ciudad pide un programa para procesar los datos de los barcos que estan
siendo cargados en sus muelles. Por cada barco se conoce su patente (una cadena), empresa
a la que pertenece, tipo de carga que llevará (un valor del 0 al 14, por ejemplo: 0: Soja,
1: Maiz, 2: Gas Licuado etc.) y la cantidad de dias que estará en puerto. Se desea almacenar
la información referida a los n barcos  en un arreglo de registros de tipo Barco
(definir el tipo Barco  y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones,
que permita gestionar las siguientes tareas:

    Cargar el arreglo con los datos de los n barcos. Valide que la cantidad de dias
    que estará en puerto sea mayor a cero y que el tipo de carga esté en el rango
    especificado. Puede hacer la carga en forma manual, o puede generar los datos en
    forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo
     desea. Pero al menos una debe programar.

    Mostrar todos los datos de todos barcos, en un listado ordenado de mayor a menor
    según las patentes de los barcos.

    Determinar la cantidad total de barcos por cada tipo de carga que se carga en el puerto,
    15 contadores en total enn un vcetor de conteo.

    Determinar el barco con menor cantidad de días en el puerto entre los barcos cuyo tipo
    de carga es 0, 1, o 2.

    Determinar si existe un barco cuya empresa propietaria sea igual x y su tipo de carga sea
    8, siendo x un valor que se carga por teclado. Si existe, mostrar sus datos. Si no existe,
    informar con un mensaje. Si existe mas de un registro que coincida con esos parámetros de
    búsqueda, debe mostrar sólo el primero que encuentre.

Criterios generales de evaluación:

    Desarrollo del programa completo, incluyendo el menú correctamente planteado,
    funciones correctamente diseñadas, parametrizadas y retornando valores (cuando sea apropiado) y
    validaciones: [máximo: 10 puntos (16.66% del puntaje)]
    Desarrollo correcto del ítem 1: [máximo: 10 puntos (16.66% del puntaje)]
    Desarrollo correcto del ítem 2: [máximo: 10 puntos (16.66% del puntaje)]
    Desarrollo correcto del ítem 3: [máximo: 10 puntos (16.66% del puntaje)]
    Desarrollo correcto del ítem 4: [máximo: 10 puntos (16.66% del puntaje)]
    Desarrollo correcto del ítem 4: [máximo: 10 puntos (16.66% del puntaje)]
    Para aprobar el parcial, el alumno debe llegar a un total acumulado de al menos 55% del
     puntaje (es decir, alrededor de 33 puntos acumulados), pero obligatoriamente debe estar desarrollado
     el programa funcionando y operativo, usando el vector de registros pedido, y planteado con
     funciones correctamente planteadas (usando pámetros y retornos cuando corresponda).
"""
import random

_author_ = 'Bianca Cano 1k2 86809'
# Modulo en el que se definen las clases y otras funciones  autilizar en Principal_86809


class Barco:
    def __init__(self, patente, empresa, tipo, dias):
        self.patente = patente
        self.empresa = empresa
        self.tipo = tipo
        self.dias = dias


def separar():
    print('=' * 70)


def validar_intervalo(n1, n2, inf):
    num = n1 - 1
    while num < n1 or num > n2:
        num = int(input(inf))
        if num < n1 or num > n2:
            print('\033[31mERROR: ingrese un valor mayor a', n1, 'y menor a',
                  n2, '\033[0m')
    return num


def validar_mayor_que(n, inf):
    num = n
    while num <= n:
        num = int(input(inf))
        if num <= n:
            print('\033[31mERROR: Porfavor ingrese un valor mayor a', n,
                  '\033[0m')
    return num


def to_string(barco):
    cad = 'Patente:{:>8} | Empresa:{:>10} | Tipo:{:>3} | Dias:{:>5}'
    return cad.format(barco.patente, barco.empresa, barco.tipo, barco.dias)


def ordenar_x_patente(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].patente.lower() < v[j].patente.lower():
                v[i], v[j] = v[j], v[i]


def contar_tipos(barcos):
    cont = [0] * 15
    for i in range(len(barcos)):
        cont[barcos[i].tipo] += 1
    return cont


# ===================================OPCION 1==================================
# Esta es la opcion en la que se cargaran los vectores y se haran las validaciones iniciales

def opcion1(barcos):
    # Se valida n para que no se pida el largo de un vectos nulo o negativo
    n = validar_mayor_que(0, '+ Cuantos Barcos desea cargar?: ')
    manual_or_random = validar_intervalo(1, 2,
                                         '\t\t(Manual = 1 / Automatico = 2)'
                                         '\n>> Como desea cargar el vector?: ')
    if manual_or_random == 1:
        carga_manual(barcos, n)
    elif manual_or_random == 2:
        carga_automatica(barcos, n)
    print('\033[33m Datos cargados con exito!!\033[0m')


def carga_manual(barcos, n):
    for i in range(n):
        separar()
        print('BARCO [', i+1, ']')
        patente = input('+ Patente: ')
        empresa = input('+ Empresa propietaria: ')
        tipo = validar_intervalo(0, 14, '+ Tipo de carga: ')
        dias = validar_mayor_que(0, '+ Dias que estara en el puerto: ')
        barcos.append(Barco(patente, empresa, tipo, dias))


def carga_automatica(barcos, n):
    lis = ['AGA', 'SOR', 'MAT', 'CCL', 'STR', 'AED']
    for i in range(n):
        patente = random.choice(lis) + str(random.randint(100, 999))
        empresa = random.choice(lis)
        tipo = random.randint(0, 14)
        dias = random.randint(1, 100)
        barcos.append(Barco(patente, empresa, tipo, dias))


# ===================================OPCION 2==================================

def opcion2(barcos):
    print('>> Datos de todos los Barcos <<')
    print('\t\t\033[3mOrdenados de mayor a menor segun sus patentes...\033[0m')
    ordenar_x_patente(barcos)
    mostrar_vector(barcos)


# Ordenados por patente en orden alfabetico inverso, de Z a A
def mostrar_vector(barcos):
    for i in range(len(barcos)):
        s = to_string(barcos[i])
        print(s)
        separar()


# ===================================OPCION 3==================================

# Determinar la cantidad total de barcos por cada tipo de carga que se carga en el puerto

def opcion3(barcos):
    print('\n\t>> ❌ = No hubo barcos con este tipo de carga.')
    print('Barcos por cada tipo de carga:')
    cont = contar_tipos(barcos)
    mostrar_contador(cont)


def mostrar_contador(cont):
    for i in range(len(cont)):
        print('Tipo [', i, ']:', end=' ')
        if cont[i] != 0:
            print(cont[i])
        else:
            print('\033[31m❌\033[0m')


# ===================================OPCION4===================================

def opcion4(barcos):
    """ Determinar el barco con menor cantidad de días en el puerto entre los barcos cuyo tipo
    de carga es 0, 1, o 2."""
    men = menor_en_rango(barcos)
    if men != -1:
        print('>> Barco con menor cantidad de dias en el puerto: ')
        print(to_string(barcos[men]))
    else:
        print('\033[31mNo hubo ningun barco de tipo 0, 1 o 2\033[0m')


def menor_en_rango(barcos):
    band = False
    men = 0
    for i in range(len(barcos)):
        if barcos[i].tipo in range(0, 3):
            if not band:
                men = i
                band = True
            elif barcos[i].dias < barcos[men].dias:
                men = i
    if not band:
        men = -1
    return men


# ===================================OPCION5===================================


def opcion5(barcos):
    print('\033[3m(Recuerde que el tipo de carga debe ser = a 8)\033[0m')
    x = input('+ Ingrese empresa a buscar: ')
    val = buscar_en_vector(barcos, x)
    if val != -1:
        print('\033[33m\tBarco encontrado!!\033[0m')
        print(to_string(barcos[val]))
    else:
        print(
            '\033[31mNo hubo ningun barco que cumpliera con las caracteristicas..\033[0m')


def buscar_en_vector(barcos, x):
    for i in range(len(barcos)):
        if (barcos[i].empresa == x) and (barcos[i].tipo == 8):
            return i
    return -1


# ============================MENU y Principal=================================

def menu():
    separar()
    print('\t\t>> Menu de Opciones <<'
          '\n1. Cargar datos. '
          '\n2. Mostrar datos de los Barcos. '
          '\n3. Determinar la cantidad total de barcos por cada tipo de carga.'
          '\n4. Determinar el barco con menoa días entre los barcos cuyo tipo de carga es 0, 1, o 2'
          '\n5. Determinar si existe un barco cuya empresa sea x y su tipo de carga sea 8'
          '\n0. SALIR.')
    op = int(input('>> Ingrese una opcion: '))
    separar()
    return op


def principal():
    print('>> ¡Bienvenido al programa!\n')
    print('{:^60}'.format(
        '\033[1;3;33m💫 Parcial Nro3 - Bianca Cano 💫\033[0m\n'))
    barcos = []
    op = -1
    datos = False
    while op != 0:
        op = menu()
        if (op in range(2, 6) and datos) or op == 1:
            print('\t\t\t\033[1;33m 💥 OPCION', op, '💥\033[0m')
        if op == 1:
            opcion1(barcos)
            datos = True
        elif datos:
            if op == 2:
                opcion2(barcos)
            elif op == 3:
                opcion3(barcos)
            elif op == 4:
                opcion4(barcos)
            elif op == 5:
                opcion5(barcos)
            elif op != 0:
                print('Esa opcion no existe...')
        elif op != 0:
            print('\033[31mERROR: Primero cargue valores..\033[0m')
    print('Fin de programa.. \n\t\tHasta la proxima!')


if __name__ == '__main__':
    principal()
