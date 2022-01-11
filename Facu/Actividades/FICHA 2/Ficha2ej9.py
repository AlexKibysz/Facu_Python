'''9. Datos de un rectángulo
Hacer un programa que tome como entrada el ancho y el alto de un rectángulo
y determine el perímetro y la superficie del mismo.
'''
ancho = float(input('ingrese ancho'))
alto = float(input('ingrese alto'))
perimetro = alto + ancho
superficie = alto * ancho
print('tu perimetro es de:', perimetro)
print('tu superficie es de: ', superficie)
