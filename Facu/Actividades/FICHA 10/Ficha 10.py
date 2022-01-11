'''2. Sólo menores que 7.
Desarrollar un programa de Phyton que permita cargar por teclado un secuencia
de números, uno por uno.
 Siempre se supone que el usuario cargará un 0(cero) para indicar el final
 del proceso de carga.
 El cero no debe considerarse un dato a procesar. El programa debe:

a) Determinar el porcentaje que cantidad de números pares representa en la
cantidad total de números ingresados.

b) Determinar cuántos de los números ingresados tenían su último dígito
 igual a 4 o igual a 5.

c) Determinar el menor de los números ingresados que sean divisibles por 3.

d) Determinar si la secuencia estaba formada sólo por números menores o
iguales que 7.'''


def porcentaje(cant, cant_total):
    if cant_total != 0:
        calculo = round((cant * 100) / cant_total,2)
        return calculo
    else:
        return 0


def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False


def ult_4_5(x):
    if x%10==4 or x%10==5:
        return True

def es_multiplo(numero, divisor):
    resto= numero%divisor
    return resto==0



par = cuenta = cant_4_5 = 0
sec_igualmenor_7=True
menor=None
x = int(input('ingrese numero con cero cierra el programa: '))
while x != 0:
    if x>7:
        sec_igualmenor_7=False
    if ult_4_5(x):
        cant_4_5+=1
    # cuenta pares
    if es_par(x):
        par += 1
    if es_multiplo(x, 3):
        if menor==None or menor>x:
            menor=x
    # conteo de vueltas
    cuenta += 1
    # anterior
    anterior = x
    x = int(input('ingrese numero con cero cierra el programa'))
print('='*100)
#a
print('porcentaje de numeros pares: ', porcentaje(par, cuenta))
#b
print('los numeros que tenian 4 o 5 en sus ultimos digitos fueron: ',cant_4_5)

#c
print('el menor numero divisible por 3 es: ', menor)
#d
if sec_igualmenor_7:
    print('la secuencia esta formada por numeros menores o iguales a 7')
else:
    print('la secuencia no esta formada por numeros menores o iguales a 7')
