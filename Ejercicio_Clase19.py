def tabla(n1):
    for i in range(11):
        print(n1," X ",i," = ",n1*i)

def longitudtexto(t1):
    l = len(t1)
    print("La longitud de caracteres del texto ",t1," es: ",l)

def triplesuma(n1, n2):
    s = n1+n2
    t = s*3
    print("El triple de la suma de dos números es: ",t)

def producto(n1, n2):
    p = n1*n2
    print("El producto de dos números es: ",p)

def suma(n1, n2):
    s = n1+n2
    print("La suma de dos números es: ",s)

def menu():
    print("Seleccione una opción")
    print(" ")
    print(" ")
    print("1-Suma de dos números")
    print("2-Producto de dos números")
    print("3-Triple de la suma de dos números")
    print("4-Longitud de un texto")
    print("5-Tabla de multiplicar")
    print("6-Para Salir")
    print(" ")
    print(" ")
menu()
while True:
    print("Ingrese la opción deseada")
    a = float(input())
    if a==1:
        print("Ingrese un número")
        n1 = int(input())
        print("Ingrese otro número")
        n2 = int(input())
        suma(n1,n2)
        print("Elija otra opción del menú o 6 para salir!!")
    elif a==2:
        print("Ingrese un número")
        n1 = int(input())
        print("Ingrese otro número")
        n2 = int(input())
        producto(n1,n2)
        print("Elija otra opción del menú o 6 para salir!!")
    elif a==3:
        print("Ingrese un número")
        n1 = int(input())
        print("Ingrese otro número")
        n2 = int(input())
        triplesuma(n1,n2)
        print("Elija otra opción del menú o 6 para salir!!")
    elif a==4:
        print("Ingrese un texto")
        t1 = input()
        longitudtexto(t1)
        print("Elija otra opción del menú o 6 para salir!!")
    elif a==5:
        print("Ingrese un número")
        n1 = int(input())
        tabla(n1)
        print("Elija otra opción del menú o 6 para salir!!")
    elif a==6: 
        print("Gracias por participar")
        break
    else:
        print("Opción incorrecta inténtelo nuevamente")
    if a>0 and a<6: True