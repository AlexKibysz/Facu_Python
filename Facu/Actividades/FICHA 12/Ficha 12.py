'''1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio
en cada mes del país, en base a esos datos armar un menú de opciones que
permita:

1 Determinar el promedio anual de lluvias
2 Determinar el promedio de lluvias para un determinado trimestre
3 Determinar el mes más seco del año
4 Determinar los meses del año en los que llovió más que el promedios de
lluvia de todo el año'''


def carga():
    lista_numeros = []
    for i in range(12):
        x = int(input(f'Ingrese el {i + 1} mes:'))
        lista_numeros.append(x)
    print('la lista generada fue: ', lista_numeros)
    return lista_numeros


def promedio(numero, total):
    calculo = round(numero / total, 2)
    return calculo


def sumatoria(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def trimestre_promedio(lista, trimestre):
    if trimestre == 1:
        trimestre_1 = lista[:3]
        print(trimestre_1)
        return promedio(sumatoria(trimestre_1), 3)
    if trimestre == 2:
        trimestre_2 = lista[3:6]
        print(trimestre_2)
        return promedio(sumatoria(trimestre_2), 3)
    if trimestre == 3:
        trimestre_3 = lista[6:9]
        print(trimestre_3)
        return promedio(sumatoria(trimestre_3), 3)
    if trimestre == 4:
        trimestre_4 = lista[9:]
        print(trimestre_4)
        return promedio(sumatoria(trimestre_4), 3)


def menor_cant(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = i + 1
    return menor


def mayor_prom(lista, promedio):
    mayores = []
    for i in range(len(lista)):
        if lista[i] > promedio:
            mayores.append(i + 1)
    return mayores


def menu():
    print('Bienvenido al asistente FoxRain❤ por favor ingrese los datos')
    lluvias = carga()
    # lluvias= [12, 32, 43, 65, 34, 23, 54, 76, 98, 34, 2, 4]
    total = sumatoria(lluvias)
    promediof = promedio(total, 12)
    restart = 'no'
    while restart == 'no':
        print('*' * 50, 'Opciones', '*' * 50)
        print()
        print('1. Determinar el promedio anual de lluvias\n'
              '2. Determinar el promedio de lluvias para un determinado trimestre\n'
              '3. Determinar el mes más seco del año\n'
              '4. Determinar los meses del año en los que llovió más '
              'que el promedios de lluvia de todo el año')

        opcion = int(input('\nElija una opcion: '))
        if opcion == 1:
            print('la sumatoria de precipitaciones es de: ', total,
                  'y el promedio'
                  , ' anual es de: ', promediof)
        if opcion == 2:
            print('ingrese trimestre para ver su promedio de precipitaciones')
            x = int(input('que trimestre desea analizar?(1 al 4): '))
            print(f'el promedio de lluvias en el', x, 'trimestre fue: ',
                  trimestre_promedio(lluvias, x))
        if opcion == 3:
            print('el mes mas seco fue: ', menor_cant(lluvias))
        if opcion == 4:
            print(f'los meses del año en que llovio mas fueron: ',
                  mayor_prom(lluvias, promediof))
        restart = input('Quiere finalizar el programa [si o no]: ')


menu()
'''2. Último y Primero
Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:

Informe cuántas veces se repite en el vector el último número ingresado
Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.'''


def carga():
    vector = []
    n = int(input('Ingrese cuantos valores quiere cargar al vector: '))
    if n == 0:
        return vector
    else:
        for i in range(n):
            numero = int(input(f'ingrese valor del {i + 1} elemento: '))
            vector.append(numero)
        return vector


def lista_menores(lista):
    menores = []
    menor = lista[0]
    for i in range(len(lista)):
        if menor > lista[i]:
            menores.append(lista[i])
    return menores


def repetcion(lista):
    repetidas = 0
    for i in range(len(lista)):
        if lista[i] == lista[-1]:
            repetidas += 1
    return repetidas


def principal():
    lista = carga()
    punto_1 = repetcion(lista)
    print('las veces que se repite el ultimo numero incluyendolo son: ',
          punto_1)
    punto_2 = lista_menores(lista)
    print('la lista con valores menores al primero es: ', punto_2)


principal()

'''3. Busqueda de primos
Desarrollar un programa que permita generar un arreglo de n elementos,
a partir del arreglo:

Generar un segundo vector con todos aquellos números primos
Determinar el promedio del vector generado en el punto 1'''


def carga():
    vector = []
    n = int(input('Ingrese cuantos valores quiere cargar al vector: '))
    if n == 0:
        return vector
    else:
        for i in range(n):
            numero = int(input(f'ingrese valor del {i + 1} elemento: '))
            vector.append(numero)
        return vector


def esPrimo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def lista_primos(lista):
    primos_lista = []
    for i in range(len(lista)):
        if esPrimo(lista[i]):
            primos_lista.append(lista[i])
    return primos_lista


def sumatoria(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def promedio(lista):
    prom = sumatoria(lista) / len(lista)
    return prom


def principal():
    vector = carga()
    print('la lista principal es: ', vector)
    print('la lista de los numeros primos segun la primera es: ',
          lista_primos(vector))
    print('el promedio de la primera lista es: ', promedio(vector))


principal()
'''4. Mayores con el mismo índice
Cargar por teclado dos vectores de tamaño n y, a partir de ellos, generar un
tercer vector que contenga, para cada componente, el mayor valor entre las
componentes homólogas (mismo índice) de los otros dos vectores.
Por ejemplo, si se cargan los siguientes vectores a y b:

a = [3, 4, 6]

b = [8, 5, 1]

El resultado sería:
c = [8, 5, 6]'''


def carga():
    vector1 = []
    vector2 = []
    n = int(input('Ingrese cuantos valores quiere cargar al vector: '))
    if n == 0:
        return vector1, vector2
    else:
        for i in range(n):
            numero = int(
                input(f'vector 1 ingrese valor del {i + 1} elemento: '))
            vector1.append(numero)
        print('*' * 100)
        for i in range(n):
            numero = int(
                input(f'vector 2 ingrese valor del {i + 1} elemento: '))
            vector2.append(numero)
        return vector1, vector2


def lista_mayores(lista1, lista2):
    lista = []
    for x in range(len(lista1)):
        if lista1[x] > lista2[x]:
            lista.append(lista1[x])
        else:
            lista.append(lista2[x])
    return lista


def principal():
    vectores = carga()
    print('vector 1: ', vectores[0])
    print('vector 2: ', vectores[1])
    print(lista_mayores(vectores[0], vectores[1]))


principal()
'''5. Mayores al promedio
Ingresar por teclado un arreglo unidimensional de números enteros de tamaño n,
siendo n una variable que se ingresa por teclado. Se pide:

Calcular el valor promedio entre los números ingresados en el vector.
Determinar la cantidad de números del vector que son mayores al promedio.'''


def carga():
    vector = []
    n = int(input('Ingrese cuantos valores quiere cargar al vector: '))
    if n == 0:
        return vector
    else:
        for i in range(n):
            numero = int(input(f'ingrese valor del {i + 1} elemento: '))
            vector.append(numero)
        return vector


def sumatoria(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def promedio(lista):
    prom = sumatoria(lista) / len(lista)
    return prom


def mayores(lista):
    prom = promedio(lista)
    may = 0
    for i in range(len(lista)):
        if lista[i] > prom:
            may += 1
    return may


def principal():
    lista = carga()
    print('la lista creada es: ', lista)
    print('el promedio de la lista es: ', promedio(lista))
    print('la cantidad de vectores mayores al promedio en la lista es: ',
          mayores(lista))

principal()
