import soporte
import os


def generar_vector():
    v = [] # vector de clientes
    if not os.path.exists("Enunciado.csv"):
        return None
    m = open("Enunciado.csv", "r")

    for linea in m:
        if linea[0] != '#':
            linea = linea[:-1]
            cadenas = linea.split(',')
            if cadenas[3] == '1':
                nombre = cadenas[0]
                apellido = cadenas[1]
                mail = cadenas[2]
                fecha = cadenas[4]
                importe = float(cadenas[6])
                cliente = soporte.Cliente(nombre, apellido, mail, fecha, importe)
                v.append(cliente)
    m.close()
    return v


def mostrar_vector(v):
    for i in range(len(v)):
        soporte.write(v[i])

def promedio(v):
    acu = 0
    n = len(v)
    for i in range(n):
        acu += v[i].importe
    return acu/n

def grabar_clientes(v, prom):
    m = open("clientes.csv", "wt")

    for i in range(len(v)):
        if v[i].importe > prom:
            cadena = v[i].nombre + "," + v[i].apellido + "," + v[i].mail + "," + v[i].fecha + "," + str(v[i].importe) + "\n"
            m.write(cadena)



def principal():
    v = generar_vector()
    if v == None:
        print("error")
    else:
        mostrar_vector(v)
    prom = promedio(v)
    grabar_clientes(v, prom)



if __name__ == "__main__":
    principal()



