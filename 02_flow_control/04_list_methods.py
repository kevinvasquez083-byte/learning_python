###
# 04 - Listas Método
# Los Métodos más importantes para trabajar con listas
###

import os
os.system("cls")

lista1 = ['a','b','b','c','d','f']

lista1.append('g') #añade al final de la lista
print(lista1)

lista1.insert(1,'z') # Inserta un elemento en la 
#posicion que le indiquemos como primer parametro
print(lista1) #Cada metodo permite permite la cantidad 
#parametros segun su funcion 

lista1.extend(['🚴','🏃🏾‍♀️']) # agrega elementos al finalde la lista

print(lista1)

#Eliminar elementos de la lista 

lista1.remove('z')
print(lista1)

ultimo = lista1.pop(-1) # Elimina el ultimo elementon de la lista 
# ademas lo devuelve

print(ultimo)
print(lista1)



ultimo1 = lista1.pop(-1) # Elimina el ultimo elementon de la lista 
# ademas lo devuelve

print(ultimo1)
print(lista1)

lista1.pop(1) # elimina el segundo elemento de la lista
print(lista1)

#eliminar 

del lista1[-1]
print(lista1)

lista1.clear() # Elimina todos los elemtnos
print(lista1)

# Eliminar un rango de elementos 

lista1 = ['🐰','🦝','🐽','🦧','🦥']
del lista1[1:3]
print(lista1)

# Metodos utiles

print ('Ordenar listas modificando la original')
numbers = [3,10,2,8,99,101]
numbers.sort()
print(numbers)

print ('Ordenar lista creando una nueva lista')

numbers = [3,10,2,8,99,101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


print("ordenar una lista de cadenas de texto en minuscula ")
frutas = ['manzana','pera','limón','manzana','pera','limon']
sorted_frutas = sorted(frutas)
print(sorted_frutas)


print("ordenar una lista de cadenas de texto en minuscula y mayuscula")
frutas = ['manzana','Pera','Limón','manzana','pera','limon']
frutas.sort(key = str.lower)
print(frutas)

#-------------

animals = ['🦄','🐎','🐿️','🐿️','🐼','🐨']
print(animals)
print(len(animals)) # Tamaño de la lista -> 6
print(animals.count('🦄')) # Cuantas veces aparece el unicornio

print ('🐿️' in animals) # Comprueba si hay un elemento en la lista
print ('🐽' in animals) # -> False 