# validación
def cargar_entre(desde, hasta, mensaje="Ingrese un valor:"):
    val = int(input(mensaje))
    while val < desde or val > hasta:
        print("Error, el valor debe estar entre", desde, "y", hasta,"!")
        val = int(input(mensaje))
    return val


# caracteres
def es_digito(car):
    return car in "0123456789"

def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


def es_letra(car):
    return es_vocal(car) or es_consonante(car)


def es_mayuscula_v1(car):
    return car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def es_mayuscula_v2(car):
    return es_letra(car) and car == car.upper()


def prueba():
    a = cargar_entre(5,7)
    print(a)

# script principal
if __name__ == '__main__':
    prueba()


