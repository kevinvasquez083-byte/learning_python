# Ejercicio 1: Determinar el mayor de dos numeros
# pedir al usuario introducir dos numeros y muestra un mensaje
# indicando cual es mayor o si son iguales

import os
os.system("cls")

print ("\n Ejercicio 1: Determinar el mayor de dos numeros")
num1 = int(input("Teclea el primer numero  : "))
num2 = int(input("Teclea el segundo numero : "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los numeros son iguales")

# # Ejericio 2: Calculadora simple
# # Solicita la usuario dos numeros y una operacion (+,*,-,/)
# # Realiza la operacion y muestra el resultado (manejando division por cero)

print ("\n Ejercicio 2: Calculadora simple")
num1 = float(input("Ingresa el primer numero:     "))
num2 = float(input("Ingresa el segundo numero:    "))
operacion = input("Ingresa la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        resultado = "Error: No se puede dividir por cero"   
    else:
        resultado = num1 / num2
else:
    print("Operacion no valida")
if 'resultado' in locals(): # Comprueba si la variable resultado existe.
    print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

# Ejericio 3 : Año bisiesto
# Solicita al usuario ingresar un año y determinar si es bisiesto.
# Un año es bisiesto si es divisible por 4, --
# excepto si es divisible por 100, a menos que sea divisible por 400.

print ("\n Ejercicio 3 : Año bisiesto  ")
año = int(input("Ingresa un año: "))

if(año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.") 


# Ejercicio 4: Categorizar edades 
# Pide al usuario que ingrese una edad y la clasifique en:
# -Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Anciano (65 años o más)

print ("\n Ejercicio 4: Categorizar edades  ")
edad = int(input("Ingresa una edad: "))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Anciano")    
else:
    print("Edad no valida")