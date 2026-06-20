import os
os.system("cls")

##
# #  01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
##



print ("\n Sentencia simple condicional")

edad = 18 

if edad >= 18:
    print("Eres mayor de edad")

print("\n Sentencia concdicional con else")
edad = 15

tiene_carnet = True

if edad >=18:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 7 
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("No estas calificado")


# Javascript
# && = and
# || = or
# 🇻🇪 un pueblo de Valencia 
if edad >= 18 and tiene_carnet:
    print ("Puedes conducir 🚗 ")
else:
    print("POLICIA!!!!👮")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 and tiene_carnet:
    print ("Puedes conducir en la Isla Margari 🚗 ")
else: 
    print("Paga al policia y te deja conducir!!👮")


es_fin_de_semana = False

if not es_fin_de_semana:
    print("Llorelo, hay que chambear 😨")

print ("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad>= 18:
    if tiene_dinero:
        print("Puedes ir a la disco🕺")
    else:
        print("Quedate en la casa, no tienes dinero 😢")
else:
     print("No puedes entrar a la disco, no eres mayor de edad 😢")
    
# Simplificado
# if edad < 18:
#     print("No puede entrar a la disco")
# elif tiene_dinero:
#     print("Puedes ir a la disco🕺")
#  else:
#     print("Quedate en casa")



numero = 5 
if numero: # False
    print("El numero no es cero")

numero = 0 
if numero: # False
    print("Aquí no entrará neverland")

nombre = ""
if nombre:
    print("El nombre no esta vacio")

numero = 5
if numero == 2:
    print("El numero es 2") 


numero = 3 # asignacion
es_tres= numero == 3 # comparacion

if es_tres:
    print("El numero es 3")


# print ("\n Condicion ternaria:  ")
# Es una forma concisa de un if-else en una linea de codigo
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

edad = 24
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
