from registro import *
import random


# Función para cargar el vector de forma automática
def crear_vector(vec_polizas, n):
    # Variable auxiliar
    nombres = ('José', 'Martín', 'Julieta', 'Silvio', 'Jorge', 'Cristian', 'Martina', 'Ricardo', 'Agustín')

    # Ciclo de creación
    for i in range(n):
        identificacion = random.randint(1, 99)
        nombre = random.choice(nombres)
        tipo = random.randint(0, 19)
        costo = random.randint(2000, 10000)

        # Asignación...
        casillero = Poliza(identificacion, nombre, tipo, costo)
        vec_polizas.append(casillero)


# Función para ordenar el vector de mayor a menor por nombres
def ordenar_por_nombres(vec_polizas):
    n = len(vec_polizas)

    # Ciclos
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec_polizas[i].nombre < vec_polizas[j].nombre:
                vec_polizas[i], vec_polizas[j] = vec_polizas[j], vec_polizas[i]


# Función para mostrar el vector de pólizas
def mostrar_vector(vec_polizas):
    for poliza in vec_polizas:
        print(to_string(poliza))


# Función para validar cargas
def validar_carga(mensaje, limite_inferior):
    num = limite_inferior - 1

    while num < limite_inferior:
        num = int(input(mensaje))
        if num < limite_inferior:
            print('\n>>> Ingresaste un número menor a', limite_inferior, ', probá de vuelta')

    return num


# Función para contar la cantidad total de cada tipo de póliza
def contar_tipo(vec_polizas):
    # Vector de conteo
    conteo = [0] * 20

    # Ciclo de analisis
    for poliza in vec_polizas:
        conteo[poliza.tipo] += 1

    return conteo


# Función para mostrar el vector de conteo
def mostrar_conteo(vec_conteo):
    for i in range(len(vec_conteo)):
        print('-Cantidad de pólizas del tipo', i, ': ', vec_conteo[i])


# Función para determinar el costo mensual promedio (punto 4)
def punto_4(vec_polizas):
    # Variables auxiliares
    tipos = (2, 5, 9)
    contador = 0
    acumulador = 0

    # Ciclo de análisis
    for poliza in vec_polizas:
        if poliza.tipo in tipos:
            contador += 1
            acumulador += poliza.costo

    # Cálculo del promedio
    promedio = 0
    if contador > 0:
        promedio = acumulador / contador

        # Muestra del promedio
        print('> El costo mensual promedio entre las pólizas de tipo 2, 5, y 9 es: $', promedio)

        # Muestra de los datos de las pólizas del mismo tipo cuyo costo es menor al promedio
        print('> Polizas de estos tipos, cuyo costo sea menor al promedio: \n')
        cuenta = 0
        for poliza in vec_polizas:
            if (poliza.tipo in tipos) and (poliza.costo < promedio):
                cuenta += 1
                print(to_string(poliza))

        if cuenta == 0:
            print('-No hay polizas cuyo costo sea menor al promedio...')

    else:
        print('> El costo mensual promedio entre las pólizas de tipo 2, 5, y 9 es: $', promedio)
        print('> No existen polizas de estos tipos...')


# Función para buscar por numero de identificacion y costo mensual
def buscar_por_numero_costo(vec_polizas, x, c):
    for poliza in vec_polizas:
        if (poliza.identificacion == x) and (poliza.costo > c):
            return poliza
    return None
