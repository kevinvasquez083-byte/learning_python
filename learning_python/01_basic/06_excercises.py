# ##
# Soluciones a ejercicios basicos de python
# ##

import os
os.system("cls")

print("\nEjercicio 1 : Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas")

# Solucion : 
nombre = "Estiwar"
ciudad = "Medellin"

print(nombre)
print(ciudad)

#-------------------------------------------------------------

print("\nEjercicio 2 : Muestra los tipos de datos de las siguientes variables :")
print(" Usa el comando 'type()' para determinar el tipo de datos de cada variable")

# Variables

a = 24
b = 2.718
c = "Hola jefe"
d = True
e = None
f = "0"
g = 0
h = False

# ====

print("Tipo de a :", type(a))
print("Tipo de b :", type(b))
print("Tipo de c :", type(c))
print("Tipo de d :", type(d))
print("Tipo de e :", type(e))
print("Tipo de f :", type(f))
print("Tipo de g :", type(g))
print("Tipo de h :", type(h))

#-------------------------------------------

print("\n Ejercicio 3 : Casting de tipos")
print("Convierte la cadena 654321 a un entero y luego a un float")
print("Convierte el float 3.99 a un entero. ¿Que ocurre?")

# =====
cadena = "654321"
numero_entero = int(cadena) #Covierte cadena a entero
numero_float = float(numero_entero) #Convierte entero a float

print("Numero entero :", numero_entero)
print("Numero a float :", numero_float)

#---

float_num = 9.99
entero_convertido = int(float_num) #Se trunca el decimal

print("Float original :", float_num)
print("Float convertido a entero (se trunca su parte decimal) :", entero_convertido)

#-----------------------------

print("\nEjercicio 4 : Variables")
print("Crea variables para tu nombre, edad y altura")
print("Usa f-string para imprimir una presentacion")

# ===

nombre = "Estiwar"
edad = 24
altura = 1.80

#using f-string
print(f"Hola! mi nombre es {nombre} , mi edad es {edad} y mi estatura es de {altura} metros")

#---------

print("\n Ejercicio 5 : Números")
print("1. Crea una variable con el numero PI (sin asignar una variable)")
print("2. Redondea el numero con round()")
print("3. Haz la division entera entre el numero que te salió y el numero 2")
print("4. El resultado debería ser 1")

# #=====
# Redondeamos directamente el valor de pi soin almacenarlo en una variable

resultado = int(round(3.1416) / 2)
print("El valor de PI (aproximado) : ", 3.1416)
print("PI redondeado :", round(3.1416))
print("Division entera de PI redondeado entre 2 : ", resultado)