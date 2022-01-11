'''
1. Determinar la cantidad de palabras que tuvieron más de 3 caracteres.
2. Determinar el porcentaje de palabras que contienen 'si' y 'no'.
3. Determinar la cantidad de palabras que incluyeron la sílaba 'de'.
4. Determinar cuantas palabras tuvieron 'u' y terminaron en 'lo'
5. Determinar la posición de la palabra más larga del texto
6. Determinar la cantidad de palabras que incluyen 'll' y tienen cantidad de letras par.
7. Determinar la cantidad de palabras que comienzan con la última letra de la primera palabra del texto y tienen más de 2 vocales
8- Determinar la cantidad de palabras que contienen 'de' en la primera mitad de la palabra.





'''
texto = input('ingrese texto a anlizar con punto finaliza ejemplo (hola '
              'como estas.): ')
texto = texto.lower()
# contadores
palabra = letra = palabra_con_3_letras = letras_3 = palabras_con_si = \
    palabras_con_no = palabra_con_de = \
    palabras_u_lo = may = pos = palabra_con_ll = cont_vocales = palabra_2_voc_ini = 0
# Banderas
cont_3_letras = tiene_si = tiene_no = tiene_de = tiene_u = tiene_lo_final = \
    tiene_ll = empieza_inicial = False
anterior = anterior_anterior = None


# funcion promedio

def promedio(a, b):
    if a != 0 and b != 0:
        promedio = a // b
    else:
        promedio = 0
    return promedio


# funcion porcentaje

def porcentaje(a, b):
    if b != 0:
        porcentaje = (a * 100) / b
    else:
        porcentaje = 0
    return porcentaje


# funcion es dijito

def es_digito(c):
    res = False
    digito = "0123456789"
    if c in digito:
        res = True
    return res


# funcion es vocal

def es_vocal(letra):
    vocal = 'aeiou' or 'AEIOU'
    if letra in vocal:
        return True
    else:
        return False


# funcion es terminal

def es_terminal(x):
    terminal = ' .'
    if x in terminal:
        return True
    else:
        return False


for carac in texto:
    if es_terminal(carac):
        palabra += 1
        # mayor en
        if palabra == 1:
            may = letra
            pos = palabra
        elif may < letra:
            pos = palabra
            may = letra

        # tiene lo en palabras al terminar
        letras_en_palabra = letra

        # tiene lo al final en palabra
        if anterior_anterior == 'l' and anterior == 'o':
            tiene_lo_final = True

        # tiene ll en la palabra y la cant de letras es par
        if tiene_ll and letra % 2 == 0:
            palabra_con_ll += 1
        # contador palabra con mas o 2 vocales y empieza con inicial
        if cont_vocales >= 2 and empieza_inicial:
            palabra_2_voc_ini += 1
        empieza_inicial = False
        cont_vocales = 0

        # palabras con mas de 3 letras
        if cont_3_letras:
            palabra_con_3_letras += 1
            # se resetea letra si hay que hacer alguna op que sea arriba
        letra = 0
        cont_3_letras = False

        # tiene si en palabra
        if tiene_si:
            palabras_con_si += 1
        tiene_si = False

        # tiene no en palabras
        if tiene_no:
            palabras_con_no += 1
        tiene_no = False

        # tiene de en palabras
        if tiene_de:
            palabra_con_de += 1
        tiene_de = False

        # tiene u y lo al final en palabra
        if tiene_u and tiene_lo_final:
            palabras_u_lo += 1

        # reseteo
        tiene_u = False
        tiene_lo_final = False
        if (anterior is not None) and carac == '.':
            break

    # LETRAS
    else:
        letra += 1
        if es_vocal(carac):
            cont_vocales += 1
        # tiene ll
        if anterior == 'l' and carac == 'l':
            tiene_ll = True
        # tiene mas de 3 letras
        if letra > 3:
            cont_3_letras = True
        # tiene si en letras
        if anterior == 's' and carac == 'i':
            tiene_si = True
        # tiene no en letras
        if anterior == 'n' and carac == 'o':
            tiene_no = True
        # tiene de en letras
        if anterior == 'd' and carac == 'e':
            tiene_de = True
        # tiene u en letras
        if carac == 'u':
            tiene_u = True

        # empieza con la primera palabra del texto
        if carac == texto[0] and (anterior is None or es_terminal(anterior)):
            empieza_inicial = True

    anterior_anterior = anterior
    anterior = carac

print('palabras con mas 3 letras: ', palabra_con_3_letras)
print('palabras con si: ', palabras_con_si, 'palabras con no: ',
      palabras_con_no)
print('cantidad de palabra con de: ', palabra_con_de)
print('Determinar cuantas palabras tuvieron u y terminaron en lo',
      palabras_u_lo)
print('la posicion de la palabra es: ', pos, 'y tiene letras: ', may)
print('Determinar la cantidad de palabras que incluyen ll y tienen cantidad '
      'de letras par: ', palabra_con_ll)
print('la cantidad de palabras que comienzan con la última letra de la'
      ' primera palabra del texto y tienen más de 2 vocales',
      palabra_2_voc_ini)
