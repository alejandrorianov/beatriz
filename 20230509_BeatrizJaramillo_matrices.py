"""
Programa elaborado por Beatriz E. Jaramillo Moncada
Nombre del programa: Ejercicio de Matrices.
Fecha: 09-Mayo-2023
"""

import random # Se importa esta librería para poder usar la función de randint

matriz=[[int() for filas in range(6)] for colunnas in range(6)] # Se inicializa la matriz con 5 filas y 5 columnas 

# Ciclos anidados de asignación de valor a cada posición de la matriz
for filas in range(1,6): # Se usa este ciclo for para recorrer las filas
    for columnas in range(1,6): # Se usa este ciclo for para recorrer las columnas
        matriz[filas][columnas] = random.randint(1,20) # Se usa esta asignación para llenar con un valor aleatorio entero de 1 a 20 cada posición de la matriz

print("¡¡¡¡Bienvenidos al examen final!!!!\n________________________")

# Ciclos anidados para la impresión del valor de cada posición de la matriz
for filas in range(1,6):# Se usa este ciclo for para recorrer las filas
    for columnas in range(1,6):# Se usa este ciclo for para recorrer las columnas
        print("|",matriz[filas][columnas], end = " ")# Se usa esta asignación para imprimir el valor de cada posición de la matriz
    print("|") # Se usa este caracter para finalizar cada fila
    print("________________________") # Se usa esta cadena de caracteres para separar cada fila

# En esta sección se evalúa el dato del estudiante y su aula vs la matriz
estudiante=int(input("Por favor ingrese su identificación de 1 a 5\n"))
aula=int(input("Por favor indique el aula donde realizará su examen de 1 a 5\n"))
print(f"El usuario {estudiante} le corresponde el salón {matriz[estudiante][aula]} en el salón {aula}") 