'''

A partir de un angulo expresado
en sexagesimal convertir al mismo
en solo grados solo minutos y solo segundos
'''
angulo = float(input('ingrese angulo'))
angamin=angulo//60
minsobra=angamin%angulo

print(angamin)
angaseg=angaminsobra/60
print(angaseg)
print(angulo,'angulo',angaminsobra,'minuto',angaseg )
