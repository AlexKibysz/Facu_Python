"""Se ha solicitado un programa que permita cargar las
precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:

    Determinar el promedio anual de lluvias
    Determinar el promedio de lluvias para un determinado trimestre
    Determinar el mes más seco del año
"""

#genera vector de meses del año y promedios en cada uno...
def carga(meses):
    lis = [0]*12
    for i in range(len(lis)):
        lis[i] = int(input('-->Ingrese el promedio del mes '+str(meses[i])+': '))
    return lis



def promedio(cant, lista):
    suma = prom = 0
    if len(lista) != 0:
        for i in range(cant):
            suma += lista[i]

        prom = suma / cant
    return prom


def menor_lista(lis):
    men = mes = 0
    for i in range(len(lis)):
        if men == 0:
            men = lis[i]
            mes = i
        elif lis[i] < men:
            men = lis[i]
            mes = i
    opcion3 = men, mes
    return opcion3


def validacion(inf):  # validacion de opcion correcta en menu de opciones.
    opcion = -1
    while opcion not in inf:
        opcion = int(input('\033[1;33m➥ Ingrese su opcion 🔎: \033[0m'))
        if opcion not in inf:
            print('\033[1;31mERROR: Porfavor seleccione una opcion valida.'
                  '\033[0m')
    return opcion



def promedio_trim(lis):
    opcion2 = [0]*4
    c = 0
    for i in range(len(opcion2)):
        opcion2[i] = (lis[c] + lis[c+1] + lis[c+2]) / 3
        c += 3
    return opcion2


def menu(opcion1, opcion2, opcion3, meses):

    opcion = 1
    while opcion != 0:
        print('\n\t\t\033[33;3;1m Menu de opciones:\033[0m'
              '\n-1.Promedio anual de lluvias'
                  '\n-2.Promedio de un trimeste en especifico'
                  '\n-3.El mes mas seco.'
                  '\n-0.>>Salir<<')
        opcion = validacion([1, 2, 3, 0])
        print('\t\t\t\033[43m"OPCION'+str(opcion)+'"\033[0m')
        if opcion == 1:
            print('\n-->El promedio anual de lluvias es de:', opcion1)
        elif opcion == 2:
            print('\n-->¿De que trimestre desea obtener el promedio? [1, 2, 3, 4]')
            prom_trime = 0
            trimestre = validacion([1,2,3,4])
            if trimestre == 1:
                prom_trime = opcion2[0]
            elif trimestre == 2:
                prom_trime = opcion2[1]
            elif trimestre == 3:
                prom_trime = opcion2[2]
            elif trimestre == 4:
                prom_trime = opcion2[3]
            print('-->El promedio del', trimestre, 'trimestre es:', prom_trime)
        elif opcion == 3:
            print('-->El mes mas seco fue:', meses[opcion3[1]], '\n\t\t-Con un total de:',
          opcion3[0], 'lluvias.')
        else:
            break


def principal():
    print('\t\t\033[1;7;33m====BIENVENIDO AL PROGRAMA=====\033[0m\n')
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
    lis = carga(meses)

    opcion1 = promedio(len(lis), lis)
    opcion3 = menor_lista(lis)
    opcion2 = promedio_trim(lis)

    menu(opcion1, opcion2, opcion3, meses)

    print('\nFin de programa.')




if __name__=='__main__':
    principal()
