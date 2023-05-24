edades=[20, 41, 6, 18, 23]

#Recorriendo los elementos

for edad in edades:
    print(edad)

#Recorriendo los índices
for i in range(len(edades)):
    print(edades[i])

indice = 0
while indice < len(edades):
    print(edades[indice])
    indice +=1

numeros = []

numeros.append(10)
numeros.append(5)
numeros.append(3)

print(numeros)
#Mostrará [10, 5, 3]

#Unimos la lista anterior con una nueva
numeros = []
numeros = numeros + [10, 5, 3]
print(numeros)
#Mostrará [10, 5, 3]

palabras = ['hola', 'hello', 'ola']
palabras.pop(1)
print(palabras)

palabras = ['hola', 'hello', 'hello', 'ola']
palabras.remove('hello')
print(palabras)
#Mostrará ['hola', 'hello', 'ola']


#Ejemplo 1
arreglo = [float() for i in range(10)]
for i in range(10):
	arreglo[i] = i
	print(arreglo[i])

#Ejemplo 2
arreglo = [float() for i in range(10)]
suma = int()
suma = 0
for i in range(10):
	arreglo[i] = i
	suma = suma+arreglo[i]
	print(arreglo[i])
print("La suma es ",suma)

#Ejemplo 3
arreglo = [float() for i in range(10)]
suma = int()
media = float()
suma = 0
media = 0
for i in range(10):
	arreglo[i] = i
	suma = suma+arreglo[i]
	print(arreglo[i])
print("La suma es ",suma)
media = suma/10
print("El promedio de la suma de los numeros es:  ",media)

#Ejemplo 4
a1 = [int() for i in range(6)]
a2 = [int() for i in range(6)]
a3 = [int() for i in range(6)]
for i in range(6):
	print("Introduce el valor del arreglo a1 en la posición ",i+1)
	a1[i] = int(input())
	print("Introduce el valor del arreglo a2 en la posición ",i+1)
	a2[i] = int(input())
	a3[i] = int(a1[i]+a2[i])
for i in range(6):
	print(a1[i]," + ",a2[i]," = ",a3[i])

#Ejemplo 5
a1 = [float() for i in range(5)]
a1[0] = 2
a1[1] = 5
a1[2] = 4
a1[3] = 3
a1[4] = 2
print("inserta elemento a buscar: ")
numerobuscado = float(input())
encontrado = False
for i in range(5):
	if numerobuscado==a1[i]:
		print("Se ha encontrado el número: ",numerobuscado," en la posición: ",i)
		encontrado = True
if encontrado == False:
	print(" No se ha encontrado ningún elemento ")