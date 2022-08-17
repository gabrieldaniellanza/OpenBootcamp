
#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
desde = int(input('Ingrese el numero desde: '))
hasta = int(input('Ingrese el numero desde: '))

for x in range(desde, (hasta +1)):
   if(x % 2 == 1):
      print(str(x))
