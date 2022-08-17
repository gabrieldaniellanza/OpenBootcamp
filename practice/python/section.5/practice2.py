import math

def EsPrimo(numero):
  for x in range(2, math.floor(math.sqrt(numero))):
    if (numero % x) == 0 :
      return False
  return True  

print("19 es primo: " + str(EsPrimo(19)))
print("18 es primo: " + str(EsPrimo(18)))
