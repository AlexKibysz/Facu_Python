# Legajo: 85421
# DNI: 4412758
# Nombre: De Philippis Jérémie
'''
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir al
menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter
(a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

    Determinar la cantidad de palabras sin consonantes que posee el texto. Por ejemplo, en el texto:
    Elegir entre educación a distancia o presencial.
    Resultado: 2 palabras cumplen con la condición (“o” y "a").

    Determinar la cantidad de palabras que tienen una ‘x’ en la segunda mitad de la palabra. Por ejemplo, en el texto:
    El texto oxx trata del ave fenix.
    Resultado: 2 palabras cumplen con la condición (“oxx” y “fenix”).

    Determinar la cantidad de palabras que comienzan con un dígito y tienen una letra 'a' en la tercera posición.
    Por ejemplo, en el texto:
    "La 3ra temporada es mala pero la 2da es muy buena."
    tiene dos palabras que cumplen la
    consigna ("3ra" y "2da").

    Determinar el porcentaje de las palabras que finalizaron en “on”. Por ejemplo, en el texto:
    "En esta ocasión viajo en avión."
    hay 2 palabras que terminan en on ("ocasión" y "avión") por lo que el porcentaje
    sobre las 6 palabras del texto es de 33.33%.
'''


# es digito
def es_digito(car):
    return car in '0123456789'


# es vocal
def es_vocal(caracter):
    return caracter in 'aeiouAEIOU'


# es letra
def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'


# el porcentaje
def porcentaje(total, var):
    if total != 0:
        return var * 100 / total
    return 0


# es consonante
def es_consonante(caracter):
    return es_letra(caracter) and not es_vocal(caracter)


# analisis del texto
def analisis(texto):
    # contadores
    cant_palabras = cant_letras = sin_cons = con_x = posicion_x = eyt_3a = cant_on = 0
    tiene_consonante = contiene_x = emp_num_term_a = empieza_num = termina_on = False
    ant = ''
    # analisis
    for c in texto:
        # fuera text
        if c == ' ' or c == '.' or c == ',':
            if cant_letras > 0:
                cant_palabras += 1

            if not tiene_consonante and cant_letras > 0:
                sin_cons += 1

            if contiene_x and (posicion_x > cant_letras // 2):
                con_x += 1

            if emp_num_term_a:
                eyt_3a += 1

            if termina_on:
                cant_on += 1

            # reset
            cant_letras = posicion_x = 0
            tiene_consonante = contiene_x = empieza_num = emp_num_term_a = False

        # dentro text
        else:
            emp_num_term_a = termina_on = False
            cant_letras += 1
            if es_consonante(c):
                tiene_consonante = True

            if c in 'xX':
                contiene_x = True
                posicion_x = cant_letras

            if cant_letras == 1 and es_digito(c):
                empieza_num = True
            if empieza_num and cant_letras == 3 and c in 'aáAÁ':
                emp_num_term_a = True

            if ant in 'oóOÓ' and c in 'nN':
                termina_on = True
        ant = c
    term_on = porcentaje(cant_palabras, cant_on)
    return sin_cons, con_x, eyt_3a, term_on


def ppal():
    print('\033[1;35m*' * 60)
    print('\t\t\tSegundo parcial 💻 Analisis de texto')
    print('*' * 60, '\033[0m')
    texto = input('📩 Ingrese su texto: ')
    cant_sin_consonantes, cant_x, tiene_num_a, terminan_on = analisis(texto)
    print('\033[0;34m⋙La cantidad de palabras sin sonsonantes:\033[0m', cant_sin_consonantes)
    print('\033[0;34m⋙La cantidad de palabras con x después de la mitad de la palabra:\033[0m', cant_x)
    print('\033[0;34m⋙La cantidad de palabras que empiezan con Num. y termina con a:\033[0m', tiene_num_a)
    print('\033[0;34m⋙El porcentaje de palabras q termina con "on":\033[0m %', round(terminan_on, 2), sep='')

    print('\n\t\033[3;31mFin del programa.\033[0m')


if __name__ == '__main__':
    ppal()

