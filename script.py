
#numeros

#enteiros
numEnteiro = 5
print(type(numEnteiro))

#Coma flotante

numDecimal = 5.6
numDecimal2 = 0.1e-5
print(type(numDecimal))
print (10/3)
print(10.2/3)
#Booleano

booleano = True
print(type(booleano))

#Complejos

complexo = 2.3 + 9.3j
print(type (complexo))
print(complexo)

#Cadeas
"""Este é o comentario multiliña"""
'''Estos se pueden marcar con comillas simples'''
cadea = "Esto é unha cadea marcada con comillas 'dobres'"
cadea2= 'Esto é unha cadea marcada con comillas "simples"'
print(cadea, "\n", cadea2)
print(cadea2)

#Operadores aritmeticos

# + -> más
# - -> menos o valor negaitvo
# * -> multiplicar
# / -> dividir
# ** -> exponente
# // -> division que se queda en el entero (10/3 = 3.333 pero 10//3 = 3)
# % -> devuleve el resto de la division (10%3 = 1)

#Operadores a nivel de bit
# & -> and  se hace un y logico bit a bit (2&3 = 2)
# | -> or se hace un o logico bit a bit (2|3 = 3)
# ^ -> xor se hace un xor logico bit a bit (2^3 = 1)
# ~ -> not. se hace un not logico bit a bit (~2 = -3 -> porque la nomenclatura binaria hace que el primer digito sea el signo y luego funciona raro)
# >> -> dividir por potencoias de 2 (Realmente muevo los bits a la derecha la cantidad de huecos indicada)
# << -> multiplicar potencias de 2 (Realmente muevo los bits a la izquierda la cantidad de huecos indicada)

#Operadores de cadea + *
#+ concadena
#* replica una cadena el numero de veces indicada
cad = "un"
cad2 = "Dous"
print(cad+cad2)
print(cad * 1000)

# Java   $$   ||   |
#Python  and  or  not
#Comunes ==  !=  <  >  <=  >=

print(1 or 0)
