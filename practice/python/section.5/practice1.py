import math

# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros 
def CalularAreaTriangulo(altura, base):
  area = base * altura / 2
  return area

# y otra función que calcule el área de un círculo recibiendo el radio del mismo.
def CalularAreaCirculo(radio):
  area = 2 * math.pi * radio
  return area
   
print("Area Triangulo: " + str(CalularAreaTriangulo(2,3)))

print("Area Circulo: " + str(CalularAreaCirculo(5)))
