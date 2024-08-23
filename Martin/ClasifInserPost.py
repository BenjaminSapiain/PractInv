# from Formulario import *
from Vincular_Insertar_PostgreSQL import *
from Vinculacion_Py_Mongo import *
import joblib
from copy import copy

# Cargar Modelo 1
modelo1ML = joblib.load('knn_joblib_infra')
# Cargar Modelo 2
modelo2ML = joblib.load('SVM_joblib_infra2')


# Conseguir los organismos
# C r e a c i n de arreglos para almacenar caracteristicas de los organismos
docs = collection.find()
tiempo1 = []
largo1 = []
ancho1 = []
forma1 = []

# Guardo los datos en arreglos
for doc in docs :
    tiempo1.append(doc["Tiempo"])
    largo1.append(doc["Largo"])
    ancho1.append(doc["Ancho"])
    forma1.append(doc["Forma"])

forma2 = copy(forma1)
print(forma1)
print(forma2)

# Pasar strings a numeros , en el arreglo de Forma .

for n in range(len(forma1)):
    if forma1[n] == "Coccus":
        forma1[n] = 0
    elif forma1[n] == "Bacilos":
        forma1[n] = 1
    elif forma1[n] == "CoccusBacilos":
        forma1[n] = 2
    elif forma1[n] == "Spirillum":
        forma1[n] = 3

for n in range(len(forma1)):
    if forma2[n] == "Coccus":
        forma2[n] = 0
    elif forma2[n] == "Bacilos":
        forma2[n] = 1
    elif forma2[n] == "CoccusBacilos":
        forma2[n] = 2
    elif forma2[n] == "Spirillum":
        forma2[n] = 3
print(forma2)

# Comienzo de clasificaciones
for n in range(len(largo1)):
    # Usamos el modelo 1
    prediction_int3 = ''
    if forma1[n] == 0 or forma1[n] == 1:
        prediction1 = modelo1ML.predict([[largo1[n], ancho1[n]]])
        prediction_int1 = prediction1[0]
        print ("Usando modelo1: ",prediction_int1)
    # Usamos el modelo 2
        prediction2 = modelo2ML.predict([[largo1[n], ancho1[n], forma1[n]]])
        prediction_int2 = prediction2[0]
        print ("Usando modelo 2.0: ",prediction_int2)
    if forma1[n] == 2 or forma1[n] == 3:
    # Usamos modelo 2 para los sin tipo
        prediction3 = modelo2ML.predict([[largo1[n], ancho1[n], forma1[n]]])
        prediction_int3 = prediction3[0]
        print ("Usando modelo 2.1: ",prediction_int3)

    # Cambiamos las clasificaciones por palabras
    if forma2 [ n ] == 0 or forma2 [ n ] == 1:
        if prediction_int1 == 0:
            prediction_int1 = "E. coli"
        elif prediction_int1 == 1:
            prediction_int1 = "Cerevisiae"
        print ("prediccion modelo 1:", prediction_int1)

        if prediction_int2 == 0:
            prediction_int2 = "Conocido"
        elif prediction_int2 == 1:
            prediction_int2 = "Desconocido"
        print ("prediccion modelo 2:", prediction_int2)

    if forma2 [ n ] == 2 or forma2 [ n ] == 3:
        if prediction_int3 == 0:
            prediction_int3 = "Conocido"
        elif prediction_int3 == 1:
            prediction_int3 = "Desconocido"
        print("prediccion modelo 2(caso desconocido):",prediction_int3)
    
    if forma2[n] == 0 or forma2[n] == 1:

        if forma1[n] == 0:
            forma1[n] = "Coccus"
        elif forma1[n] == 1:
            forma1[n] = "Bacilos"

        if prediction_int2 == "Conocido":
            if prediction_int1 == "E. coli":
                insertarOrganismo1(tiempo1[n], largo1[n], ancho1[n], forma1[n], prediction_int1, prediction_int2)
                print("Insercion correcta: es E. Coli")

            elif prediction_int1 == "Cerevisiae":
                insertarOrganismo2(tiempo1[n], largo1[n], ancho1[n], forma1[n], prediction_int1, prediction_int2)
                print("Inserci n correcta: es S. cerevisiae")
    
    elif forma1[n] == 2 or forma1[n] == 3:
        if forma1[n] == 2:
            forma1[n] = "CoccusBacilos"
        elif forma1[n] == 3:
            forma1[n] = "Spirillum"

        insertarDesconocido(tiempo1[n], largo1[n], ancho1[n], forma1[n], prediction_int3)
        print (" Organismo desconocido .")

