#Ejemplo 1: para imprimir la matriz 
print('Ejemplo 1: para imprimir la matriz')
M1 = [[8, 14, -6], 
           [12,7,4], 
           [-11,3,21]]

#To print the matrix
print(M1)

#Ejemplo 2: Leer el último elemento de cada fila
print('Ejemplo 2: Leer el último elemento de cada fila')
M1 = [[8, 14, -6],
           [12,7,4], 
           [-11,3,21]]

matrix_length = len(M1)
#print (matrix_length)
#To read the last element from each row.
for i in range(matrix_length):
    print(M1[i][-1])

#Ejemplo 3: para imprimir las filas en la matriz
print('Ejemplo 3: para imprimir las filas en la matriz')
M1 = [[8, 14, -6],
           [12,7,4], 
           [-11,3,21]]

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i]) 