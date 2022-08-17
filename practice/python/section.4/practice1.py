#Escribe un programa que pregunte al usuario su edad 
edad = int(input('¿Cuál es su edad?: '))

esMayor = ''
if edad < 18 :
  esMayor = 'no '

#muestre por pantalla si es mayor de edad o no.
print('Usted ' + esMayor + 'es mayor de edad')
