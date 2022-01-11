''' 6. Precio de venta
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento)
Precio de venta con tarjeta (5% de recargo)'''

articuloprecio = float(input('pon el precio del articulo'))
print('en contado tenes un 10% de descuento\n en tarjeta tenes un 5% de recargo')
preciocont = (articuloprecio * 10) / 100
recargo = (articuloprecio * 5) / 100
print('precio de contado con 10% de descuento')
print(articuloprecio - preciocont)
print('precio total tarjeta')
print(recargo + articuloprecio)
