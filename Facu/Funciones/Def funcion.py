def principal():
    print('portal de empleos')
    # datos
    cuit = input('ingrese cuit')
    descripcion = input('ingrese descripcion de la busqueda')
    salario = int(input('Ingrese salario ofrecido'))
    # procesos
    def validar_cuit(cuit):
        validar_cuit=False
        if len(cuit)==13:
           validar_cuit=True
    def validar_descripcion():
        print('='*50)
        print('AVISO')
        print('El empleador', cuit, 'te esta buscando')
        print('el salario ofrecido $', salario)


principal()
