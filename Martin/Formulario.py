from Vinculacion_Py_Mongo import *
from lecturacoco import *

org = lectura()

#Tiempo del organismo
def lee_tiempo(n):
  while True:
    entrada = 300
    try:
      entrada = float(entrada)
      return entrada
    except ValueError:
      print ("La entrada es incorrecta: escribe un numero entero o flotante.")

#Largo del organismo
def lee_largo(n):
  while True:
    entrada = org[0][n]
    try:
      entrada = float(entrada)
      return entrada
    except ValueError:
      print ("La entrada es incorrecta: escribe un numero entero o flotante.")

#Ancho del organismo

def lee_ancho(n):
  while True:
    entrada = org[1][n]
    try:
      entrada = float(entrada)
      return entrada
    except ValueError:
      print ("La entrada es incorrecta: escribe un numero entero o flotante.")

# Forma del organismo
def lee_forma(n):
  while True:
    entrada = org[2][n]
    try:
      entrada = str(entrada)
      if entrada == "Coccus" or entrada == "Bacilos" or entrada == "CoccusBacilos" or entrada == "Spirillum":
        return entrada
      else:
        print("Ingresa una forma correcta (Coccus, Bacilos, CoccusBacilos, Spirillum).")
    except ValueError:
      print ("Debe ser una forma correcta.")

def respuesta():
  while True:
    entrada = len(org[0])
    try:
      entrada = int(entrada)
      return entrada
    except ValueError:
      print ("La entrada es incorrecta: escribe un numero entero.")


print (" ######## Ingresar organismo (s) ######### ")

respuesta = respuesta()

if respuesta >= 1:
  for n in range(respuesta):

    tiempo = lee_tiempo(n)
    largo = lee_largo(n)
    ancho = lee_ancho(n)
    forma = lee_forma(n)
    collection.insert_one({"Tiempo": tiempo, "Largo" : largo , "Ancho" : ancho , "Forma" : forma})

    print("Organismo guardado")
    print("Tiempo del organismo: ", tiempo)
    print("Largo del organismo: ", largo)
    print("Ancho del organismo: ", ancho)
    print("Forma del organismo: ", forma)
else :
  print("Debe ser cantidad positiva de organismos.")
