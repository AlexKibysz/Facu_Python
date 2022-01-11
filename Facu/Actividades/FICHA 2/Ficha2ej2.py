# 2. Descuento en medicinas
# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
# (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
# tienen un descuento del 35%. Mostrar el precio actual,
# el monto del descuento y el monto final a pagar.
precio = float(input('precio del medicamento'))
descuento = (precio * 35) / 100
descuentoprecio = precio - descuento
preciofinal = descuento
print('Precio de medicamento: ', precio)
print('Precio con descuento: ', descuentoprecio)
print('descuento de: ', preciofinal)


