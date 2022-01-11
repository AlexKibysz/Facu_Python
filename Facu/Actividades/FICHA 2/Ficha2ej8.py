'''8. Rinde de un Campo Agricola
Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela.
Se pide ingresar el largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2
se obtienen 2 quintales.'''
largo = float(input('ingrese metros de largo'))
ancho = float(input('ingrese metros de ancho'))
metros = largo * ancho
quintales = (metros / 5)
print('vas a tener : ', quintales, 'quintales')
