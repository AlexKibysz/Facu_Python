"""4. Mayores con el mismo índice
Cargar por teclado dos vectores de tamaño n y, a partir de ellos,
 generar un tercer vector que contenga, para cada componente, el mayor
 valor entre las componentes homólogas (mismo índice) de los otros dos vectores."""


def validar():
    n = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    while n < 0:
        n = int(input("Ingrese un numero mayor a 0 por favor: "))
    return n


def principal():
    n = validar()
    g = [0] * n
    h = [0] * n
    d = [0] * n

    for i in range(len(g)):
        g[i] = input("Ingrese un numero para el PRIMER vector")
        h[i] = input("Ingrese un numero para el SEGUNDO vector")

        if g[i] > h[i]:
            mayor = g[i]
        else:
            mayor = h[i]
        for a in range(len(h)):
            d[i] = mayor

    print("Vector 1 : ", g)
    print("Vector 2 : ", h)
    print("EL nuevo vector : ", d)


if __name__ == '__main__':
    principal()
