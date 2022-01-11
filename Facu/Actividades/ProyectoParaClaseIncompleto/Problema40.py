# PROBLEMA 40
#
# Desarrollar un programa que permita cargar por teclado dos arreglos de números enteros
# de n y m componentes respectivamente, y genere y muestre un tercer arreglo que contenga
# los valores que aparecen repetidos en los dos arreglos originales.

def validar_mayor_que(mensaje, valor):
    tam = int(input(mensaje))
    while tam <= valor:
        print('ERROR')
        tam = int(input(mensaje))
    return tam

def read(v):
    n = len(v)
    print('Cargue ahora los datos de este arreglo...')
    for i in range(n):
        v[i] = int(input('Valor[' + str(i) + ']: '))

# HAY QUE COMPLETAR
def generate(v1, v2):
    v3 = []
    for i in range(len(v1)):
      for j in range(len(v2)):
        if v1[i] == v2[j]:
            # si v1[i] esta en v2[j] lo agrego al vector v3
            v3.append(v1[i])
    # retornar el nuevo arreglo...
    return v3

def test():

    # Primer Arreglo
    tam = validar_mayor_que('Ingrese el tamaño del primer vector: ', 0)
    v1 = [0] * tam
    read(v1)

    # Segundo Arreglo
    tam = validar_mayor_que('Ingrese el tamaño del segundo vector: ', 0)
    v2 = [0] * tam
    read(v2)

    # Generar el Tercer Arreglo
    v3 = generate(v1, v2)
    print('Los valores presentes en ambos arreglos son:', v3)

if __name__ == '__main__':
    test()
