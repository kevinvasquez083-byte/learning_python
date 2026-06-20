# ##
# # 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinamico y de tipado fuerte
# ##

# Asignar una variable
# solo hace falta poner esto

my_name = "kevvvin"
print(my_name)
age = 24
print (age)
##
# tipado dinamico: el tipo de dato se determina
# en tiempo de ejecucion y no se tiene que declarar declarar
# de manera explicita
##
age = 25

print (age)

# Tipado fuerte: Python no realizar conversiones de tipo automatico

print(f"Hola {my_name}, tengo {age-1} años")

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

Minombrdevariable = "ko" #PascalCase
minombredevariable = "ko" #todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 #UPPER_CASE constantes

# nombre no validos de variables
# 123123_variable = "KO"
# mi-variable = "ko"
# mi variable = "ko"

##PALABRAS RESERVADAS 

# if, else, elif, for, while, break, continue, pass, match, case,
# def, return, class, yield,and, or, not, is, in
# try, except, finally, raise, assert,None, True, False
# import, from, as, global, nonlocal, del, with, async, await, lambda

##

is_user_logged_in : bool = True
print(is_user_logged_in)

is_user_logged_in = 33
print(is_user_logged_in)