import math

#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def EsBisiesto(anio):
  if (anio % 4) == 0:
    if (anio % 100 == 0):
      return(anio % 400 == 0)
    else:
      return True

print("10 es bisiesto: " + str(EsBisiesto(10)))
print("12 es bisiesto: " + str(EsBisiesto(12)))
print("1800 es bisiesto: " + str(EsBisiesto(1800)))
print("2000 es bisiesto: " + str(EsBisiesto(2000)))
