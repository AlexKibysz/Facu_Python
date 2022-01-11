_author_ = 'Alexander Kibysz 85698 1K2'
'''Desarrolle un programa completo en Python, sin usar las funciones 
predefinidas min() y max(), que permita cargar por teclado el ancho, 
el largo y profundidad de una pileta. Muestre la cantidad de metros 
cúbicos necesarios para llenarla (el producto entre las tres
 medidas cargadas)
 .Informe además si se trata de una pileta de superficie cuadrada
 o rectangular
. En caso que sea rectangular, informar si el lado más largo duplica, 
al menos, al lado mas corto.'''

ancho = float(input('Ingrese Ancho en metros: '))
largo = float(input('Ingrese largo en metros: '))
profundidad = float(input('ingrese profundidad en metros: '))
metros_cubicos = ancho * largo * profundidad
duplica = False
print('=' * 60)
print('los metros cubicos para llenar la pileta son: ', metros_cubicos,
      'metros cubicos!')
if ancho == largo:
    forma = 'Cuadrada'
if largo > ancho:
    forma = 'rectangulo'
    grande, corto = largo, ancho
    if grande >= 2 * corto:
        duplica = True
elif largo < ancho:
    forma = 'rectangulo'
    grande, corto = ancho, largo
    if grande >= 2 * corto:
        duplica = True

print('La forma de la pileta es: ', forma)
if duplica == True:
    print('El lado mas largo duplica al lado mas corto')
''''Desarrolle un programa completo en Python, sin usar las funciones
 predefinidas min() y max(), que permita cargar por teclado las cantidades
  de producción correspondientes a tres sucursales. Muestre la mayor de esas 
  cantidades. Informe si al menos alguna de estas cantidades fue mayor a 1000.
  '''



'''Desarrolle un programa completo en Python, sin usar las funciones 
predefinidas min() y max(), 
que permita cargar por teclado los valores de tres temperaturas. 
Muestre el valor de la temperatura menor 
y si esta es negativa muestre un mensaje que diga 
“Hay temperaturas bajo cero”, de lo contrario no 
muestre ningún mensaje.'''
