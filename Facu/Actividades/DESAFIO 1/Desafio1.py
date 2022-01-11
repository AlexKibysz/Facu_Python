tiempototal1 = int(input('ingrese primera ejecucions'))
tiempohoras = (tiempototal1) // 3600
tiemposobrantehoras=tiempototal1%3600
tiempominutos=tiemposobrantehoras//60
tiemposobranteminuto=tiemposobrantehoras%60
tiemposegundo=tiemposobranteminuto
tiempofinal= (tiempohoras,'horas',tiempominutos,'minutos',tiemposegundo,'segundos')
print(tiempofinal)
th=int(input('ingrese hs: '))
tm=int(input('ingrese min: '))
ts=int(input('ingrese seg: '))
ths=th*3600
tms=tm*60
tt=('tu tiempo en segundos es de: ', ths+tms+ts)
print(tt)


