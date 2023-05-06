"""
Programa elaborado por Beatriz E. Jaramillo Moncada - TEOREMA DE PITÁGORAS.
"""
#INICIO DEL PROGRAMA

import math # Se importa la librería de matemáticas de Pÿthon para poder usar la función de Raíz Cuadrada 'sqrt()'

print("*** INICIO DEL PROGRAMA ***")
mensaje01 = " BIENVENIDO AL TEOREMA DE PITÁGORAS "
print ("\n",mensaje01.center(50,"="))

mensaje02 = "\nMuchas gracias, lo esperamos en una nueva oportunidad.\n\n*** FIN DEL PROGRAMA ***" # Se establece este mensaje preconfigurado de despedida para ser reusado cuando se necesite

# Evaluación si las medidas que se van a ingresar son un triángulo rectángulo.
print ("\nPara continuar con la ejecución de este programa debes confirmar si las medidas que se van a ingresar son de un triángulo rectángulo y son números enteros positivos.")
confirmacion01 = input ("\n¿Confirmas que las medidas que vas ingresar son de un triángulo rectángulo y son números enteros positivos? S/N: ")
confirmacion01 = confirmación_01.upper()
if confirmación01 == "S":
  print ("\nSu respuesta ha sido 'SÍ'")
else: 
  print ("\nSu respuesta no ha sido 'Sí'\n",mensaje02)
  exit() # Salida del programa si elige la opción 'N'
  
confirmacion02 = input("\n¿Cuántos lados conoce de este triángulo? ")
if confirmacion02 == "1":
  print("\nNo es posible aplicar el Teorema de Pitágoras si solo conoce un lado.\n",mensaje02)
  exit() # Salida del programa si no cumple las condiciones
elif confirmacion02 == "2":
  confirmacion03 = input("\n¿Conoce el valor de longitud de la Hipotenusa? S/N: ")
  confirmacion03 = confirmacion03.upper()
  if confirmacion03 == "S":
    bandera = False # Se inicializa en falso para poder entrar en el ciclo While
    while bandera == False: 
      hipotenusa = input("\nIngrese el valor del Hipotenusa (Esta no debe ser menor a ninguno de los catetos): ")
      bandera = hipotenusa.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
      if bandera == False:
        print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
    hipotenusa = float(hipotenusa) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él

    bandera = False # Se inicializa en falso para poder entrar en el ciclo While
    while bandera == False:
      cateto01 = input("\nIngrese el valor del Cateto 01: ")
      bandera = cateto01.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
      if bandera == False:
        print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
    cateto01 = float(cateto01) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él
      
    if hipotenusa < cateto01: # Evalúa si el cateto ingresado es mayor a la hipotenusa
      print("\nError:Los catetos no pueden ser mayores a la hipotenusa.\n",mensaje02)
      exit() # Salida del programa si no cumple las condiciones
    else: # Esta opción se ejecuta cuando se conoce el valor de la Hipotenusa y de uno de los dos catetos
      print("\nConforme a estos datos, y aplicando el Teorema de Pitágoras:")
      print(hipotenusa,"^2 = ", cateto01,"^2 + ", "cateto02^2")
      print("\nDespejamos para obtener el valor del Cateto02:\n")
      print("Cateto02 = Raíz Cuadrada de la Resta de Hipotenusa al Cuadrado Menos Cateto01 al Cuadrado, así:")
      print("Cateto02 = Raíz Cuadrada de ", hipotenusa**2," - ", cateto01**2)
      print("Cateto02 = Raíz Cuadrada de ", hipotenusa**2 - cateto01**2)
      cateto02 = math.sqrt(hipotenusa**2 - cateto01**2)
      print("Cateto02 = ", cateto02)
  elif confirmacion03 == "N": # Esta opción se ejecuta cuando no se conoce el valor de la Hipotenusa pero si de los dos catetos

      bandera = False # Se inicializa en falso para poder entrar en el ciclo While
      while bandera == False:
        cateto01 = input("\nIngrese el valor del Cateto 01: ")
        bandera = cateto01.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
        if bandera == False:
          print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
      cateto01 = float(cateto01) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él

      bandera = False # Se inicializa en falso para poder entrar en el ciclo While
      while bandera == False:
        cateto02= input("\nIngrese el valor del Cateto 02: ")
        bandera = cateto02.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
        if bandera == False:
          print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
      cateto02 = float(cateto02) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él   
    
    # Se calcula el valor de la Hipotenusa a partir de los valores de los Catetos ingresados
      print("\nConforme a estos datos, y aplicando el Teorema de Pitágoras:")
      print("hipotenusa^2 = ", cateto01,"^2 + ", cateto02,"^2")
      print("\nDespejamos para obtener el valor de la Hipotenusa:\n")
      print("Hipotenusa = Raíz Cuadrada de ", cateto01**2," + ", cateto02**2)
      print("Hipotenusa = Raíz Cuadrada de ", cateto01**2 + cateto02**2)
      hipotenusa = math.sqrt(cateto01**2 + cateto02**2)
      print("Hipotenusa = ", hipotenusa)
  else:
    print ("\nUsted ha ingresado una opción incorrecta. '",confirmacion03,"'.\n",mensaje02)
    exit() # Salida del programa si elige la una opción errada
