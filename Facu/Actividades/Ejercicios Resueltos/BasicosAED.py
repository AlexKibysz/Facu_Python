
def esVocal(car):
    vocales = 'aeiouAEIOU'
    return car in vocales

def esDigito(car):
    digitos = '0123456789'
    return car in digitos

def esConsonante(car):
    car = car.lower()
    consonantes = 'bcdfghjklmnñpqrstvwxyz'
    return car in consonantes

def promedio(num,den):
    if den !=0:
        prom = num/den
    else:
        prom = 0
    return prom

def porcentaje(total,x):
    if total != 0:
        porc = x * 100 / total
    else:
        porc = None
    return porc

def esPar(num):
    if num%2 == 0:
        return True
    return False

def test():
    car = 'P'
    if esConsonante(car):
        print('Es consonante')
    else:
        print('No es consonante')

if __name__ == '__main__':
    test()


