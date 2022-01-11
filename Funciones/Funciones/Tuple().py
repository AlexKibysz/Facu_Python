#tuple
print('tuple separa por caracteres el objeto o numeros que se le asignen incluyendo los espacios vacios')
print()
t = tuple('Alexander Kibysz')
print(t)
print('-'*100)
t = tuple('123456')
print(t)
print('-'*100)

#una tupla puede tener elementos de diferentes tipos

print('en este caso caracteres, enteros y floats')
t2 = 'Juan', 24, 3400.57, 'Córdoba'

print(t2)
nombre = t2[0]
edad = t2[1]

# acordarse que va desde [0 a 3]

print('Nombre:', nombre, '- Edad:', edad, '- Sueldo:', t2[2], '- Ciudad:', t2[3])
print('-'*100)
#tambien se puede hacer duplas para variables como en el ejemplo de abajo
print('las duplas pueden aplicarse a variables tambien')
a = 5
x, y = 2*a, 4*a
print(x)
print(y)
print(x, y)
print('-'*100)
print('va a mostrar los numeros en tal variable como una dupla')
sec = 5, 8
print('Secuencia: ', sec)

# muestra: Secuencia: (5, 8), y asigna a, b a la var sec que vale la dupla 5 y 8

a, b = sec
print('a: ', a)
print('b: ', b)
print('-'*100)


