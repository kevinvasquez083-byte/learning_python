# 02 - Booleanos
# Valores logicos: true (verdadero) y False (falso).
# Fundamentales para el control de flujo y la logica en programacion

# Los booles se representan en valores de verdad: True or False.
###



import os
os.system("cls")


print("\n Valores booleanos basicos:")
print(True)
print(False)

# Operadores de comparacion devuelven un valor booleano
print("\n Operadores de comparacion:")
print("5<3:", 5<3) #False
print("5>3}:", 5>3)  #True
print("5==5:", 5==5) #Igualdad
print("5!=3:", 5!=3) #Desigualdad
print("5>=3:", 5>=3) #Mayor o igual
print("5<=3:", 5<=3) #Menor o igual

# Comparacion de cadenas de texto
print("manzan < pera : ", "manzana" < "pera") #True, orden alfabetico
print("'Hola' == 'hola':", "Hola" == "hola") #False, mayusculas y minusculas son diferentes


# Operadores logicos : and, or, not
print("\n Operadores logicos:")
print("True and True:", True and True) #True
print("True and False:", True and False) #False
print("True or False:", True or False) #True
print("False or False:", False or False) #False
print("not True:", not True) #False
print("not False:", not False) #True

# Tablas de verdad
print("and:")
print("A     B   A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("or:")
print("A     B   A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("not:")
print("A     not A")
print("True  ", not True)
print("False ", not False)


