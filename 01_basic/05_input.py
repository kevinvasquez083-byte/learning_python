

##
# 05 - Entrada de usuario (input()) - Version simplificada
# Lafuncion input() permite obtener datos del usuario a traves
# de la consola
##

nombre = input ("Hola, ¿Como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuantos años tienes?\n")

age = int(age)
print(f"Tienes {age} años")

print("Obtener multiples valores a la vez")
country, city = input ("¿En que pais y ciudad vives?\n").split()

print(f"Vives en {country},{city}")

