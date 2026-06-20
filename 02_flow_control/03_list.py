# 03 - Listas 
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos


import os
os.system("cls")

# Creacion de listas
print("\n Crear listas")

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #lista de enteros
lista2 = ["manzana", "banana", "cereza","peras","platanos"] #lista de cadenas
lista3 = [1, "hola",3.14,True] # Lista de tipos mixtos

lista_vacia =[]
lista_de_lista = [1,2], ['yo',4], [5,6]
matrix = [[1,2],[3,4],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_lista)
print(matrix)


# Acceso a elementos por indice
print("\n Acceso a elementos por indice")
print(lista2[0]) #manzana
print(lista2[1]) #banana
print(lista2[-1]) #platanos, indice negativo accede desde el final
print(lista2[-5])


print(lista_de_lista[1][0]) 

# Slicing de listas
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1[1:5]) # [2,3,4,5] , desde el indice 1 hasta el 5 (el 6 no se incluye)
print(lista1[5:]) # [6,7,8,9,10] , desde el indice 5 hasta el final
#------------------#
print(lista1[::-2]) # [1,3,5,7,9] , desde el inicio hasta el final con paso de 2 // paso negativo reverse

# Modificar una lista

lista1[0] = 1000
print(lista1) # [1000,2,3,4,5,6,7,8,9,10]

# Añadir elementos a una lista
# (large way)
lista1 = lista1 + [11,12] # Concatenacion de listas
print(lista1) # [1000,2,3,4,5,6,7,8,9,10,11,12]

# (short way)
lista1 += [13,14] # Operador de asignacion con suma
print(lista1) # [1000,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Recuperar wlongitud de lista

print("longitud de lista", len(lista1)) 