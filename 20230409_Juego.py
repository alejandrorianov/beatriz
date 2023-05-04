"""
Programa elaborado por Beatriz E. Jaramillo Moncada - JUEGO DE LOTERÍA.
"""
"""
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
"""
#INICIO DEL PROGRAMA

print("*** INICIO DEL PROGRAMA ***")
mensaje01 = " BIENVENIDO AL JUEGO DE LOTERÍA "
print ("\n",mensaje01.center(50,"="))

import random # Se importa la librería de random de Python para poder usar la función de randit()'

juegos = [1, 2, 3]

for juego in juegos:
  numeroLoteria = random.randint(1, 10) # Se usa la función randit para que asigne un valor aleatorio de 1 a 10
  intentos = 0 # Inicializamos los intentos en cero
  
  while True: # Se coloca el valor en Verdadero para que el ciclo While se ejecute de manera indefinida
    bandera = False # Se inicializa en falso para poder entrar en el ciclo While
    while bandera == False:
      numeroUsuario = input("\nAdivina el número secreto del 1 al 10: ")
      bandera = numeroUsuario.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
      if bandera == False:
        print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, del 1 al 10")
      elif int(numeroUsuario) >= 1 and int(numeroUsuario) <= 10: # Se evalúa si el valor ingresado sea de 1 a 10
        bandera = True
        numeroUsuario = int(numeroUsuario) # Convierte el valor texto en entero para poder hacer operaciones matemáticas con él
      else:
        bandera = False
        print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, del 1 al 10")
    intentos += 1
    if numeroUsuario == numeroLoteria: # Evalúa el valor ingresado por el usuario vs el que se tiene de Lotería
      print("\n¡Felicidades! Adivinaste la LOTERÍA en", intentos, "intentos.")
      break # Esta sentencia rompe el ciclo ya que el número ya fue adivinado
    elif numeroUsuario > numeroLoteria: # Evalúa si el valor ingresado por el usuario es menor al que se tiene de Lotería
      print("\nEl número secreto es menor que", numeroUsuario)
    else: # Evalúa si el valor ingresado por el usuario es mayor al que se tiene de Lotería
      print("\nEl número secreto es mayor que", numeroUsuario)
  
  print("\nFin del juego.")
  print("\nTe quedan ", 3-juego, " juegos.") # Hace el conteo de los juegos restantes
print("\nMuchas gracias, vuelve pronto.")