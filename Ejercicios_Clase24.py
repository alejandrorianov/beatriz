"Ejercicios del módulo random"

#Ejercicio 1
print('Ejercicio 1: función randint()')
import random
# ¿Quién comienza?
comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')
# Número aleatorio del parchís
numero = random.randint(1, 6)

#Ejercicio 2
print('Ejercicio 2: función randrange()')
import random
for i in range(10):
    print(random.randrange(5, 27, 4))

#Ejercicio 3
print('Ejercicio 3: función random()')
import random
for i in range(5):
    print(random.random())

#Ejercicio 4
print('Ejercicio 4: función uniform()')
import random
for i in range(5):
    print(random.uniform(100, 200))

#Ejercicio 5
print('Ejercicio 5: función choice()')
import random
frutas = ['peras', 'manzanas', 'plátanos', 'ciruelas']
for i in range(3):
    print(random.choice(frutas))

#Ejercicio 6
print('Ejercicio 6: función shuffle()')
import random
baraja = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
for i in range(3):
    random.shuffle(baraja)
    print(baraja)

#Ejercicio 7
print('Ejercicio 7: función sample()')
import random
baraja = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
print(random.sample(baraja, 5))

'''
Actividad para aplicación de conocimientos
Finalmente, después de haber tenido acceso a este contenido, realicemos una matriz que asigne de manera aleatoria a 5 estudiantes, los equipos de 5 aulas de clase, cada aula tiene 20 equipos (los cuales se asignan de manera aleatoria), al final yo podré consultar cual equipo le corresponde a un estudiante elegido (filas:  estudiantes, columnas: aulas de clase)

Dicho ejercicio se deberá subir al “TdeA virtual” en el espacio asignado para ello.
'''
import random

m = [[int() for i in range(6)] for i in range(6)]
for f in range(1,6):
	for c in range(1,6):
		m[f][c] = random.randint(1, 20)
print("  ____________________________  ")
for f in range(1,6):
	for c in range(1,6):
		print(" | ",m[f][c], end="")
	print(" | ")
	print("  ____________________________  ")

e = int(input("Numero de estudiante que buscas? desde 1 hasta 5"))
a = int(input("Numero de aula que buscas?  desde 1 hasta 5 "))
	
print("el estudiante ",e," tiene el equipo ",m[e][a]," en la aula ",a)