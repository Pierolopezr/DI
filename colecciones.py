"""Colecciones:

Listas
Tuples
Diccionarios


"""

#Listas

l = [23,25.5,3+4j,-15,"pepe",[23,25,51],12+45] # la lista puede contener de distintos tipos en la misma lista
print(l[-1])
print(l)
l[-2] = "Personaje npc" #se puede modificar una lista


print(l)
print(type(l))

#lista dentro de lista
print(l[5][2:6])

#Slicing puedes pillar un rango con : estnado el primer numero incluido y el segundo excluido
print(l[2:5])
print(l[:5])
print(l[2:])
print(l[1:6:3]) # el ultimo numero es cada cuantos saltos pilla en este caso pilla un valor cada 3
print(l[::-1]) # puedes hacer que la direccion del salto sea al reves

#Tuplas son listas pero no se pueden modificar

l = (2,5,2+4j,"un texto",[22,3,5,6],3,9) # el parentesis es solo visual la tupla existe con las comas directamente los parentesis pueden no aparecer
t = 2,5,2+4j,"un texto",[22,3,5,6],3,9  #Ejemplo de tupla sin parentesis
t2 = 2,5,2+4j,"un texto",(22,3,5,6),3,9 #Ejemplo de necesidad de parentesis en dupla
t3 = 5, # ejemplo de tupla de un solo valor
t4 =None,54 # ejemplo de añadir un elemento vacio, no sirve para casi nada porque lo que este vacio casi siempre se puede omitir
print(t4)
print(t3)
print(t)
print(l)
print(l[2])
l[-3][2] = 4 # se puede modificar una lista si esta en una tupla siempre que solo se modifique la lista y no la tupla
print(l)

# Diccionarios

d= { 1: "Un",
     2: "Dous",
     3: "Tres",
     4: "catro",
     }
# d[3] = "Three" -> se puede reescribir
print (d[3])
print(d)

#Sentencias condicionales
n1 = 3
if n1 > 5 :  #Se puede poner parentesis pero para más de un caso en la condición
     print("Pois resulta")
     print("que ni é ")
     print("maior que 5")
else:
     if n1 == 0:
          print("n1 é ")
          print("igual a 0")
     else:
          print("Pois resulta")
          print("Que ni é ")
          print("menor que 5")