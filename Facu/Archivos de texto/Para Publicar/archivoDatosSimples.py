__author__ = 'Cátedra de AED'

import pickle

def test():
    print('Procediendo a grabar números en el archivo')
    x, y = 2.345, 19
    # Carga de datos en el archivo
    m = open('prueba.num', 'wb')
    pickle.dump(x, m)
    pickle.dump(y, m)
    m.close()

    # Tamaño del archivo


    # Lectura de los datos que tiene el archivo
    m = open('prueba.num', 'rb')
    a = pickle.load(m)
    b = pickle.load(m)
    m.close()

    print('Datos recuperados desde el archivo:', a, ' - ', b)
    print('Hecho...')

if __name__ == '__main__':
    test()
