# Ejercicio 1 El mensaje secreto
# Dada la siguiente lista :
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# utilizando slicing y concatenacion, crear una nueva lista que contenga solo el mensaje "secreto".

import os
os.system("cls")


print("\n Ejercicio 1: ")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print (secreto)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista :
# numero = [10,20,30,40,50]
# intercambia la primera y la ultima posicion utilizando asignacion por indices

print("\n Ejercicio 2: ")
numeros = [10,20,30,40,50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)


# Ejercicio 3 : El sandwich de listas
# Dada las siguientes listas :
# pan = ["pan arriba"]
# ingredientes = ["jamon", "queso", "lechuga"]
# pan_abajo = ["pan abajo"]
# Crear una lista llamada sandwich que tenga el pan de arriba, los ingredientes y el pan de abajo
# en ese orden, utilizando concatenacion de listas.

print("\n Ejercicio 3: ")
pan = ["pan arriba"]
ingredientes = ["jamon", "queso", "lechuga","sal"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)


# Ejercicio 4 : Duplicando la lista
# dada una lista :
# lista = [1,2,3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados
# Ejemplo : [1,2,3] -> [1,2,3,1,2,3]

print("\n Ejercicio 4 :")
lista = [1,2,3,4,5,6]
lista1 = [6,5,4,3,2,1]
lista_duplicada = lista + lista1
print(lista_duplicada)

#--------------------------------
lista = [1,2,3,4,5,6]
lista_duplicada1 = lista + lista
print(lista_duplicada1)

#-------------------------------

lista += [1,2,3,4,5,6]
print(lista)

#--------------------------------------------------
#con paso

lista2 = [1,2,3,4,5,6,7,8,9,0]
lista_doble = lista2 + lista2[::-1]
print(lista_doble)

# # Ejercicio 5 : Extraer el centro 
# # Dada una lista con un numero impar de elementos, extrae el elemento
# # que se encuentra en el centro de la lista utilizando slicing
# Ejemplo : lista = [10,20,30] el centro es 20

print("\n Ejercicio 5 :")
lista = [0,10,20,30,40,50,60,70,80,90,100,110]
centro = len(lista) //2
print(lista[centro])



#_-------------------------------


# Ejercicio 6 : Reversa parcial
# dada una lista, invierte solo la primera mitad de la lista 
# utilizando slicing y concatenacion.
# ejemplo : lista = [1,2,3,4,5] -> Resultado : [3,2,1,4,5]

print("\n Ejercicio 6 :")
lista = [1,2,3,4,5,6,7,8,9,0]
mitad = len(lista) // 2
lista_inversa = lista[:mitad][::-1] + lista[mitad:]
print(lista_inversa)

print(lista_inversa + lista_inversa[::-1])

#-------------------------------------------------------------------------------------------------------------
