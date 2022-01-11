import random

# random.random()

# tal cual genera numeros del 0 al 0.9999999 [0, 1) en float
print('-' * 100)
print('random.random')
x = random.random()
print(x)



# random.randrange

# número aleatorio entero y tal que 2 <= y < 10 (2, 10) nunca va a ser 10
print()
print('-' * 100)
print('random.randrange')
y = random.randrange(2, 10)
print(y)

# random.radint

# número aleatorio entero y tal que 2 <= y <= 10

print('-' * 100)
print('random.randint')
y = random.randint(2, 10)
print(y)
print()
print('-' * 100)
#random.choice(sec): acepta secuencias, letras, numeros etc

sec1 = 2, 10, 7, 9, 3, 4
r1 = random.choice(sec1)
print(r1)
sec2 = 'ABCDEFGHIJKLMNOPQRS'
r2 = random.choice(sec2)
print(r2)


