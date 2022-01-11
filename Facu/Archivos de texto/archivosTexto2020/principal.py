import random

def grabar():
    m = open("archivo.txt", "wt")
    n = 20
    for i in range(n):
        num = random.randint(0, 1000)
        m.write(str(num) + "\n")
    m.close()

def leer():
    m = open("archivo.txt", "rt")
    v = []
    #print("\nContenido del archivo:\n", m.read(),"\n")
    for linea in m:
        if linea[-1] == "\n":
            linea = linea[:-1]
        print(linea)
        v.append((int(linea)))

    m.close()
    print(v)



def principal():
    op = 1
    while op != 3:
        print("Menú")
        print("1-Grabar")
        print("2-Leer")
        print("3-Salir")

        op = int(input("Ingrese su opción: "))

        if op == 1:
            grabar()
        elif op == 2:
            leer()
        elif op == 3:
            print("Bye!")
        else:
            print("Opción incorrecta!")

if __name__ == "__main__":
    principal()