elif confirmacion02 == "3":
  # Ingreso de datos
  bandera = False # Se inicializa en falso para poder entrar en el ciclo While
  while bandera == False:
    cateto01 = input("\nIngrese el valor del Cateto 01: ")
    bandera = cateto01.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
    if bandera == False:
      print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
  cateto01 = float(cateto01) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él
  
  bandera = False # Se inicializa en falso para poder entrar en el ciclo While
  while bandera == False:
    cateto02= input("\nIngrese el valor del Cateto 02: ")
    bandera = cateto02.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
    if bandera == False:
      print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
  cateto02 = float(cateto02) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él 

  bandera = False # Se inicializa en falso para poder entrar en el ciclo While
  while bandera == False: 
    hipotenusa = input("\nIngrese el valor del Hipotenusa (Esta no debe ser menor a ninguno de los catetos): ")
    bandera = hipotenusa.isnumeric() # Se evalúa si el valor ingresado es Entero Positivo
    if bandera == False:
      print("\nHaz ingresado un valor incorrecto, deben ser valores enteros positivos, vuelve a intentarlo")
  hipotenusa = float(hipotenusa) # Convierte el valor texto en flotante para poder hacer operaciones matemáticas con él

  # Comprobar si ningún lado excede el tamaño de la hipotenusa
  if cateto01 > hipotenusa or cateto02 > hipotenusa:
    print("\nError: Al menos uno de los catetos es mayor a la hipotenusa.",mensaje02)
    exit() # Salida del programa si no cumple las condiciones
    # Comprobar si se trata de un triángulo rectángulo
  if cateto01**2 == hipotenusa**2 - cateto02**2 or cateto02**2 == hipotenusa**2 - cateto01**2 or hipotenusa**2 == cateto01**2 + cateto02**2: # Aquí se evalúa que los valores corresponden a los lados de un triángulo rectángulo
    print("\nEl triángulo es rectángulo, se puede aplicar el teorema de Pitágoras.")
  else:
    print("\nError: El triángulo no es rectángulo, no se puede aplicar el teorema de Pitágoras.",mensaje02)
    exit() # Salida del programa si no cumple las condiciones
else:
  print("\nError: Si no se tiene los datos de al menos dos lados, no se puede aplicar el teorema de Pitágoras.",mensaje02)
  exit() # Salida del programa si no cumple las condiciones

# Presentación del teorema de Pitágoras con los valores de los Catetos e Hipotenusa
print("\nConforme lo anterior")
print("\n1. Los tres lados del triángulo rectángulo son:")
print("\n\tCateto01 = ", cateto01, "\n\tCateto02 = ", cateto02, "\n\tHipotenusa = ", hipotenusa)
print("\n2. La representación del Teorema con estos valores es la siguiente:\n")
print("\t",hipotenusa,"^2 = ", cateto01,"^2 + ", cateto02,"^2")
print("\t",hipotenusa**2," = ", cateto01**2, " + ", cateto02**2)
print("\t",hipotenusa**2," = ", cateto01**2 + cateto02**2)
print("\n3. Aplicando la fórmula para calcular el área del triángulo:")
print("\n\tÁrea del Triángulo = Base por Altura Dividido en Dos")
print("\n\tEs decir: \n\tÁrea = (", cateto01, " * ", cateto02, ")/2")
print("\n\tTenemos que:")
print("\tÁrea = ", cateto01*cateto02, "/2")
print("\n\tY el resultado es:")
print("\tÁrea = ", cateto01*cateto02/2)
print(mensaje02)

#FIN DEL PROGRAMA