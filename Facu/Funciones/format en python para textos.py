''''Nombre = input(str("Ingresa tu nombre \n")) #Solicitamos datos de entrada
print ("Tu nombre es {0}".format(Nombre)) #Formateamos la salida

Nombre = input(str("Ingresa tu nombre \n"))
Edad = int(input("Bien, ahora ingresa tu edad \n"))
NombreMascota = input(str("Ingresa el nombre de tu mascota \n"))
print ("Tu nombre es {0} y tienes {1} años. Tu mascota se llama {2}".format(Nombre, Edad, NombreMascota))'''
a = 'abra'
b = 'cad'
print('{0}{1}{0}'.format(a, b))

a = 'abra'
b = 'cad'
print('{0:<2}{1:^5}{0:>5}'.format(a, b))

Tabla = """\
+---------------------------------------------------------------------+
| Nombre    Apellido        Primero Segundo Tercero     Promedio anual|
|---------------------------------------------------------------------|
{}
+---------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>23} |".format(*fila)
 for fila in ListasAlumnos)))
print (Tabla)
