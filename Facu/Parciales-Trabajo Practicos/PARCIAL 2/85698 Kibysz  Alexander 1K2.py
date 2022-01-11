_author_ = 'Alexander Kibysz 85698 1K2'
print('\033[1;35m※' * 50)
print('\033[1;35m※' * 17, "Analisis De Texto", '※' * 23)
print('※' * 50)

'''Se pide desarrollar un programa en Python que permita cargar por teclado
 un texto completo en una variable de tipo cadena de caracteres. 
 El texto finaliza con ‘.’ y se supone que el usuario cargará el
  punto para indicar el final del texto, y que cada palabra de ese 
  texto está separada de las demás por un espacio en blanco. 
  El programa debe incluir al menos una función simple con parámetros 
  y retorno de resultado, debe procesar el texto caracter a caracter 
  (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin 
  usar un menú de opciones:'''


# 1
# Determinar la cantidad de palabras sin consonantes que posee el texto.
# Por ejemplo, en el texto: “Elegir entre educación a distancia o presencial.”
# Resultado: 2 palabras cumplen con la condición (“o” y "a").
# 2
# Determinar la cantidad de palabras que tienen una ‘x’ en la segunda mitad de
# la palabra. Por ejemplo, en el texto: “El texto oxx trata del ave fenix.”
# Resultado: 2 palabras cumplen con la condición (“oxx” y “fenix”).
# 3
# Determinar la cantidad de palabras que comienzan con un dígito y tienen una
# letra 'a' en la tercera posición. Por ejemplo, en el texto:
# "La 3ra temporada es mala pero la 2da es muy buena." tiene dos
# palabras que cumplen la consigna ("3ra" y "2da").
# 4
# Determinar el porcentaje de las palabras que finalizaron en “on”.
# Por ejemplo, en el texto: "En esta ocasión viajo en avión."
# hay 2 palabras que terminan en on ("ocasión" y "avión")
# por lo que el porcentaje sobre las 6 palabras del texto es de 33.33%.

# funciones


def porcentaje(palabras_esp, total):
    if total != 0:
        operacion = (palabras_esp * 100) / total
        return operacion
    else:
        return 0


def es_consonante(car):
    if car in 'BbCcDdFfGgHhJjKkLlMmÑñPpQqRrSsTtVvWwXxYyzZ':
        return True
    else:
        return False


def no_digit(x):
    digitos = '1234567890'
    if x != digitos:
        return True
    else:
        return False


# contadores

cont_palabra_total = letra = palabra_x = palabra_sin_consonante = \
    palabra_con_digitoa = palabra_x = cont_palabra_on = 0
palabra = anterior = None

# variables

vocales = 'aeiouáéíóú'
digito = '1234567890'
palabra = ''
var_o = 'óoO'

# banderas

sin_digito = False

print('\033[1;39mParcial 2 \033[0m')
print('Ingrese texto con punto "." al finalizar como por ejemplo'
      ' ejemplo: (hola como estas.) ')

texto = input('↪: ')
texto = texto.lower()

for carac in texto:
    # letras

    if carac != '.' and carac != ' ':
        palabra += carac

        if no_digit(carac):
            sin_digito = True

        if not no_digit(carac):
            sin_digito = False

        if es_consonante(carac):
           consonante= True

        if carac in digito:
            es_vocal = False

        if carac in vocales:
            es_vocal = True
        anterior_anterior=anterior
        anterior = carac
        
# palabra

    else:
        cont_palabra_total += 1
        #validacion si es palabra sin consonantes

        if not consonante:
            palabra_sin_consonante += 1

        #reseteo de banderas

        consonante=False
        sin_digito = False
        es_vocal=False

        #si tiene digito en la primera parte de la palabra y en la 3 a

        if (palabra[0] in digito) and palabra[2] == 'a':
            palabra_con_digitoa += 1

        #si termina en on

        if len(palabra)>3:
            if palabra[-1] == 'n' and palabra[-2] == 'o' or palabra[-2] == 'ó':
                cont_palabra_on += 1

        #segunda mitad x
        for analisis in range(round(len(palabra) / 2)):
            if analisis != 0 and palabra[-analisis] == 'x':
                palabra_x += 1
        palabra = ''


#resultados
print('Palabra sin consonantes', palabra_sin_consonante)
print('Palabra con x en la segunda mitad', palabra_x)
print('Palabra con digito en la primera posicion y en la tercera a: ',
      palabra_con_digitoa)
print('El porcentaje de palabras que finalizan con on es: ',
      porcentaje(cont_palabra_on, cont_palabra_total))
