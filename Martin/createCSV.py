import pandas as pd
import mysql.connector
import math

conn = mysql.connector.connect(
    host="localhost",
    database="infraestructura",
    user="root",
    password="1234"
)
cur = conn.cursor()

cur.execute("SELECT tiempo, largo, ancho, tipo, forma FROM organismo_1")

org1 = cur.fetchall()

cur.execute("SELECT tiempo, largo, ancho, tipo, forma FROM organismo_2")

org2 = cur.fetchall()
ToCsv = []

def coli(x, aux, org1, cont):
    if cont <5:
        aux.append(0)
        aux.append(100)
        aux.append(org1[x][3])

    else:
        contaux = cont - 5
        aux.append(0)
        aux.append(100 + 10*contaux)
        aux.append(org1[x][3])
    return aux

def cerv(x, aux, org2, cont):
    if cont < 5:
        aux.append(0)
        aux.append(100)
        aux.append(org2[x][3])

    elif cont < 10:
        contaux = cont - 5
        aux.append(0)
        aux.append(100 - 20*contaux)
        aux.append(org2[x][3])
    else:
        contaux = cont - 10
        aux.append(5*contaux)
        aux.append(100)
        aux.append(org2[x][3])
    return aux

contador = 0

for x in range(len(org1)):
    casoAux = '1.' + str(x+1)
    aux = []
    aux.append(casoAux)
    aux.append(300)
    if org1[x][4] == "Bacilos":
        bio = math.pi * org1[x][1] * pow((org1[x][2]/2),2)
    else:
        bio = 4/3 * math.pi * pow((org2[x][2]/2),3)
    aux.append(bio)
    aux2 = coli(x, aux, org1, contador)
    ToCsv.append(aux2)
    contador = contador + 1
    if contador == 10:
        contador = 0

contador2 = 0

for x in range(len(org2)):
    casoAux = '2.' + str(x+1)
    aux = []
    aux.append(casoAux)
    aux.append(300)
    if org2[x][4] == "Bacilos":
        bio = math.pi * org1[x][1] * pow((org1[x][2]/2),2)
    else:
        bio = 4/3 * math.pi * pow((org2[x][2]/2),3)
    aux.append(bio)
    aux2 = cerv(x, aux, org2, contador2)
    ToCsv.append(aux2)
    contador2 = contador2 + 1
    if contador2 == 15:
        contador2 = 0
    

df = pd.DataFrame(ToCsv, columns=['Caso', 'Tiempo', 'concBioinicial', 'concEtincial', 'concSusinicial', 'Bacteria'])
print(df)
df.to_csv('out.csv', sep=';')